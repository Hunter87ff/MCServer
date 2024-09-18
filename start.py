import os, threading
# os.system("wget https://localtonet.com/download/localtonet-linux-x64.zip")
# os.system("unzip localtonet-linux-x64.zip")
# os.system("chmod 777 ./localtonet")
with open("plugins/playiy-gg/config.yml", "w") as f: f.write(f"agent-secret: {os.environ['pggtoken']}") 
# os.system(f"sudo ngrok config add-authtoken {os.environ['ngtoken']}")
def task1(): os.system("java -Xmx1024M -Xms1024M -jar server.jar nogui")
def task2(): os.system(f"./localtonet authtoken {os.environ['lttoken']}")
threads = [threading.Thread(target=task1), threading.Thread(target=task2)]
for thread in threads:thread.start()
