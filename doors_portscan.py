import sys
import os
import socket
from time import sleep
from IPy import IP
from stringcolor import *

slgn = cs("██▓ ██▓     ▓█████▄  ▒█████   ▒█████   ██▀███    ██████       ██▓ ██▓\n"
          "▓██▒▓██▒     ▒██▀ ██▌▒██▒  ██▒▒██▒  ██▒▓██ ▒ ██▒▒██    ▒      ▓██▒▓██▒\n"
          "▒██▒▒██▒     ░██   █▌▒██░  ██▒▒██░  ██▒▓██ ░▄█ ▒░ ▓██▄        ▒██▒▒██▒\n"
          "░██░░██░     ░▓█▄   ▌▒██   ██░▒██   ██░▒██▀▀█▄    ▒   ██▒     ░██░░██░\n"
          "░██░░██░     ░▒████▓ ░ ████▓▒░░ ████▓▒░░██▓ ▒██▒▒██████▒▒     ░██░░██░\n"
          "░▓  ░▓        ▒▒▓  ▒ ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░▒ ▒▓▒ ▒ ░     ░▓  ░▓  \n"
          " ▒ ░ ▒ ░      ░ ▒  ▒   ░ ▒ ▒░   ░ ▒ ▒░   ░▒ ░ ▒░░ ░▒  ░ ░      ▒ ░ ▒ ░\n"
          " ▒ ░ ▒ ░      ░ ░  ░ ░ ░ ░ ▒  ░ ░ ░ ▒    ░░   ░ ░  ░  ░        ▒ ░ ▒ ░\n"
          " ░   ░          ░        ░ ░      ░ ░     ░           ░        ░   ░  \n"
          "              ░                                                        ", "red")

default_ports = {'ECHO     ': 7,
                 'FTP-DATA ': 20,
                 'FTP      ': 21,
                 'SSH      ': 22,
                 'TELNET   ': 23,
                 'SMTP     ': 25,
                 'DOMAIN   ': 53,
                 'TFTP     ': 69,
                 'HTTP     ': 80,
                 'POP3     ': 110,
                 'NNTP     ': 119,
                 'SNMP     ': 161,
                 'SNMP-TRAP': 162,
                 'HTTPS    ': 443
                 }
user_loaded = {}
user_predef = {}
final_text = []


def delayed_print(text):
    for char in text:
        sleep(0.05)
        sys.stdout.write(char)
        sys.stdout.flush()


def save_file():
    global final_text
    x = input(cs('\n[-_+] SCAN FINISHED\n', 'green').bold() +
              '[1] Save file (txt)\n'
              '[2] SCAN another target\n'
              '[3] Finish\n'
              '[>>>] ')
    if x == '1':
        file_name = input(bold('\n[---] Enter a file name: \n') +
                          '[>>>] ')
        with open(file_name + '_scan.txt', 'w') as file:
            for line in final_text:
                file.write(line)
            file.close()
            final_text.clear()
        print(bold(f"\n[+++] FILE SAVED: {file_name + '_scan.txt'}"))
        sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
    elif x == '3':
        print(bold('\n[###] PROGRAM FINISHED'))
        sleep(1)
        exit(0)


def check_ip(adress):
    try:
        IP(adress)
        return adress
    except ValueError:
        return socket.gethostbyname(adress)


def add_port(ports_dict):
    run = True
    while run:
        service_port = input(bold('\n[---] ADDING PORT\n') +
                             '[#] Input in format "service:port"\n'
                             '[>>>] ')
        service, port = service_port.split(':')
        ports_dict.update({service.upper(): int(port)})
        print(bold(f'[+++] SERVICE: {service.upper()} || PORT: {int(port)} ADDED'))
        x = input('[1] - Add another SERVICE:PORT\n'
                  '[2] - Go back\n'
                  '[>>>] ')
        if x == '2':
            break


def main():
    choice = None

    while choice != 'exit':
        print(f'\n\n{slgn}\n\n')  # Print slogan
        print('# Created by Luiz Gustavo for educatational purposes, based in a\n'
              '# Afonso da Silva class available in the TDI community.\n')
        choice = input(bold('[---] Choose an option:\n') +
                       '[1] - SCAN\n'
                       '[2] - Configurations\n'
                       '[3] - Finish\n'
                       + bold('[>>>] '))
        if choice == '1':
            domain = input(bold('\n[---] Enter with TARGET(s):\n'
                                '[#] You can pass multiple targets separated by ","\n'
                                '[>>>] '))
            dict_scan = input(bold('\n[---] Choose a PORT-DICT:\n') +
                              '[1] - Default\n'
                              '[2] - User defined\n'
                              '[3] - Loaded\n'
                              '[4] - Go Back \n[>>>] ')
            if dict_scan == '1':
                dict_scan = default_ports
            elif dict_scan == '2':
                dict_scan = user_predef
            elif dict_scan == '3':
                dict_scan = user_loaded
            else:
                sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')
            if dict_scan in [default_ports, user_predef, user_loaded]:
                show_ports = input(bold('\n[---] Do you wish to show CLOSED PORTS [y/n]?\n>> ')).upper()
                print(bold('\n[-_*] INITIALIZING'))
                if ',' in domain:
                    try:
                        for address in domain.split(','):
                            converted_domain = check_ip(address.strip())
                            print(f'\n[->-] SCANNING TARGET: {address.strip()}')
                            final_text.append(f'\n[->-] SCANNING TARGET: {address.strip()}\n')
                            scan(converted_domain, show_ports, dict_scan)
                        save_file()
                    except Exception:
                        print('[-X-] Stopping... Maybe there is a an mistake in your TARGETS')
                else:
                    converted_domain = check_ip(domain)
                    print(f'\n[->-] SCANNING TARGET: {domain}')
                    final_text.append(f'\n[->-] SCANNING TARGET: {domain.strip()}\n')
                    scan(converted_domain, show_ports, dict_scan)
                    save_file()
        elif choice == '2':
            choice_x = input(bold('\n[---] CONFIGURATION\n') +
                             '[1] - Define a service:port\n'
                             '[2] - Show existing services:ports\n'
                             '[3] - Go back\n'
                             '[>>>] ')
            if choice_x == '1':
                choice_y = input(bold('\n[---] DEFINING PORT\n') +
                                 '[1] - Add to DEFAULT_DICT\n'
                                 '[2] - Define a new PORT_DICT\n'
                                 '[3] - Load a file\n'
                                 '[4] - Go back\n'
                                 '[>>>] ')
                # ============================== ADDING TO DEFAULT PORT-DICT!
                if choice_y == '1':
                    add_port(default_ports)
                    z = input(bold('\n[+++] PORTS CONFIGURED\n') +
                              '[1] - Save file\n'
                              '[2] - Go back to MENU\n'
                              '[>>>]')
                    if z == '1':
                        file_name = input(bold('\n[---] Choose your file name:'
                                               '[#] EX: target01\n') +
                                          '[>>>]')
                        with open(file_name + '_predef.txt', 'w') as arquivo:
                            for line in default_ports.items():
                                arquivo.write(f'{line[0]}:{line[1]}\n')
                            arquivo.close()
                        print(bold(f"\n[+++] FILE SAVED: {file_name + '_predef.txt'}"))
                        sleep(2)
                        os.system('cls' if os.name == 'nt' else 'clear')
                # ============================== CREATING A PORT-DICT!
                elif choice_y == '2':
                    add_port(user_predef)
                    file_name = input(bold('\n[---] Choose your file name:'
                                           '[#] EX: target01\n') +
                                      '[>>>]')
                    with open(file_name + '_predef.txt', 'w') as arquivo:
                        for linha in user_predef.items():
                            arquivo.write(f'{linha[0]}:{linha[1]}\n')
                        arquivo.close()
                    print(bold(f"\n[+++] FILE SAVED: {file_name + '_predef.txt'}"))
                    sleep(2)
                    os.system('cls' if os.name == 'nt' else 'clear')
                # ============================== LOADING A PORT-DICT!
                elif choice_y == '3':
                    file_name = input(bold('\n[---] Enter with the file name:\n'))
                    try:
                        with open(file_name, 'r') as file:
                            content = file.readlines()
                            for line in content:
                                service, port = line.split(':')
                                user_loaded.update({service.upper(): int(port)})
                            file.close()
                        print(bold(f"\n[+++] FILE LOADED: '{file_name}' "))
                        sleep(2)
                        os.system('cls' if os.name == 'nt' else 'clear')
                    except:
                        print(bold('\n[-X-] FILE DOES NOT EXIST'))
                        sleep(1)
                        os.system('cls' if os.name == 'nt' else 'clear')
                elif choice_y == '4':
                    sleep(1)
                    os.system('cls' if os.name == 'nt' else 'clear')
            # ============================== SHOWING EXISTING PORT-DICTS!
            elif choice_x == '2':
                xx = input('[1] Default\n'
                           '[2] Used defined\n'
                           '[3] Loaded\n'
                           '[4] Go back\n'
                           '[>>>] ')
                if xx == '1':
                    for port in default_ports.items():
                        if len(str(port[1])) < 3:
                            length = 3 - len(str(port[1]))
                            space = ' '
                            delayed_print(f'SERVICE: {port[0]} || PORT: {port[1]}{length * space}\n')
                elif xx == '2':
                    if len(user_predef.items()) > 1:
                        for port in user_predef.items():
                            if len(str(port[1])) < 3:
                                length = 3 - len(str(port[1]))
                                space = ' '
                                delayed_print(f'SERVICE: {port[0]} || PORT: {port[1]}{length * space}\n')
                    else:
                        print(cs('\n[-X-] ERROR', 'red'))
                        print('[-X-] EMPTY DICT')
                        sleep(2)
                        os.system('cls' if os.name == 'nt' else 'clear')
                elif xx == '3':
                    if len(user_loaded.items()) > 1:
                        for port in user_loaded.items():
                            if len(str(port[1])) < 3:
                                length = 3 - len(str(port[1]))
                                space = ' '
                                delayed_print(f'SERVICE: {port[0]} || PORT: {port[1]}{length * space}\n')
                    else:
                        print(cs('\n[-X-] ERROR', 'red'))
                        print('[-X-] EMPTY DICT')
                        sleep(2)
                        os.system('cls' if os.name == 'nt' else 'clear')
            else:
                sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')
        else:
            break
    print(bold('\n[###] Program finished'))
    sleep(1)
    exit(0)


def scan(domain, show_ports, ports):
    import socket
    global final_text

    if len(ports.items()) > 1:
        for port in ports.items():
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            result = sock.connect_ex((domain, port[1]))
            sock.close()
            if show_ports == 'S':
                if result == 0:
                    if len(str(port[1])) < 3:
                        length = 3 - len(str(port[1]))
                        space = ' '
                        delayed_print(f'SERVICE: {port[0]} || PORT: {port[1]}{length * space}'
                                      f' || STATUS: OPEN\n')
                        final_text.append(f'SERVICE: {port[0]} || PORT: {port[1]}{length * space}'
                                          f' || STATUS: OPEN\n')
                    else:
                        delayed_print(f'SERVICE: {port[0]} || PORT: {port[1]} || STATUS: OPEN\n')
                        final_text.append(f'SERVICE: {port[0]} || PORT: {port[1]} || STATUS: OPEN\n')
                else:
                    if len(str(port[1])) < 3:
                        length = 3 - len(str(port[1]))
                        space = ' '
                        delayed_print(f'SERVICE: {port[0]} || PORT: {port[1]}{length * space}'
                                      f' || STATUS: CLOSED\n')
                        final_text.append(f'SERVICE: {port[0]} || PORT: {port[1]}{length * space}'
                                          f' || STATUS: CLOSED\n')
                    else:
                        delayed_print(f'SERVICE: {port[0]} || PORT: {port[1]} || STATUS: CLOSED\n')
                        final_text.append(f'SERVICE: {port[0]} || PORT: {port[1]} || STATUS: CLOSED\n')
            else:
                if result == 0:
                    if len(str(port[1])) < 3:
                        length = 3 - len(str(port[1]))
                        space = ' '
                        delayed_print(f'SERVICE: {port[0]} || PORT: {port[1]}{length * space}'
                                      f' || STATUS: OPEN\n')
                        final_text.append(f'SERVICE: {port[0]} || PORT: {port[1]}{length * space}'
                                          f' || STATUS: OPEN\n')
                    else:
                        delayed_print(f'SERVICE: {port[0]} || PORT: {port[1]} || STATUS: OPEN\n')
                        final_text.append(f'SERVICE: {port[0]} || PORT: {port[1]} || STATUS: OPEN\n')
    else:
        print(cs('\n[-X-] ERROR', 'red'))
        print('[-X-] EMPTY DICT')
        sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
