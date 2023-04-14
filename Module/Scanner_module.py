from Script.Scanner_script import check_subdomains

import os
from Validate.Validate_domain import validate_domain
from Validate.Validate_file import validate_file

def Scanner_module(language):
    print("\nSubdomain enumeration tool / 子域名枚举工具")
    default_file_path = os.path.join(os.getcwd(), 'dist', 'subdomains.txt')

    while True:
        if language == "en":
            domain = input("Enter the domain to scan (example.com):")
        elif language == "cn":
            domain = input("输入要扫描的域名：")

        if validate_domain(domain):
            break
        else:
            if language == "en":
                print("Invalid domain format, please enter a valid domain (example.com)")
            elif language == "cn":
                print("域名格式无效，请输入有效的域名（例如：example.com）")

    while True:
        if language == "en":
            file_path = input(
                f"Enter the path of the file containing subdomains (default: {default_file_path}): ") or default_file_path
            timeout_str = input("Enter the timeout for requests (default: 10): ")
        elif language == "cn":
            file_path = input(f"输入包含子域名的文件路径（默认：{default_file_path}）：") or default_file_path
            timeout_str = input("输入请求超时时间（默认：10）：")
        if validate_file(file_path):
            break
        else:
            if language == "en":
                print("Invalid file path, please enter a valid file path")
            elif language == "cn":
                print("文件路径无效，请输入有效的文件路径")

    if timeout_str.isdigit():
        timeout = int(timeout_str)
    else:
        timeout = 10

    with open(file_path,encoding='utf-8') as f:
        subdomains = f.read().splitlines()
        check_subdomains(subdomains, domain, timeout)
