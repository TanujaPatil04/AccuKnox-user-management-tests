import requests
import sys

def check_app_health(url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print(f"Application is UP (HTTP {response.status_code})")
        else:
            print(f"Application is DOWN (HTTP {response.status_code})")
    except requests.exceptions.RequestException as e:
        print(f"Application is DOWN (Error: {e})")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python app_health_checker.py <URL>")
    else:
        check_app_health(sys.argv[1])
