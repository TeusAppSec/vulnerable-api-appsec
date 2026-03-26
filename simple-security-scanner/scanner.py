import requests

def check_headers(url):
    print(f"\n[+] Scanning {url}\n")

    try:
        response = requests.get(url)
    except:
        print("[-] Failed to connect")
        return

    headers = response.headers

    security_headers = {
        "X-Content-Type-Options": "Prevents MIME sniffing",
        "X-Frame-Options": "Prevents clickjacking",
        "Content-Security-Policy": "Mitigates XSS",
        "Strict-Transport-Security": "Enforces HTTPS"
    }

    for header, desc in security_headers.items():
        if header in headers:
            print(f"[OK] {header} present")
        else:
            print(f"[!] Missing {header} - {desc}")

if __name__ == "__main__":
    target = input("Enter target URL: ")
    check_headers(target)