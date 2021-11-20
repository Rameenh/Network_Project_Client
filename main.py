from socket import *


def main():
    clientSocket = socket(AF_INET, SOCK_STREAM)

    while True:
        clientSocket.connect(('127.0.0.1', 65432))

        mode = "y"
        while mode == 'y':

            mode = input("please type 1 for receive sorted inventory list, 2 for delete item in inventory list, 3 for "
                         "change quantity or 4 for exit\n")
            if mode == '1':
                mode2 = input("please type in sort criteria: \"name\", \"quantity\", or \"inventory_date\"\n")
                if mode2 == 'name' or mode2 == 'quantity' or mode2 == 'inventory_date':
                    clientSocket.sendall('1 {}'.format(mode2).encode())
                    data = clientSocket.recv(1024).decode()
                    print(data)
                else:
                    print('invalid sort mode')
            elif mode == '2':
                to_remove = input("please type in the name of item you want to remove from inventory\n")
                clientSocket.sendall('2 {}'.format(to_remove).encode())
            elif mode == '3':
                name_ident = input("please type in the name of the item you would like to change the quantity of\n")
                new_quantity = input('please type in the new quantity\n')
                clientSocket.sendall('3 {} {}'.format(name_ident, new_quantity).encode())
            elif mode == '4':

                quit()
            else:
                print("invalid mode chosen")
            mode = input("would you like to continue? y/n\n")





main()
