"""
Target list generator For IPs 192.168.1.1 to 192.168.1.5 and ports 22, 80,
443 , print every ip:port combination. Hint: nested for , with the ports in a list. Expected:
15 lines beginning 192.168.1.1:22
"""
def target_list_generator():
    ports =[22,80,443]
    for i in range(1,6):
        for port_number in ports:
          print(f"192.168.1.{i}:{port_number}")
target_list_generator()
