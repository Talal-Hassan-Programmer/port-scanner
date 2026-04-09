# 🔍 Port Scanner

A fast, multithreaded Python port scanner built from scratch using raw sockets. No external dependencies required.

> Built as part of a personal Python + cybersecurity learning roadmap.

---

## ✨ Features

| Feature | Status |
|---|---|
| Accepts IP addresses and hostnames | ✅ |
| Auto-cleans input (strips http://, https://, slashes) | ✅ |
| Validates IP/hostname before scanning | ✅ |
| Custom port range input (e.g. 1-1024) | ✅ |
| Multithreaded scanning — all ports checked simultaneously | ✅ |
| Displays service name for each open port | ✅ |
| Saves scan results to a .txt file | ✅ |
| CLI argument support with argparse | ✅ |
| Banner grabbing (detect software versions on open ports) | ✅ |
| Upgrade to python-nmap for advanced scanning | 🔜 |

---

## 📁 Project Structure

```
port-scanner/
│
├── scanner.py       # All scanning logic
├── saves/           # Scan results saved here (git-ignored)
├── .gitignore       # Ignores saves/ folder
├── LICENSE          # MIT License
└── README.md        # This file
```

---

## 🚀 Usage

### With CLI arguments

```bash
python scanner.py -t scanme.nmap.org -p 1-1024
```

### Interactive mode (no arguments)

```bash
python scanner.py
```

```
Please enter a valid IP or hostname:
> scanme.nmap.org

Please enter a valid port range <int>-<int>:
> 1-1024

Port scans started for 45.33.32.156
Port 22 is open | ssh | SSH-2.0-OpenSSH_6.6.1p1 Ubuntu-2ubuntu2.13
Port 80 is open | http
Port scans ended for 45.33.32.156
```

Results are automatically saved to `saves/45.33.32.156.txt`.

### Arguments

| Argument | Description |
|---|---|
| `-t`, `--sip` | Target IP address or hostname |
| `-p`, `--sport` | Port range in format `start-end` (e.g. `1-1024`) |

---

## ⚙️ How It Works

1. Input is validated and resolved to an IP using `socket.gethostbyname()`
2. One thread is spawned per port using `threading.Thread`
3. Each thread attempts a TCP connection with a 1 second timeout via `socket.connect_ex()`
4. Open ports are printed with their service name from `socket.getservbyport()`
5. If the service sends a response, the banner is captured using `socket.recv(1024)` and displayed
6. Results are written to a `.txt` file inside the `saves/` folder

---

## 📋 Requirements

- Python 3.x
- No external libraries — uses only built-in `socket`, `threading`, `argparse`, `os`, and `time` modules

---

## ⚠️ Legal

Only scan hosts you own or have explicit permission to scan.  
`scanme.nmap.org` is provided by the nmap project for legal scanning practice.

---

## ✍️ Author

**Talal Hassan** — Competitive Programmer · IOI Qatar 2026 National Champion · Cybersecurity Enthusiast 🇶🇦  
[GitHub — Talal-Hassan-Programmer](https://github.com/Talal-Hassan-Programmer)

---

## 📄 License

Licensed under the [MIT License](https://opensource.org/licenses/MIT) — free to use and modify.