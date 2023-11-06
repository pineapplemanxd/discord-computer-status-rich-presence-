import psutil
from pypresence import Presence
import time
             
client_id = 'xxxxxxxxxxxxxxxxxxx'  
RPC = Presence(client_id, pipe=0)  # Initialize the client class
RPC.connect()  # Start the handshake loop
def get_size(bytes, suffix="B"):
    """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor
while True:  # The presence will stay on as long as the program is running
    cpu_per = round(psutil.cpu_percent(), 1)  # Get CPU Usage
    RAM_ammount = psutil.virtual_memory().total*1000000000
    mem = psutil.virtual_memory()
    mem_per = round(psutil.virtual_memory().percent, 1)
    svmem = psutil.virtual_memory()
    cores = psutil.cpu_count(logical=True)
    print(
        RPC.update(
            details="RAM usage: " + str(mem_per) + "%" +(f" | RAM ammount: : {get_size(svmem.total)}"+"GB"),
            state="CPU usage: " + str(cpu_per) + "%" + str(" | CPU cores: ")+str(cores)
        )
    )  # Set the presence

    time.sleep(15)  # Can only update rich presence every 15 seconds
