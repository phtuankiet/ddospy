import threading
import requests
import queue
import time

url = input("Nhập Url Web > ")
num_threads = int(input("Nhập Threading > "))
delay = float(input("Nhập Delay > "))

with open("proxies.txt", "r") as f:
    proxy_list = [line.strip() for line in f if line.strip()]

proxy_queue = queue.Queue()
for proxy in proxy_list:
    proxy_queue.put(proxy)

def worker():
    while not proxy_queue.empty():
        proxy = proxy_queue.get()
        try:
            proxies = {
                "http": f"http://{proxy}",
                "https": f"http://{proxy}"
            }
            response = requests.get(url, proxies=proxies, timeout=10)
            print(f"[OK] {proxy} -> {response.status_code}")
        except Exception as e:
            print(f"[ERR] {proxy} -> {e}")
        time.sleep(delay)
        proxy_queue.task_done()

threads = []
for _ in range(num_threads):
    t = threading.Thread(target=worker)
    t.start()
    threads.append(t)

for t in threads:
    t.join()
