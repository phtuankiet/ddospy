# Advanced DDoS Testing Tool 🚀

A professional-grade stress testing utility with advanced features for authorized penetration testing and security research.

## ⚠️ **IMPORTANT DISCLAIMER**

This tool is designed **ONLY** for:
- Authorized penetration testing
- Security research on your own systems
- Educational purposes
- Load testing of your own applications

**NEVER** use this tool against systems you don't own or have explicit permission to test. Unauthorized use may be illegal and result in legal consequences.

## 🌟 **New Advanced Features**

### 🎨 **Professional UI**
- **Color-coded output** for better readability
- **Real-time statistics** with progress tracking
- **Professional banner** and status indicators
- **Timestamped logs** for detailed tracking

### 🔧 **Advanced Functionality**
- **URL validation** with proper error handling
- **Proxy rotation** with automatic validation
- **User agent randomization** to avoid detection
- **Multiple HTTP methods** support (GET, POST, HEAD, etc.)
- **Session management** for better performance
- **Request parameter randomization** to bypass caching

### 📊 **Comprehensive Statistics**
- **Real-time request tracking**
- **Success/failure rate monitoring**
- **Requests per second calculation**
- **Detailed error categorization**
- **Automatic report generation**

### 🛡️ **Enhanced Security & Safety**
- **Input validation** to prevent crashes
- **Graceful error handling** with detailed logging
- **Configurable timeouts** and delays
- **Proxy connectivity testing** before use
- **Safe shutdown** with cleanup

### 📝 **Logging & Reporting**
- **File-based logging** (`ddos_attack.log`)
- **JSON report generation** with timestamps
- **Detailed error messages** for debugging
- **Attack summary** with statistics

## 🚀 **Installation**

### Prerequisites
```bash
pip install requests
```

### Quick Start
```bash
python3 ddos.py
```

## 📋 **Usage**

### Basic Usage
1. Run the script: `python3 ddos.py`
2. Enter the target URL when prompted
3. Specify the number of threads (1-1000)
4. Set the delay between requests
5. The tool will automatically detect and use proxies if available

### Advanced Configuration

#### Proxy Setup
Create a `proxies.txt` file with one proxy per line:
```
192.168.1.100:8080
10.0.0.1:3128
proxy.example.com:8080
```

#### Custom Headers
The tool automatically uses realistic browser headers:
- Random User-Agent rotation
- Accept headers for various content types
- Connection keep-alive
- Upgrade-Insecure-Requests

## 📊 **Output Examples**

### Real-time Output
```
[14:30:15] Worker-1 | 192.168.1.100:8080 | Status: 200 | Size: 15432 bytes
[14:30:16] Worker-2 | DIRECT | Status: 200 | Size: 15432 bytes
[14:30:17] Worker-3 | 10.0.0.1:3128 | Timeout
```

### Statistics Display
```
=== STATISTICS ===
Total Requests: 1250
Successful: 1180
Failed: 70
Success Rate: 94.4%
Requests/Second: 25.0
Elapsed Time: 50.0s
```

## 🔧 **Configuration Options**

### Environment Variables
- `DDOS_TIMEOUT`: Request timeout in seconds (default: 10)
- `DDOS_MAX_THREADS`: Maximum allowed threads (default: 1000)

### Command Line Arguments
```bash
python3 ddos.py --url https://example.com --threads 100 --delay 0.1
```

## 📁 **Generated Files**

### Log Files
- `ddos_attack.log`: Detailed execution log
- `attack_report_1234567890.json`: JSON report with statistics

### Report Format
```json
{
  "target_url": "https://example.com",
  "attack_method": "GET",
  "threads_used": 100,
  "delay": 0.1,
  "statistics": {
    "requests_sent": 1250,
    "successful_requests": 1180,
    "failed_requests": 70,
    "start_time": 1234567890.123,
    "end_time": 1234567940.123
  },
  "timestamp": "2024-01-01T12:00:00"
}
```

## 🛠️ **Technical Features**

### Advanced Error Handling
- **Connection errors**: Automatic retry with different proxies
- **Timeout handling**: Configurable timeouts per request
- **SSL errors**: Automatic certificate verification bypass
- **Proxy failures**: Automatic fallback to direct connection

### Performance Optimizations
- **Session reuse**: Maintains connections for better performance
- **Proxy rotation**: Distributes load across multiple proxies
- **Thread management**: Efficient thread pool handling
- **Memory management**: Proper cleanup and resource management

### Security Features
- **Input sanitization**: Prevents injection attacks
- **Rate limiting**: Configurable delays to avoid overwhelming targets
- **Proxy validation**: Tests proxy connectivity before use
- **Safe defaults**: Conservative settings to prevent abuse

## 🔍 **Troubleshooting**

### Common Issues

#### Proxy Connection Failures
```
[WARNING] proxies.txt not found - using direct connections
```
**Solution**: Create a `proxies.txt` file with valid proxy addresses

#### Invalid URL Format
```
[ERROR] Invalid URL format. Please enter a valid URL.
```
**Solution**: Ensure URL includes protocol (http:// or https://)

#### Thread Limit Exceeded
```
[ERROR] Please enter a number between 1 and 1000.
```
**Solution**: Reduce thread count to stay within limits

### Performance Tips
1. **Use proxies**: Distribute load across multiple IPs
2. **Optimize delays**: Balance between speed and stealth
3. **Monitor resources**: Watch CPU and memory usage
4. **Check logs**: Review `ddos_attack.log` for errors

## 📈 **Version History**

### v2.0 (Current)
- ✨ Complete rewrite with professional architecture
- 🎨 Color-coded UI and real-time statistics
- 🔧 Advanced proxy handling and validation
- 📊 Comprehensive logging and reporting
- 🛡️ Enhanced error handling and safety features

### v1.0 (Original)
- Basic threading implementation
- Simple proxy support
- Minimal error handling

## 🤝 **Contributing**

Contributions are welcome! Please ensure:
- Code follows PEP 8 style guidelines
- New features include proper error handling
- Documentation is updated for new features
- Tests are added for new functionality

## 📄 **License**

This project is for educational and authorized testing purposes only. Users are responsible for ensuring compliance with local laws and regulations.

## ⚖️ **Legal Notice**

The authors are not responsible for any misuse of this tool. Users must:
- Only test systems they own or have explicit permission to test
- Comply with all applicable laws and regulations
- Use the tool responsibly and ethically

---

**Remember: With great power comes great responsibility!** 🕷️