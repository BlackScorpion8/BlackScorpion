import threading
from concurrent.futures import ThreadPoolExecutor
import requests
import os
from bs4 import BeautifulSoup
from RandomFunc.generate_random_headers import generate_random_headers
import warnings
from urllib3.exceptions import InsecureRequestWarning

warnings.simplefilter('ignore', InsecureRequestWarning)


def check_url(url, directory, timeout, headers, lock):
    """
    检查URL是否存在指定的目录。
    """
    try:
        response = requests.get(f"{url.rstrip('/')}/{directory}", allow_redirects=False, timeout=timeout,
                                headers=headers, verify=False)

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            title = soup.title.string if soup.title else "N/A"
            result = f'[+] {url.rstrip("/")}/{directory} ({response.status_code}): {title}'
        elif response.status_code in [301, 302]:
            result = f'[+] {url.rstrip("/")}/{directory} -> {response.headers["location"]} ({response.status_code})'
        elif response.status_code == 400:
            result = f'[-] {url.rstrip("/")}/{directory} - Bad Request ({response.status_code})'
        elif response.status_code == 401:
            result = f'[-] {url.rstrip("/")}/{directory} - Unauthorized Access ({response.status_code})'
        elif response.status_code == 403:
            result = (f'[-] {url.rstrip("/")}/{directory} - Forbidden')
        elif response.status_code == 404:
            print(f"scan {url}{directory}\t{response.status_code}")
            return
        else:
            result = f'[-] {url.rstrip("/")}/{directory} ({response.status_code})'

        with lock:
            print(f"scan {url}{directory}\t{response.status_code}")
            with open(os.path.join('Result', 'dirs.txt'), 'a') as f:
                f.write(result + '\n')

    except requests.exceptions.Timeout:
        print(f'[-] {url.rstrip("/")}/{directory} - Timeout')
    except requests.exceptions.ConnectionError:
        print(f'[-] {url.rstrip("/")}/{directory} - Connection Error')

def check_urls(url, directories, timeout):
    """
    使用线程池和锁来实现高并发扫描目录。
    """
    lock = threading.Lock()

    try:
        with ThreadPoolExecutor() as executor:
            futures = []
            for directory in directories:
                futures.append(executor.submit(check_url, url, directory, timeout, generate_random_headers(), lock))
            for future in futures:
                future.result()
    except KeyboardInterrupt:
        print("\nScan interrupted by user. Exiting...")
