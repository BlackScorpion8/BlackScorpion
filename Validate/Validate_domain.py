import re


def validate_domain(domain):
    pattern = r"(?:[a-zA-Z0-9](?:[a-zA-Z0-9\-]{,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6}"
    return re.match(pattern, domain)
