import os

cmd1 = "wget https://raw.githubusercontent.com/ant-media/Scripts/master/install_ant-media-server.sh -O install_ant-media-server.sh  && chmod 755 install_ant-media-server.sh" 
cmd2 = "sudo ./install_ant-media-server.sh"

os.system(cmd1 + "&&" + cmd2)