import socket
import threading
import time
import os
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('-t', '--sip', help="Enter you target IP")
parser.add_argument('-p', '--sport', help="Enter a valid range of ports")
args = parser.parse_args()

while True:
    if args.sip is None:
        sip = input("Please enter a valid IP : \n").strip().removeprefix("http://").removeprefix("https://").rstrip("/")
    else:
        sip = args.sip.strip().removeprefix("http://").removeprefix("https://").rstrip("/")
    try:
        sip = socket.gethostbyname(sip)
        print("IP is valid")
        break
    except (socket.gaierror, UnicodeEncodeError):
        print("IP is not valid")

while True:
    try:
        if args.sport is None:
            ps, pe = map(int, input("Please enter a valid Port range <int>-<int> : \n").strip().split("-"))
        else:
            ps, pe = map(int,args.sport.strip().split("-"))
                
        if 0 < ps <= pe <= 65535:
            break
        print("Port range must be between 1 and 65535")
    except ValueError:
        print("Invalid format. Use example: 1-1024")


#Main Scans
os.makedirs("saves", exist_ok=True)

def scan_ports(sip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1) 
    result = s.connect_ex((sip, port))
    if result == 0:
        try:
            portname = socket.getservbyport(port, 'tcp')
        except OSError:
            portname = "unknown"
        
        try:
            banner = s.recv(1024).decode(errors='ignore').strip()
        except:
            banner = ""
        
        with open(f"saves/{sip}" , "a") as f:
            if banner:
                f.write(f"Port {port} is open | {portname} | {banner}")
            else:
                f.write(f"Port {port} is open | {portname}")
            
        if banner:
            print(f"Port {port} is open | {portname} | {banner}")
        else:
            print(f"Port {port} is open | {portname}")

    

# Start threads for each link
threads = []
for port in range(ps , pe+1):
    # Using `args` to pass positional arguments and `kwargs` for keyword arguments
    t = threading.Thread(target=scan_ports, args=(sip, port))

    threads.append(t)
        

# Start each thread
with open(f"saves/{sip}" , "a") as f:
        f.write(f"starting at {time.strftime("%Y-%m-%d %H:%M:%S")} \n")
print(f"Port scans started for {sip}")
for t in threads:
    t.start()

# Wait for all threads to finish
for t in threads:
    t.join()

print(f"Port scans ended for {sip}")
            