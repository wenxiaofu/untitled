import time
import paramiko


def verification_ssh(host,username,password,port,root_pwd,cmd):
    print(111111111111)
    s=paramiko.SSHClient()
    s.load_system_host_keys()
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    print(host+username+password)
    s.connect(hostname = host,port=port,username=username, password=password)
    if username != 'root':
        ssh = s.invoke_shell()
        time.sleep(0.1)
        ssh.send('su - \n')
        # time.sleep(2)
        buff = ''
        while (("Password" in buff) == False):
            resp = ssh.recv(999)
            resp1 = str(resp)
            print("-------------" + resp1 + "------------------")
            buff += resp1
            print("Password" in buff)
            print(buff)
        print("lalala ")
        ssh.send(root_pwd)
        ssh.send('\n')
        time.sleep(2)
        buff = ''
        #here is use for test the response
        while (("#" in buff) == False):
            resp = str(ssh.recv(999))
            buff += resp
            print(buff)
        ssh.send(cmd)
        ssh.send('\n')
        #发送命令
        buff = ''
        while (("#" in buff) == False):
            resp = str(ssh.recv(999))
            buff += resp
            print(buff)
        s.close()
        #result = buff
        print("hahahha ")
        result = buff
    else:
        stdin, stdout, stderr = s.exec_command(cmd)
        result = stdout.read()
        s.close()
    return result


if __name__ == "__main__":
    a=verification_ssh('200.200.169.100', 'background', 'moatest', 22, 'OrYuWFHeLDBtgX1BitJu', 'ifconfig')
    print("-------"+a)