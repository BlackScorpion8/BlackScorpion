
from urllib.parse import urlparse

def validate_scheme(url):
    """
    验证 URL 是否符合 http 或 https 协议，并且返回规范化后的 URL。
    """
    url_parts = urlparse(url)
    scheme = url_parts.scheme
    host = url_parts.netloc
    path = url_parts.path

    if not scheme:
        print('[-] 请输入 URL 的协议部分（例如：http:// 或 https://）')
        return False

    if scheme not in ['http', 'https']:
        print(f'[-] 不支持的协议 {scheme}，请使用 http 或 https 协议')
        return False

    if not host:
        print('[-] 无法解析主机名，请检查 URL 格式是否正确')
        return False

    if not path.endswith('/'):
        path += '/'

    url = f'{scheme}://{host}{path}'
    return url
