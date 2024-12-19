import requests

def get_ip_info(ip):
    """
    Получить информацию об IP-адресе с использованием сервиса ip-api.
    :param ip: Строка с IP-адресом.
    :return: Словарь с информацией об IP или None, если запрос не удался.
    """
    url = f"http://ip-api.com/json/{ip}?fields=status,message,country,regionName,city,lat,lon,isp"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if data["status"] == "success":
                return data
            else:
                print(f"Ошибка: {data['message']}")
                return None
        else:
            print(f"HTTP ошибка: {response.status_code}")
            return None
    except Exception as e:
        print(f"Ошибка: {e}")
        return None


def main():
    ip = input("Введите IP-адрес: ").strip()
    if not ip:
        print("IP-адрес не может быть пустым.")
        return

    info = get_ip_info(ip)

    if info:
        print("\nИнформация об IP:")
        print(f"Страна: {info.get('country')}")
        print(f"Регион: {info.get('regionName')}")
        print(f"Город: {info.get('city')}")
        print(f"Провайдер: {info.get('isp')}")
        print(f"Широта: {info.get('lat')}")
        print(f"Долгота: {info.get('lon')}")

if __name__ == "__main__":
    main()
