import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from concurrent.futures import ThreadPoolExecutor
import threading
import os

result_folder = "Result"
if not os.path.exists(result_folder):
    os.makedirs(result_folder)


def check_subdomain(subdomain, domain, results, lock, timeout=10):
    domain = domain.strip().lower().replace("http://", "").replace("https://", "")
    parser_url = urlparse("http://" + domain)
    domain = parser_url.netloc.split(':')[0]

    url = f'http://{subdomain}.{domain}'
    try:
        r = requests.get(url, timeout=timeout)
        code = r.status_code
        soup = BeautifulSoup(r.content, 'html.parser')
        title = soup.title.string if soup.title else None
        with lock:
            results.append({'url': url, 'code': code, 'title': title})
    except requests.ConnectionError:
        pass
    except requests.exceptions.ReadTimeout:
        pass

    url = f'https://{subdomain}.{domain}'
    try:
        r = requests.get(url, timeout=timeout)
        code = r.status_code
        soup = BeautifulSoup(r.content, 'html.parser')
        title = soup.title.string if soup.title else None
        with lock:
            results.append({'url': url, 'code': code, 'title': title})
    except requests.ConnectionError:
        pass
    except requests.exceptions.ReadTimeout:
        pass


def check_subdomains(subdomains, domain, timeout=10):
    domain = domain.strip().lower().replace("http://", "").replace("https://", "")
    parser_url = urlparse("http://" + domain)
    domain = parser_url.netloc.split(':')[0]
    print(f'[+] Domain: {domain}')

    results = []
    lock = threading.Lock()

    with ThreadPoolExecutor() as executor:
        futures = executor.map(lambda subdomain: check_subdomain(subdomain, domain, results, lock, timeout), subdomains)
        for future in futures:
            pass

    results.sort(key=lambda x: x['code'])
    result_file = os.path.join(result_folder, "subdomain.txt")

    with open(result_file, "a") as f:
        f.write(f'[+] Domain: {domain} \n')
        for result in results:
            url = result['url']
            code = result['code']
            title = result.get('title', '')
            if code <= 401:
                f.write(f'[+] Discovered subdomain: {url} status code: {code} title: {title}\n')
            else:
                f.write(f'[-] Discovered subdomain: {url} status code: {code}\n')

    print(f"Results have been saved to {result_file}")
