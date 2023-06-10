#!usr/bin/python3
from netmiko import ConnectHandler




router_mikotik = {
        "device_type" : "mikrotik_routeros",
        "host" :  "192.168.1.1",
        "username" : "admin",
        "password" : "Ctplus12!",
        "port" : 22,}
try:
    net_connect = ConnectHandler(**router_mikotik)
    output = net_connect.send_command("/interface print")
    print(output)

    output = net_connect.send_command("/ip address print")
    print(output)

    output = net_connect.send_command("/system resource print")
    print(output)

    net_connect.disconnect()
except Exception as e:
    print("An error occurred:", str(e))





#for componets in commands:
 #output = net_connect.send_command (commands, cmd_verfy=True)
 #print(output)


