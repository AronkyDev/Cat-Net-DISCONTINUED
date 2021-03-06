# Created by IsTk0 ;)
#This version of Cat-Net cannot be run!

import paramiko, time, os, sys
from ping3 import ping, verbose_ping

sistema_operativo = sys.platform

def windows_administrator():
    if not pyuac.isUserAdmin():

        import win32gui, win32con
        import pyuac
        from pyuac import main_requires_admin
        import ctypes, sys, platform

        hide = win32gui.GetForegroundWindow()
        win32gui.ShowWindow(hide, win32con.SW_HIDE)
        print("Non chiudere questa finestra!")
        pyuac.runAsAdmin()

def macOS_administrator():

def linux_administrator():

print("   ____    _  _____     _   _ _____ _____ ")
print(" /  ___|  / \|_   _|   | \ | | ____|_   _|")
print(" | |     / _ \ | |_____|  \| |  _|   | |  ")
print(" | |___ / ___ \| |_____| |\  | |___  | |  ")
print(" \_____/_/   \_\_|     |_| \_|_____| |_|  ")
print("\n")

if sistema_operativo == "win32":
    windows_administrator()

if sistema_operativo == "darwin":
    macOS_administrator()

if sistema_operativo == "linux":
    linux_administrator()

def printProgressBar(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='█', printEnd="\r"):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end=printEnd)
    if iteration == total:
        print()


items = list(range(0, 57))
l = len(items)

# Qui c'è l'avanzamento ogni 0.1 secondi
printProgressBar(0, l, prefix='Caricamento:', suffix='In corso..', length=50)
for i, item in enumerate(items):
    if (i == 56):
        time.sleep(0.1)
        printProgressBar(57, l, prefix='Caricamento:', suffix='Completato', length=50)
    elif (i <= 56):
        time.sleep(0.1)
        printProgressBar(i + 1, l, prefix='Caricamento:', suffix='In corso..', length=50)


print("Benvenuto in CAT-NET V1.2.2 BETA \nDigita 'help' se hai bisogno di aiuto oppure guarda la mia repository ;)")
print("Cat Net Source code: https://github.com/IsTk0/Python-project/tree/main/Cat-Net%20project")


def ssh_code():
    print("\n")
    server = input("Hostname macchina: --> ")
    username = input("Username macchina: --> ")
    password = input("Password macchina: --> ")
    porta = input("Porta macchina: --> ")

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    ssh.connect(server, porta, username, password, allow_agent=False, look_for_keys=False)
    print("Connessione avvenuta con successo")

    while True:
        risposta = []

        comando = input("Comando macchina: --> ")

        if comando == "exit":
            ssh.close()

        ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(comando)

        for line in ssh_stdout:
            risposta.append(line.strip('\n'))
        for i in risposta:
            print(i.strip())


def ping_code():
    hostname = input("Indirizzo macchina: --> ")
    comando_ping = input("Opzione: ")
    if comando_ping == "-P":
        risposta = os.system("ping -c 1 " + hostname)
        delay = ping(hostname)
        if risposta == 0:
            print(hostname, " ha risposto in: ", "%.2g" % delay, " S")
        else:
            print(hostname, " non ha risposto")
    elif comando_ping == "-Ver":
        verbose_ping(hostname)


while True:
    comando = input("CAT-NET-> ")

    if comando == "ssh":
        ssh_code()

    elif comando == "ping":
        ping_code()

    elif comando == "help":
        print("---------- TUTTI I COMANDI ----------")
        print("     1) ssh: ")
        print("     Parametri: ")
        print("               Hostname: Il nome identificativo di un dispositivo all'interno di una rete")
        print("                        Es: computer@internet-provider.com")
        print("               Username: Il nome utente in informatica definisce il nome con il quale l'utente viene riconosciuto da un computer")
        print("                        Es: nome-utente-computer")
        print("               Password: Una password, in ambito informatico, una sequenza di caratteri alfanumerici e di simboli utilizzata per accedere in modo esclusivo a una risorsa informatica")
        print("                        Es: PasswordComputer")
        print("                  Porta: Nell'ambito delle reti di computer le porte sono lo strumento utilizzato per realizzare la multiplazione delle connessioni a livello di trasporto di dati nella rete")
        print("                        Es: 22 (porta SSH base)")
        print("     2) ping: ")
        print("     Parametri: ")
        print("               Indirizzo macchina: Può essere sia un IP o un indirizzo web")
        print("                        Es: 192.168.1.1 / sito.com")
        print("               -P: Questo valore utilizza la libreria OS per il ping a macchine")
        print("                        Es: esempio-sito.esempio")
        print("               -Ver: Questo valore utilizza la libreria Verbose_Ping per il ping a macchine")
        print("                        Es: esempio-sito.esempio")

    elif comando == "quit":
        break

    else:
        print(
            "Warning! Il comando che hai scritto non è stato riconosciuto dalla macchina o risulta inesistente, riprova.")
