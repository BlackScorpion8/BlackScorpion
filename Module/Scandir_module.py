from Validate.Validate_scheme import validate_scheme
from Validate.Validate_file import validate_file
from Script.Scandir_script import check_urls
import os
import requests
import time
from RandomFunc.generate_random_headers import generate_random_headers

def Scandir_module(language):
    """
    主函数：解析命令行参数并执行目录扫描。
    """
    print("\nDirectory scan tool / 目录扫描工具")

    while True:
        if language == "en":
            url = input("Please enter the url to scan:").strip()
        elif language == "cn":
            url = input("请输入要扫描的URL：").strip()

        # 调用 validate_scheme 函数检查 URL 是否合法
        url_valid = validate_scheme(url)

        if url_valid:
            # 发送 GET 请求获取网站状态码
            r = requests.get(url,headers=generate_random_headers(), verify=False)
            if r.status_code == 404:
                if language == "en":
                    print("Web connection failed, 404 not found, please check the URL and try again")
                elif language == "cn":
                    print("网络连接失败，404未找到，请检查URL并重试")
                continue
            else:
                # 如果状态码正确，跳出循环

                if language == "en":
                    print(
                        f"[*] The URL {url} is valid, the status code is {r.status_code}，request time is {r.elapsed.total_seconds()} seconds")
                elif language == "cn":
                    print(
                        f"[*] The URL {url} is valid, the status code is {r.status_code}，请求耗时间为 {r.elapsed.total_seconds()} 秒")
                break

        else:
            # 如果 URL 不合法，提示错误并继续循环
            pass

    default_file_path = os.path.join(os.getcwd(), 'dist', 'dirs.txt')

    while True:
        if language == "en":
            file_path = input(
                f"Enter the path of the file containing directories (default: {default_file_path}): ") or default_file_path
            timeout_str = input("Enter the timeout for requests (default: 10): ")
        elif language == "cn":
            file_path = input(f"输入包含目录的文件路径（默认：{default_file_path}）：") or default_file_path
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

    directories = []
    with open(file_path, encoding='utf-8') as f:
        for line in f:
            line = line.strip()  # 去除行尾的换行符
            line = line.lstrip('/')  # 去除行首的斜杠
            directories.append(line)

    if url_valid:
        start_time = time.time()

        check_urls(url, directories, timeout)

        end_time = time.time()
        elapsed_time = round(end_time - start_time, 2)

        print(f"Total elapsed time: {elapsed_time}s")
