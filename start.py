import os, threading
def task1(): os.system("java -Xmx1024M -Xms1024M -jar server.jar nogui")
def task2(): os.system("ngrok tcp  25565")
threads = [threading.Thread(target=task1), threading.Thread(target=task2)]
for thread in threads:thread.start()
