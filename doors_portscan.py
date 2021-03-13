import sys
import os
from time import sleep
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

portas_padrao = {'ECHO     ': 7,
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


def delayed_print(texto):
    for letra in texto:
        sleep(0.05)
        sys.stdout.write(letra)
        sys.stdout.flush()


def adicionar_porta(portas_dict):
    run = True
    while run:
        servico_porta = input(bold('\n-------- ACRESCENTANDO PORTA --------\n') +
                              '>> Entre no formato "serviço:porta"\n'
                              '>> ')
        servico, porta = servico_porta.split(':')
        portas_dict.update({servico.upper(): int(porta)})
        print(bold(f'-------- SERVICO: {servico.upper()} || PORTA: {int(porta)} ADICIONADO --------'))
        x = input('1) Adicionar outro servico/porta\n'
                  '2) Voltar\n'
                  '>> ')
        if x == '2':
            break


def main():
    escolha = None

    while escolha != 'exit':
        print(f'\n\n{slgn}\n\n')  # Printa o slogan
        print('# Criado por Luiz Gustavo para fins de estudo, baseado na aula\n'
              '# do Afonso da Silva na comunidade TDI.\n')
        print('1 - Realizar SCAN\n'
              '2 - Configurar\n'
              '3 - Encerrar o programa')  # Menu Inicial
        escolha = input(bold('>> Entre com a sua escolha:\n>> '))
        if escolha == '1':
            dominio = input(bold('\n>> Digite o domínio:\n>> '))
            dict_scan = input(bold('\n>> Escolha um dicionário:\n') +
                              '1) Padrão\n'
                              '2) Definido pelo usuário\n'
                              '3) Carregado\n'
                              '4) Voltar \n>> ')
            if dict_scan == '1':
                dict_scan = portas_padrao
            elif dict_scan == '2':
                dict_scan = user_predef
            elif dict_scan == '3':
                dict_scan = user_loaded
            else:
                sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')
            if dict_scan in [portas_padrao, user_predef, user_loaded]:
                mostrar_portas = input(bold('\n>> Deseja mostrar portas fechadas [s/n]?\n>> ')).upper()
                print(bold('\n-------- REALIZANDO O SCAN --------'))
                scan(dominio, mostrar_portas, dict_scan)
        elif escolha == '2':
            escolha_x = input(bold('\n-------- CONFIGURAÇÃO --------\n') +
                              '1) Definir serviços/portas\n'
                              '2) Mostrar os serviços/portas\n'
                              '3) Voltar\n'
                              '>> ')
            if escolha_x == '1':
                escolha_y = input(bold('\n-------- DEFINIR PORTAS --------\n') +
                                  '1) Acrescentar ao scan padrão\n'
                                  '2) Definir um novo dict de portas\n'
                                  '3) Carregar um arquivo\n'
                                  '4) Voltar\n'
                                  '>> ')
                # ============================== ACRESCENTANDO AO DICT SCAN PADRÃO!
                if escolha_y == '1':
                    adicionar_porta(portas_padrao)
                    z = input(bold('\n-------- PORTAS CONFIGURADAS --------\n') +
                              '1) Salvar o  arquivo\n'
                              '2) Voltar ao menu\n'
                              '>> ')
                    if z == '1':
                        nome = input(bold('\n>> Entre com o nome do seu arquivo:\n') +
                                     '>> ')
                        with open(nome + '_predef.txt', 'w') as arquivo:
                            for linha in portas_padrao.items():
                                arquivo.write(f'{linha[0]}:{linha[1]}\n')
                            arquivo.close()
                        print(bold(f"\n--------- ARQUIVO SERÁ SALVO COMO: {nome + '_predef.txt'} --------"))
                        sleep(2)
                        os.system('cls' if os.name == 'nt' else 'clear')
                # ============================== CRIANDO UM DICT SCAN NOVO!
                elif escolha_y == '2':
                    adicionar_porta(user_predef)
                    nome = input(bold('\n>> Entre com o nome do seu arquivo:\n') +
                                 '>> ')
                    with open(nome + '_predef.txt', 'w') as arquivo:
                        for linha in user_predef.items():
                            arquivo.write(f'{linha[0]}:{linha[1]}\n')
                        arquivo.close()
                    print(bold(f"\n--------- ARQUIVO SERÁ SALVO COMO: {nome + '_predef.txt'} --------"))
                    sleep(2)
                    os.system('cls' if os.name == 'nt' else 'clear')
                # ============================== CARREGANDO UM DICT SCAN!
                elif escolha_y == '3':
                    nome = input(bold('\n>> Entre com o nome do seu arquivo:\n'))
                    try:
                        with open(nome, 'r') as arquivo:
                            conteudo = arquivo.readlines()
                            for linha in conteudo:
                                servico, porta = linha.split(':')
                                user_loaded.update({servico.upper(): int(porta)})
                            arquivo.close()
                        print(bold(f"\n--------- ARQUIVO '{nome}' CARREGADO --------"))
                        sleep(2)
                        os.system('cls' if os.name == 'nt' else 'clear')
                    except:
                        print(bold('\n-------- ARQUIVO NÃO EXISTE  --------'))
                        sleep(1)
                        os.system('cls' if os.name == 'nt' else 'clear')
                elif escolha_y == '4':
                    sleep(1)
                    os.system('cls' if os.name == 'nt' else 'clear')
            # ============================== MOSTRANDO OS DICT SCAN EXISTENTES!
            elif escolha_x == '2':
                xx = input('1) Padrão\n'
                           '2) Definido por usuário\n'
                           '3) Carregado\n'
                           '4) Voltar\n'
                           '>> ')
                if xx == '1':
                    for porta in portas_padrao.items():
                        if len(str(porta[1])) < 3:
                            tamanho = 3 - len(str(porta[1]))
                            espacos = ' '
                            delayed_print(f'SERVIÇO: {porta[0]} || PORTA: {porta[1]}{tamanho * espacos}\n')
                elif xx == '2':
                    if len(user_predef.items()) > 1:
                        for porta in user_predef.items():
                            if len(str(porta[1])) < 3:
                                tamanho = 3 - len(str(porta[1]))
                                espacos = ' '
                                delayed_print(f'SERVIÇO: {porta[0]} || PORTA: {porta[1]}{tamanho * espacos}\n')
                    else:
                        print(cs('\n-------- >>>> ERRO! <<<<  --------', 'red'))
                        print('-------- DICIONÁRIO VAZIO --------')
                        sleep(2)
                        os.system('cls' if os.name == 'nt' else 'clear')
                elif xx == '3':
                    if len(user_loaded.items()) > 1:
                        for porta in user_loaded.items():
                            if len(str(porta[1])) < 3:
                                tamanho = 3 - len(str(porta[1]))
                                espacos = ' '
                                delayed_print(f'SERVIÇO: {porta[0]} || PORTA: {porta[1]}{tamanho * espacos}\n')
                    else:
                        print(cs('\n-------- >>>> ERRO! <<<<  --------', 'red'))
                        print('-------- DICIONÁRIO VAZIO  --------')
                        sleep(2)
                        os.system('cls' if os.name == 'nt' else 'clear')
            else:
                sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')
        else:
            break
    print(bold('\n-------- PROGRAMA ENCERRADO  --------'))
    sleep(1)
    exit(0)


def scan(dominio, mostrar_portas, portas):
    import socket
    funcionar = False
    texto = []

    if len(portas.items()) > 1:
        funcionar = True
        for porta in portas.items():
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            resultado = sock.connect_ex((dominio, porta[1]))
            sock.close()
            if mostrar_portas == 'S':
                if resultado == 0:
                    if len(str(porta[1])) < 3:
                        tamanho = 3 - len(str(porta[1]))
                        espacos = ' '
                        delayed_print(f'SERVIÇO: {porta[0]} || PORTA: {porta[1]}{tamanho * espacos}'
                                      f' || STATUS: ABERTA\n')
                        texto.append(f'SERVIÇO: {porta[0]} || PORTA: {porta[1]}{tamanho * espacos}'
                                     f' || STATUS: ABERTA\n')
                    else:
                        delayed_print(f'SERVIÇO: {porta[0]} || PORTA: {porta[1]} || STATUS: ABERTA\n')
                        texto.append(f'SERVIÇO: {porta[0]} || PORTA: {porta[1]} || STATUS: ABERTA\n')
                else:
                    if len(str(porta[1])) < 3:
                        tamanho = 3 - len(str(porta[1]))
                        espacos = ' '
                        delayed_print(f'SERVIÇO: {porta[0]} || PORTA: {porta[1]}{tamanho * espacos}'
                                      f' || STATUS: FECHADA\n')
                        texto.append(f'SERVIÇO: {porta[0]} || PORTA: {porta[1]}{tamanho * espacos}'
                                     f' || STATUS: FECHADA\n')
                    else:
                        delayed_print(f'SERVIÇO: {porta[0]} || PORTA: {porta[1]} || STATUS: FECHADA\n')
                        texto.append(f'SERVIÇO: {porta[0]} || PORTA: {porta[1]} || STATUS: FECHADA\n')
            else:
                if resultado == 0:
                    if len(str(porta[1])) < 3:
                        tamanho = 3 - len(str(porta[1]))
                        espacos = ' '
                        delayed_print(f'SERVIÇO: {porta[0]} || PORTA: {porta[1]}{tamanho * espacos}'
                                      f' || STATUS: ABERTA\n')
                        texto.append(f'SERVIÇO: {porta[0]} || PORTA: {porta[1]}{tamanho * espacos}'
                                     f' || STATUS: ABERTA\n')
                    else:
                        delayed_print(f'SERVIÇO: {porta[0]} || PORTA: {porta[1]} || STATUS: ABERTA\n')
                        texto.append(f'SERVIÇO: {porta[0]} || PORTA: {porta[1]} || STATUS: ABERTA\n')
    else:
        print(cs('\n-------- >>>> ERRO! <<<<  --------', 'red'))
        print('-------- DICIONÁRIO VAZIO  --------')
        sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')

    if funcionar:
        x = input(cs('\n--------- SCAN CONCLUIDO --------\n', 'green').bold() +
                  '1) Salvar em arquivo (txt)\n'
                  '2) Realizar outro scan\n'
                  '3) Encerrar o programa\n'
                  '>> ')
        if x == '1':
            with open(dominio + '_scan.txt', 'w') as arquivo:
                for linha in texto:
                    arquivo.write(linha)
                arquivo.close()
            print(bold(f"\n--------- ARQUIVO SERÁ SALVO COMO: {dominio + '_scan.txt'} --------"))
            sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
        elif x == '3':
            print(bold('\n-------- PROGRAMA ENCERRADO --------'))
            sleep(1)
            exit(0)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
