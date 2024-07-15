import os
import paramiko
from pathlib import PurePosixPath

HOSTNAME='192.168.0.84'
USERNAME='ft'
PASSWORD='fischertechnik'

def copy_helper(sftp: paramiko.SFTPClient, src: str, dest: str):
    sftp.mkdir(dest)
    
    for item in os.listdir(src):
        local_item = src + '/' + item
        remote_item = dest + '/' + item

        if os.path.isdir(local_item):
            copy_helper(sftp, local_item, remote_item)
        else:
            sftp.put(local_item, remote_item)

def upload(sftp: paramiko.SFTPClient, project_name: str, dest: str):
    copy_helper(sftp, project_name, dest + '/' + project_name )

def main():
    ssh = paramiko.SSHClient() 
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(HOSTNAME, username=USERNAME, password=PASSWORD)

    stdin, stdout, stderr = ssh.exec_command("sudo -S rm -r /opt/ft/workspaces/ft_example")
    stdin.write(PASSWORD + '\n')
    stdin.flush()

    print(stdout.readlines(), stderr.readlines())
    sftp = ssh.open_sftp()

    upload(sftp, 'ft_example', '/opt/ft/workspaces')
    
    sftp.close()
    ssh.close()

if __name__ == '__main__':
    main()