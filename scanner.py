import socket

while True:
    while True:
        sip = input("Please enter a valid IP : \n").strip().removeprefix("http://").removeprefix("https://").rstrip("/")
        try:
            sip = socket.gethostbyname(sip)
            print("IP is valid")
            break
        except (socket.gaierror, UnicodeEncodeError):
            print("IP is not valid")

    while True:
        try:
            ps, pe = map(int, input("Please enter a valid Port range <int>-<int> : \n").strip().split("-"))
            if 0 < ps <= pe <= 65535:
                break
            print("Port range must be between 1 and 65535")
        except ValueError:
            print("Invalid format. Use example: 1-1024")



    