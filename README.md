


# SSH Brute-Force Scripts

These Python scripts attempt to brute-force SSH credentials for a given host using various combinations of usernames and passwords.

## Prerequisites

- Python 3.x
- Paramiko library (install via `pip install paramiko`)

## 1. Password Brute-Force

### Usage

1. Clone or download the repository containing the script to your local machine.
2. Ensure you have a list of common passwords in a file named `ssh-common-password.txt` in the same directory as the script.
3. Run the script using Python:

```bash
python ssh_pass_brute_force.py
```

4. Follow the prompts to enter the host, port, and username.
5. The script will attempt to brute-force SSH passwords using the provided information.

### Notes

- The default port for SSH is 22. If your target SSH server uses a different port, specify it when prompted.
- Ensure you have proper authorization before attempting to brute-force SSH passwords. Unauthorized access attempts may be illegal and unethical.
- It's recommended to use this script for educational or testing purposes only and not for malicious activities.

### Disclaimer

This script is provided for educational purposes only. The author is not responsible for any misuse or damage caused by this script.

## 2. Username Brute-Force

### Usage

1. Clone or download the repository containing the script to your local machine.
2. Ensure you have a list of common usernames in a file named `ssh-common-username.txt` in the same directory as the script.
3. Run the script using Python:

```bash
python ssh_user_brute_force.py
```

4. Follow the prompts to enter the host, port, and password.
5. The script will attempt to brute-force SSH usernames using the provided information.

### Notes

- The default port for SSH is 22. If your target SSH server uses a different port, specify it when prompted.
- Ensure you have proper authorization before attempting to brute-force SSH usernames. Unauthorized access attempts may be illegal and unethical.
- It's recommended to use this script for educational or testing purposes only and not for malicious activities.

### Disclaimer

This script is provided for educational purposes only. The author is not responsible for any misuse or damage caused by this script.

## 3. Combined Username and Password Brute-Force

### Usage

1. Clone or download the repository containing the script to your local machine.
2. Ensure you have a list of common usernames in a file named `ssh-common-username.txt` and a list of common passwords in a file named `ssh-common-password.txt` in the same directory as the script.
3. Run the script using Python:

```bash
python ssh_brute_force.py
```

4. Follow the prompts to enter the host and port.
5. The script will attempt to brute-force SSH credentials using the provided information.

### Notes

- The default port for SSH is 22. If your target SSH server uses a different port, specify it when prompted.
- Ensure you have proper authorization before attempting to brute-force SSH credentials. Unauthorized access attempts may be illegal and unethical.
- It's recommended to use this script for educational or testing purposes only and not for malicious activities.

### Disclaimer

This script is provided for educational purposes only. The author is not responsible for any misuse or damage caused by this script.


