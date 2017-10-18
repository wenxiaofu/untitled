
#!/usr/bin/env python
import paramiko
import time
hostname = '200.200.169.212'
port = 22
username = "root"
password = "moatest"
if __name__ == "__main__":
        s = paramiko.SSHClient()
        s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        s.connect(hostname, port, username, password)
        stdin, stdout, stderr = s.exec_command('mdbg -p 21024 -o exportdomain')
        print(stdout.read())
        channel = s.invoke_shell()
        channel.send("su - elasticsearch\n")
        channel.send("su - root\n")
        while not channel.recv_ready():
            print
            "Working..."
            time.sleep(2)
        print
        channel.recv(1024)
        channel.send("%s\n" % "moatest")
        while not channel.recv_ready():
            print
            "Authenticating..."
            time.sleep(2)
        print
        channel.recv(1024)
        channel.send("yum update <rpm>\n")
        while not channel.recv_ready():
            print
            "Working on part 3..."
            time.sleep(10)
        print
        channel.recv(1024)
        s.close()