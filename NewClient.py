import subprocess
import string
from random import choice
import os
import webbrowser


def gen():
    alphabet = string.ascii_letters + string.digits
    while True:
        password = ''.join(choice(alphabet) for i in range(8))
        if (any(c.islower() for c in password)
            and any(c.isupper() for c in password)
            and sum(c.isdigit() for c in password) >= 1):
            break
    return password

isnew = input('Новый клиент? (д/н) ')
users = int(input('Сколько юзеров создать? '))
client = input('Имя клиента? ')

if os.path.exists('{}'.format(client)):
    os.chdir('{}'.format(client))
else:
    os.mkdir('{}'.format(client))
    os.chdir('{}'.format(client))

if isnew.lower() == 'д':
    for i in range(1, users + 1):
        tmppass = gen()
        tmpname = client + str(i)
        command_line = 'NET USER {} {} /PASSWORDCHG:NO /ADD'.format(tmpname, tmppass)
        p = subprocess.call(command_line, shell=True)
        command_line2 = 'WMIC USERACCOUNT WHERE Name="{}" SET PasswordExpires=FALSE'.format(tmpname)
        p2 = subprocess.call(command_line2, shell=True)
        with open('result.txt', 'a') as ouf:
            print(tmpname, tmppass, file=ouf)
    webbrowser.open('result.txt')
elif isnew.lower() == 'н':
    startfrom = int(input('С какого номера начать? '))
    for i in range(startfrom, startfrom + users):
        tmppass = gen()
        tmpname = client + str(i)
        command_line = 'NET USER {} {} /PASSWORDCHG:NO /ADD'.format(tmpname, tmppass)
        p = subprocess.call(command_line, shell=True)
        command_line2 = 'WMIC USERACCOUNT WHERE Name="{}" SET PasswordExpires=FALSE'.format(tmpname)
        p2 = subprocess.call(command_line2, shell=True)
        with open('result.txt', 'a') as ouf:
            print(tmpname, tmppass, file=ouf)
    webbrowser.open('result.txt')