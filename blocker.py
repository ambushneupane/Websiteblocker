import time
from datetime import datetime as dt 

host_path= r'C:\Windows\System32\drivers\etc\hosts'
redirect= "127.0.0.1"

websites_to_block=["www.instagram.com",'instagram.com']

print(dt.now())
# exit()

today_date= dt(dt.now().year,dt.now().month,dt.now().day)

def block_website(start_hour,end_hour):
    blocking_Start_time= dt(dt.now().year,dt.now().month,dt.now().day,start_hour)
    blocking_end_time= dt(dt.now().year,dt.now().month,dt.now().day,end_hour)
    while True:
        if blocking_Start_time < dt.now() < blocking_end_time:
            print("Blocking the sites")
            with open(host_path,'r+') as hostfile:
                content= hostfile.read()
                # hostfile.seek(0)
                for site in websites_to_block:
                    if site in content:
                        pass
                    else: 
                        hostfile.write(redirect +' '+ site +'\n' )
            print("Websites Blocked")
        else:
            with open(host_path,'r+') as hostfile:
                hosts= hostfile.readlines()
                hostfile.seek(0)
                for host in hosts:
                    if not any(site in host for site in websites_to_block ):
                        hostfile.write(host)
                hostfile.truncate()
           
            time.sleep(2)
if __name__=="__main__":
    block_website(16,17)