import logging
import socket
import time
def work():
    hostname = socket.gethostname()
    ipaddress = socket.gethostbyname(hostname)
    logging.basicConfig(format='%(asctime)-2s %(message)s',datefmt='%d/%m/%y %H:%M:%S %p',filename="output",encoding='utf-8',level=logging.DEBUG)
    logging.info("Hostname:"+hostname+" "+"IP:"+ipaddress)
if __name__=='__main__':
    while True:
        work()
        time.sleep(60)
