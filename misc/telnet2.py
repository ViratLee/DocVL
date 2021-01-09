import telnetlib

#host = "thadcplwcm11"
host = "thadculwcm01"
port = 22
timeout = 5000
try:
    with telnetlib.Telnet(host, port, timeout) as session:
        # session.write(b"administrator\n")
        # session.write(b"password\n")
        # session.write(b"reboot\n")
        print(type(session))
except ConnectionRefusedError as err:
        print(f"telnet {host} port {port} connection refused")