import socket

def get_ip_by_site(site_url):
    try:
        # Получение IP-адреса сайта
        ip_address = socket.gethostbyname(site_url)
        return f"IP-адрес сайта {site_url}: {ip_address}"
    except socket.gaierror:
        return f"Не удалось получить IP-адрес для {site_url}."

if __name__ == "__main__":
    site_url = input("Введите URL сайта (например, google.com): ").strip()
    print(get_ip_by_site(site_url))
