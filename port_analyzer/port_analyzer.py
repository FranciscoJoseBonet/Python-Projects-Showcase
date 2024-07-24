import socket

op_socket_list=[]

ip=socket.gethostbyname(socket.gethostname())                   # Get the ip for our host
print(f'Host ip to analyze: {ip}')

init_port=int(input('Initialization scan port: '))
end_port=int(input('Ending scan port: '))

for port in range(init_port,end_port):
    sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)      # Creating socket for ipV4 and TCP
    sock.settimeout(0.05)
    
    if sock.connect_ex((ip, port)) == 0:                        # Verification of the port status, if '.connect_ex' returns '0' means port is open and listening
        op_socket_list.append(port)
        sock.close()
   
print('\nThe open ports are: ')
for i, x in enumerate(op_socket_list): print(f'{i}- {x}')