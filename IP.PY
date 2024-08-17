import time
from stem import Signal
from stem.control import Controller
import requests

# Function to print the banner
def print_banner():
    banner = """
\033[1;31m_____________________________________________________________
_____________________________________________________________
                                  {ALU  AUTO IP CHANGER}
______________________________________________________________
_______________________________________________________________
                                                         BY "ALVANOSH JOJO"
________________________________________________________________
_______________________________________________________________\033[0m
    """
    print(banner)

def get_new_ip():
    try:
        with Controller.from_port(port=9051) as controller:
            controller.authenticate(password='your_password')  # Set your Tor password here
            controller.signal(Signal.NEWNYM)
            time.sleep(10)  # Increased wait time for the IP to change
    except Exception as e:
        print(f"Error: {e}")

def get_current_ip():
    try:
        response = requests.get('http://httpbin.org/ip', proxies={'http': 'socks5://127.0.0.1:9050', 'https': 'socks5://127.0.0.1:9050'})
        return response.json()['origin']
    except Exception as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    print_banner()  # Print the banner at the start
    while True:
        get_new_ip()
        new_ip = get_current_ip()
        if new_ip:
            print("New IP Address:", new_ip)
        time.sleep(120)  # Change IP every 120 seconds (2 minutes)
