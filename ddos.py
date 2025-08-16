import threading
import requests
import queue
import time
import os

url = input("Nhập Url Web > ")
num_threads = int(input("Nhập Threading > "))
delay = float(input("Nhập Delay > "))

proxy_queue = queue.Queue()

# Nếu có file proxies.txt thì mới load
if os.path.exists("proxies.txt"):
    with open("proxies.txt", "r") as f:
        proxy_list = [line.strip() for line in f if line.strip()]
    for proxy in proxy_list:
        proxy_queue.put(proxy)
    use_proxy = True
else:
    print("[!] Không tìm thấy proxies.txt -> Sử dụng direct request")
    use_proxy = False

def worker():
    while True:
        if use_proxy:
            if proxy_queue.empty():
                break
            proxy = proxy_queue.get()
            proxies = {
                "http": f"http://{proxy}",
                "https": f"http://{proxy}"
            }
        else:
            proxies = None

        try:
            response = requests.get(url, proxies=proxies, timeout=10)
            proxy_info = proxy if use_proxy else "NO_PROXY"
            print(f"[OK] {proxy_info} -> {response.status_code}")
        except Exception as e:
            proxy_info = proxy if use_proxy else "NO_PROXY"
            print(f"[ERR] {proxy_info} -> {e}")
        time.sleep(delay)

        if use_proxy:
            proxy_queue.task_done()

threads = []
for _ in range(num_threads):
    t = threading.Thread(target=worker)
    t.start()
    threads.append(t)

for t in threads:
    t.join()
