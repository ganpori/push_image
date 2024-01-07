import paramiko
import os

from dotenv import load_dotenv
import scp




if __name__=="__main__":
    load_dotenv()
    ip=os.environ.get("HostName")
    port=os.environ.get("Port")
    user=os.environ.get("User")
    path_key=os.environ.get("IdentityFile")

    local_path="/tmp_camera/images"
    remote_path="/tmp/camera_images"
    with paramiko.SSHClient() as sshc:
        sshc.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        sshc.connect(hostname=ip, port=port,username=user,key_filename=path_key)
        with sshc.open_sftp() as sftp:
            try:
                sftp.chdir(remote_path)
            except FileNotFoundError:
                sftp.mkdir(path=remote_path)
                sftp.chdir(remote_path)
            
