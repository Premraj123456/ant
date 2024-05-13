import os
cmd = "sudo apt-get install coreutils"
cmd1 = "chmod 755 install_ant-media-server.sh" 
cmd2 = "sudo ./install_ant-media-server.sh"
cmd3 = "sudo service antmedia start"
os.system(cmd + "&&" + cmd1 + "&&" + cmd2+ "&&" +cmd3)
