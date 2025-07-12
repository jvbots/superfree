import sys
import pickle, os
from time import sleep
import webbrowser
import time
import random
import string
import pyfiglet
from pyrogram import Client
import asyncio
from pyrogram.errors import FloodWait
from pyrogram.errors import PeerFlood
from pyrogram.errors import PeerIdInvalid
from pyrogram.errors import UserNotParticipant
from pyrogram.errors import UserNotMutualContact
from pyrogram.errors import UserPrivacyRestricted
from pyrogram.errors import UserNotParticipant, UserAlreadyParticipant
from pyrogram.errors import UserChannelsTooMuch
from pyrogram.errors import UserIdInvalid
from pyrogram.errors import UserKicked
from pyrogram.errors import ChatAdminRequired
from pyrogram.errors import UserBannedInChannel
from pyrogram.errors import RPCError
from pyrogram.errors import PhoneNumberUnoccupied
from pyrogram.errors import PhoneNumberInvalid
from pyrogram.errors import PhoneNumberOccupied
from pyrogram.errors import PhoneNumberBanned
from pyrogram.errors import PhoneNumberFlood
from pyrogram.errors import ApiIdInvalid
import datetime
import gender_guesser.detector as gender
from pyrogram import types
from pyrogram.raw import functions, types
from pyrogram.enums import UserStatus
from pyrogram.errors import UserDeactivated, AuthKeyUnregistered, SessionExpired, UserDeactivatedBan, SessionRevoked
from pyrogram.types import ChatEventFilter, InputPhoneContact
import time
import configparser
import csv
from csv import reader
from colorama import Fore, Back, Style, init
import colorama
colorama.init(autoreset=True)
from telethon import utils
import traceback
from licensing.models import *
from licensing.methods import Key, Helpers
import requests
from geopy.geocoders import Nominatim
from ts import messagesendergroup, messagesendergrouppic, messagesendergrouppicsingle, messagesendergroupsingle, messagesendergroupmultimsg, messagesendergroupmultimsgpic, messagesendergroupmultimsgpicmultigroups, messagesendergroupmultimsgmultigroups, messagesendermultigroupsinglepic, messagesendermultigroupsingle, forward_to_channels, forward_to_channelsnotag, multi_ccraper, messagesendering, messagesenderingpic, addtocontactbyimp, addtocontactbygroup
from faker import Faker
scam = '@notoscam'
init()

if not os.path.exists('./sessions'):
    os.mkdir('./sessions')

api_id = '23269382'
api_hash = "fe19c565fb4378bd5128885428ff8e26"

r = Fore.RED
n = Fore.RESET
lg = Fore.GREEN
rs = Fore.RESET
w = Fore.WHITE
grey = '\033[97m'
cy = Fore.CYAN
ye = Fore.YELLOW
colors = [r, lg, w, ye, cy]
info = lg + '[' + w + 'i' + lg + ']' + rs
error = lg + '[' + r + '!' + lg + ']' + rs
success = w + '[' + lg + '*' + w + ']' + rs
INPUT = lg + '[' + cy + '~' + lg + ']' + rs
plus = w + '[' + lg + '+' + w + ']' + rs
minus = w + '[' + lg + '-' + w + ']' + rs
re="\033[1;31m"
gr="\033[1;32m"
wi="\033[1;35m"

try:
    import requests
except ImportError:
    print(f'{lg}[i] Installing module - requests...{n}')
    os.system('pip install requests')

def banner():
    f = pyfiglet.Figlet(font='slant')
    logo = f.renderText('JVBOTS')
    print(random.choice(colors) + logo + rs)
    print(f'{gr}-------------- SUPER ROBÔ DE LEADS Versão FREE--------------- {re}')
    print(f'{re}------------------------------------------------------------------ {r}')
    print(f'{gr}Criado por Youtube:@jvtrader6595 & Telegram: @leadsstoreejvbots {re}')
    print(f'{re}Compre NÚMEROS de Telegram prontos para uso em: @SessoesBot_bot {r}')
    print(f'{re}------------------------------------------------------------------ {r}')

def clr():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def login():

    if not os.path.exists(f'phone.csv'):
        fp = open('phone.csv', 'x')
        fp.close()
    with open('phone.csv', mode='a', newline='') as file:
         writer = csv.writer(file)
         writer.writerow([])
         
    def remove_blank_lines(filename):
        with open(filename, 'r') as f:
            lines = f.readlines()
        with open(filename, 'w') as f:
            f.writelines(line for line in lines if line.strip())

    def remove_duplicates(lst):
        return list(set(lst))
    print()
    num_accounts = int(input(f"{gr}Digite a quantidade de contas que você deseja adicionar:{w} "))
    
    phone_numbers = []
    print()
    for i in range(num_accounts):
        phone = input(f"{gr}Digite o número de telefone da conta {i + 1}:{re} ")
        phone_numbers.append(phone)

    remove_blank_lines('phone.csv')
    with open('phone.csv', 'r') as f:
        str_lists = [row[0] for row in csv.reader(f)]
        
    phone_numbers = remove_duplicates(phone_numbers)
    
    with open('phone.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for phone in phone_numbers:
            if phone not in str_lists:
                phones = utils.parse_phone(phone)
                print(Style.BRIGHT + Fore.GREEN + f"Login {phones}")
                app = Client(f'sessions/{phones}', api_id, api_hash,phone_number=phones)
                app.start()
                app.join_chat('@The_Hacking_Zone')
                time.sleep(4.0)
                app.join_chat('@Techno_Trickop')
                app.stop()
                writer.writerow([phone])
    print()
    print(Style.BRIGHT + Fore.RESET + 'Números logados com sucesso !')
    print(Style.BRIGHT + Fore.YELLOW + 'Digite enter para sair')
    input()


def specificaccremove():

    if not os.path.exists(f'phone.csv'):
        fp = open('phone.csv', 'x')
        fp.close()
        
    def remove_blank_lines(filename):
        with open(filename, 'r') as f:
            lines = f.readlines()
        with open(filename, 'w') as f:
            f.writelines(line for line in lines if line.strip())

    def remove_duplicates(lst):
        return list(set(lst))

    def display_phone_numbers():
        with open('phone.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            phone_numbers = [row[0] for row in reader]
            for i, phone in enumerate(phone_numbers, start=1):
                print(f"{gr}{i}. {phone}")

    remove_blank_lines('phone.csv')
    print()
    print(f"{re}All Phone Numbers:")
    display_phone_numbers()
    print()
    to_remove = input(f"{Style.BRIGHT + ye}Digite o número da conta que você deseja remover:{re} ").split(',')
    to_remove = [int(num) for num in to_remove]

    with open('phone.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        phone_numbers = [row[0] for row in reader]

    removed_accounts = []
    for i in sorted(to_remove, reverse=True):  # Iterate in reverse to avoid index issues
        if i >= 1 and i <= len(phone_numbers):
           removed_accounts.append(phone_numbers.pop(i - 1))

    with open('phone.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for phone in phone_numbers:
            writer.writerow([phone])
    print()
    print(f"{re}Removed Accounts:")
    for account in removed_accounts:
        print(f"{gr}{account}")

    print(Style.BRIGHT + Fore.RESET + 'Contas removidas!')
    print()
    print(Style.BRIGHT + Fore.YELLOW + 'Digite enter para sair')
    input()

def BanFilter():

    if not os.path.exists(f'BanNumbers.csv'):
        fp = open('BanNumbers.csv', 'x')
        fp.close()
        
    MadeByHackingZone = []

    done = False
    with open('phone.csv', 'r') as f:
        str_list = [row[0] for row in csv.reader(f)]

        po = 0
        for unparsed_phone in str_list:
            po += 1

            phone = utils.parse_phone(unparsed_phone)

            print(f"{gr}Login {phone}")
            app = Client(f'sessions/{phone}', api_id, api_hash,phone_number=phone)
            # client.start(phone)
            try:
                    app.start()
                    continue

            except AuthKeyUnregistered:
                    print(f'{re}Essa sessão foi terminada')
                    HackingZone = str(po)
                    Nero_op = str(unparsed_phone)
                    MadeByHackingZone.append(Nero_op)
                    with open('BanNumbers.csv', 'w', encoding='UTF-8') as writeFile:
                         writer = csv.writer(writeFile, delimiter=",", lineterminator="\n")
                         writer.writerows(MadeByHackingZone)

            except UserDeactivatedBan:
                    print(f'{re}Essa conta está banida')
                    HackingZone = str(po)
                    Nero_op = str(unparsed_phone)
                    MadeByHackingZone.append(Nero_op)
                    with open('BanNumbers.csv', 'w', encoding='UTF-8') as writeFile:
                         writer = csv.writer(writeFile, delimiter=",", lineterminator="\n")

                         writer.writerows(MadeByHackingZone)
                         
            except SessionExpired:
                    print(f'{re}Essa sessão está expirada')
                    HackingZone = str(po)
                    Nero_op = str(unparsed_phone)
                    MadeByHackingZone.append(Nero_op)
                    with open('BanNumbers.csv', 'w', encoding='UTF-8') as writeFile:
                         writer = csv.writer(writeFile, delimiter=",", lineterminator="\n")

                         writer.writerows(MadeByHackingZone)
                         
            except SessionRevoked:
                    print(f'{re}Não foi possível autorizar a sessão para uso, porque a instância da sessão foi fechada no telegram.')
                    HackingZone = str(po)
                    Nero_op = str(unparsed_phone)
                    MadeByHackingZone.append(Nero_op)
                    with open('BanNumbers.csv', 'w', encoding='UTF-8') as writeFile:
                         writer = csv.writer(writeFile, delimiter=",", lineterminator="\n")

                         writer.writerows(MadeByHackingZone)
                         
            except UserDeactivated:
                    print(f'{re} Conta desativada ou Banida')
                    HackingZone = str(po)
                    Nero_op = str(unparsed_phone)
                    MadeByHackingZone.append(Nero_op)
                    with open('BanNumbers.csv', 'w', encoding='UTF-8') as writeFile:
                         writer = csv.writer(writeFile, delimiter=",", lineterminator="\n")

                         writer.writerows(MadeByHackingZone)

                    continue

            # client.disconnect()
        done = True
        print(f'{gr}Lista de números banidos')
        print(*MadeByHackingZone, sep='\n')
        print(f'{gr}Salvo em BanNumbers.csv')


    def autoremove():


        collection = []
        nc = []
        collection1 = []
        nc1 = []
        maind = []

        with open("phone.csv", "r") as infile:
            for line in infile:
                collection.append(line)

        for x in collection:
            mod_x = str(x).replace("\n", "")
            nc.append(mod_x)

        with open("BanNumbers.csv") as infile, open("outfile.csv", "w") as outfile:
            for line in infile:
                outfile.write(line.replace(",", ""))

        with open("outfile.csv", "r") as outfile:
            for line1 in outfile:
                rrr = line1.replace("\n", "")
                os.remove(f'sessions/{rrr}.session')
                collection1.append(line1)

        for i in collection1:
            mod_i = str(i).replace("\n", "")
            nc1.append(mod_i)

        unique = set(nc)
        unique1 = set(nc1)

        itd = unique.intersection(unique1)

        for x in nc:
            if x not in itd:
                maind.append(x)

        with open('unban.csv', 'w', encoding='UTF-8') as writeFile:
            writer = csv.writer(writeFile, lineterminator="\n")
            writer.writerows(maind)

        with open("unban.csv") as last, open("phone.csv", "w") as final:
            for line3 in last:
                mod_i = str(line3).replace("\n", "")
                final.write(mod_i)

        os.remove("phone.csv")
        os.rename("unban.csv", "phone.csv")
        print("Concluido, todos os números banidos foram removidos.")


    def dellst():
        import csv
        import os

        with open("phone.csv") as infile, open("unban.csv", "w") as outfile:
            for line in infile:
                outfile.write(line.replace(",", ""))

        os.remove("phone.csv")
        os.rename("unban.csv", "phone.csv")

        print("complete")


    autoremove()
    dellst()

    input("Done!" if done else "Error!")


def ramexadder():

    TARGET_group = input(f'{INPUT}{Style.BRIGHT + cy} Digite o USERNAME do grupo que você quer extrair os membros se for um grupo público, ou o link completo de entrada para o grupo se for um grupo privado para extrair os membros: {re}')
    my_group = str(input(f'{INPUT}{Style.BRIGHT + cy} Digite o USERNAME do grupo que você vai adicionar os membros se for publico, ou se for privado, coloque o link dele completo para adicionar membros: {re}'))
    HackingZone_dev = int(input(f'{INPUT}{Style.BRIGHT + cy} Digite o espaço em segundos entre a adição de um membro e outro.{w}[{lg}Digite 0 se não deseja por delay{wi}]: {re}'))
    maximamem = 20
    existing_members = set()
    addedchutiya = set()
    rajloda = set()
    async def rajn():
        with open('phone.csv', 'r')as f:
           str_list = [row[0] for row in csv.reader(f)]
           phone = utils.parse_phone(str_list[0])
           print(Style.BRIGHT + Fore.GREEN + f"Captando membros com {phone}")
           async with Client(f'sessions/{phone}', api_id, api_hash,phone_number=phone) as app:
                   try:
                      await app.join_chat(my_group)
                      print(f'{gr}Entrou no seu grupo')
                   except UserAlreadyParticipant:
                      time.sleep(0)
                   try:
                       my_group_entity = await app.get_chat(my_group)
                       rajloda.add(my_group_entity.id)
                   except Exception as e:
                       print('Erro ao coletar dados do usuario.', e)
                   print(f'{re} User: {Style.BRIGHT + cy}{phone}{gr} -- Verificando seu grupo para filtrar Membros')
                   async for my_group_member in app.get_chat_members(chat_id=my_group_entity.id):
                       existing_members.add(my_group_member.user.id)
    asyncio.run(rajn())
    gomuhu = str(rajloda)
    chutiya = gomuhu.strip('{}')
    lodabolo = int(chutiya)
    phone = []
    with open('phone.csv', 'r') as delta_obj:
            csv_reader = reader(delta_obj)
            list_of_phone = tuple(csv_reader)
            for phone_ in list_of_phone:
                phone.append(int(phone_[0]))
            pphone = phone

    print(f'{gr}Total de contas: {n} {r}{str(len(phone))}{n}')
    
    stacno = 1
    endacno = 5000000
    
    From = int(stacno) - 1
    Upto = int(endacno)
    
    async def mainn():
        indexx = 0
        a = 0
        for xd in pphone[From:Upto]:
            indexx += 1
            phone = utils.parse_phone(xd)
            async with Client(f'sessions/{phone}', api_id, api_hash,phone_number=phone) as app:
                print(f'{re} User: {Style.BRIGHT + cy}{phone}{gr} -- {cy}Iniciando session... ')
                try:
                   await app.join_chat(TARGET_group)
                   print(f'{re} User: {Style.BRIGHT + cy}{phone}{gr} -- Entrou no grupo para Extrair')
                except UserAlreadyParticipant:
                   time.sleep(0)
                try:
                   await app.join_chat(my_group)
                except UserAlreadyParticipant:
                   time.sleep(0)
                try:
                    target_group_entity = await app.get_chat(TARGET_group)
                except Exception as e:
                    print('Erro ao coletar dados do usuario.:', e)
                    return
                
                nu = 1
                stop = 0
                flood = 0
                added = 0
                peer = 0
                userbanned = 0
                
                print(f'{re} User: {Style.BRIGHT + cy}{phone}{gr} -- Extraindo do grupo fonte')
                async for target_member in app.get_chat_members(chat_id=target_group_entity.id):
                    if target_member.user.id not in existing_members and target_member.user.id not in addedchutiya:
                        user_id = target_member.user.id
                        first_name = target_member.user.first_name or ''
                        last_name = target_member.user.last_name or ''
                        username = target_member.user.username or ''
                        
                        if stop == maximamem:
                            print(f'{re}Foi adicionado {maximamem} membros, finalizando')
                            break

                        if flood == 5:
                            print(f'{re}Finalizando por erros de Flood')
                            print('Total de membros adicionados ===', added)
                            break

                        if peer == 5:
                            print(f'{re}Finalizando por erros de Peer Flood')
                            print('Total de membros adicionados ===', added)
                            break

                        if userbanned == 5:
                            print(f'{re}Finalizando por erros de Banimento')
                            print('Total de membros adicionados ===', added)
                            break

                        user_idd = await app.resolve_peer(int(user_id))
                        addedchutiya.add(user_id)
                        try:
                            access_hash = user_idd.access_hash
                            await app.add_chat_members(lodabolo, user_idd.user_id, access_hash)
                            #print("user added", str(first_name), str(last_name))
                            raj = str(first_name)
                            print(f'{re} User: {Style.BRIGHT + cy}{phone}{gr} -- {Style.BRIGHT + cy}{raj} {gr}--> {Style.BRIGHT + cy}{my_group}')
                            stop = stop + 1
                            added = added + 1
                            time.sleep(HackingZone_dev)
                            
                        except UserPrivacyRestricted as e:
                            await asyncio.sleep(random.randint(2,3))
                            
                        except UserChannelsTooMuch as e:
                            await asyncio.sleep(0)
                            
                        except PeerFlood as e:
                            print(f'{re}Erro de Peer Flood na sua conta - Dê descanso a essa conta.', nu)
                            await asyncio.sleep(random.randint(2,5))
                            nu = nu + 1
                            peer = peer + 1

                        except UserBannedInChannel as e:
                            print(f'{re}Essa conta foi banida ou teve banimento de serviço durante a adição - A remova do script depois.', nu)
                            await asyncio.sleep(random.randint(2,5))
                            nu = nu + 1
                            userbanned = userbanned + 1

                        except FloodWait as e:
                            print(f'{gr}Detectando erro de flood, esperando um pouco{re} {e.value}', nu)
                            await asyncio.sleep(random.randint(2,5))
                            nu = nu + 1
                            flood = flood + 1

                        except RPCError as e:
                             status = e.__class__.__name__
                             print(f'{status}')
                            
        a += 1
    asyncio.run(mainn())


def changeraccount():

    print(f'{gr}Envie o primeiro nome da conta:  ')
    firstname = str(input())
    print(f'{gr}Envie o ultimo nome da conta:  ')
    lastname = str(input())
    print(f'{gr}envie o texto da bio:  ')
    bio = str(input())
    print(f'{gr}Digite o tempo de espera para fazer as alterações entre uma conta e outra: ')
    HackingZone_dev = int(input())
    with open('phone.csv', 'r')as f:
        str_list = [row[0] for row in csv.reader(f)]
        po = 0
        for pphone in str_list:
            phone = utils.parse_phone(pphone)
            po += 1
            print(Style.BRIGHT + Fore.GREEN + f"Using {phone}")
            app = Client(f'sessions/{phone}', api_id, api_hash,phone_number=phone)
            app.start()
            app.update_profile(first_name=firstname, last_name=lastname, bio=bio)
            print(f'{wi}Sucesso, informações atualizadas com {phone}')
            app.stop()
            time.sleep(HackingZone_dev)
            print()
        done = True
    print(Style.BRIGHT + Fore.RESET + 'Sucesso, tarefa concluida !' if done else "Error!")
    print(Style.BRIGHT + Fore.YELLOW + 'Digite enter para sair')
    input()

def changerusername():

     def send_usernames_from_csv(phone_csv_path, usernames_csv_path):
          with open(phone_csv_path, 'r') as phone_file, open(usernames_csv_path, 'r') as usernames_file:
              phone_reader = csv.reader(phone_file)
              usernames_reader = csv.reader(usernames_file)
        
              phone_rows = list(phone_reader)
              usernames_rows = list(usernames_reader)

              if len(phone_rows) != len(usernames_rows):
                  print("Error: The number of rows in 'phone.csv' and 'username.csv' is not equal.")
                  return

              for phone_row, usernames_row in zip(phone_rows, usernames_rows):
                  phone_number = utils.parse_phone(phone_row[0])
                  username = usernames_row[0]

                  print(Style.BRIGHT + Fore.GREEN + f"Mudando username da conta {phone_number}")
                  app = Client(f'sessions/{phone_number}', api_id, api_hash,phone_number=phone_number)
                  app.start()

                  time.sleep(0)
                  

                  try:
                     app.set_username(username)
                  except Exception as e:
                      print(f"Error na clonagem: {str(e)}")

                  app.stop()
                  print()

          print(Style.BRIGHT + Fore.RESET + 'Tarefa de usernames completa!')

     send_usernames_from_csv('phone.csv', 'username.csv')

def twostepverification():

    print('Digite qual a senha de autenticação de segundo fator você deseja inserir:  ')
    usernamehh = str(input())
    print('Digite o tempo entre a adição em uma conta e em outra: ')
    Rocky_200_dev = int(input())
    with open('phone.csv', 'r')as f:
        str_list = [row[0] for row in csv.reader(f)]
        po = 0
        for pphone in str_list:
            phone = utils.parse_phone(pphone)
            po += 1
            print(Style.BRIGHT + Fore.GREEN + f"Login {phone}")
            app = Client(f'sessions/{phone}', api_id, api_hash,phone_number=phone)
            try:
               app.start()
               app.enable_cloud_password(usernamehh)
               print('Senha colocada com sucesso')
               app.stop()
            except Exception as e:
               #print('error',e)
               try:
                  print("Essa conta já tem uma senha, por favor, digite essa senha para que possamos fazer a modificação da senha depois: ")
                  rss = str(input())
                  app.remove_cloud_password(rss)
                  app.enable_cloud_password(usernamehh)
                  print('senha configurada com sucesso')
               except Exception as e:
                  print('error',e)
            time.sleep(Rocky_200_dev)
            print()
        done = True
    print(Style.BRIGHT + Fore.RESET + 'Sucesso, tarefa finalizada !' if done else "Error!")
    print(Style.BRIGHT + Fore.YELLOW + 'Digite enter para sair')
    input()

def ScamTag():

    msg = str(input(f'{gr}Digite a mensagem para reportar: {re}'))
    print(f'{gr}Digite o delay entre uma mensagem e outra: {re}')
    HackingZone_dev = int(input())
    with open('phone.csv', 'r')as f:
        str_list = [row[0] for row in csv.reader(f)]
        po = 0
        for pphone in str_list:
            phone = utils.parse_phone(pphone)
            po += 1
            print(Style.BRIGHT + Fore.GREEN + f"Using {phone}")
            app = Client(f'sessions/{phone}', api_id, api_hash,phone_number=phone)
            try:
               app.start()
               app.send_message(scam,msg)
               print(f'{wi}Successfull Report from {phone}')
            except Exception as e:
                print('Failed to Send Report:', e)
                time.sleep(0)
            app.stop()
            time.sleep(HackingZone_dev)
            print()
        done = True
    print(Style.BRIGHT + Fore.RESET + 'All Number Login Done !' if done else "Error!")
    print(Style.BRIGHT + Fore.YELLOW + 'Press Enter to back')
    input()


def ramexsender():

    TARGET_group = input(f'{INPUT}{Style.BRIGHT + cy} Digite o USERNAME do grupo que você quer extrair os membros se for um grupo público, ou o link completo de entrada para o grupo se for um grupo privado para extrair os membros: {re}')
    msg = str(input(f'{gr}Digite a mensagem que você deseja enviar: {re}'))
    HackingZone_dev = int(input(f'{INPUT}{Style.BRIGHT + cy} Digite o tempo de espera para o envio entre uma mensagem e outra.{w}[{lg}0 se não quiser tempo de espera{wi}]: {re}'))
    maximamem = 7
    addedchutiya = set()
    phone = []
    with open('phone.csv', 'r') as delta_obj:
            csv_reader = reader(delta_obj)
            list_of_phone = tuple(csv_reader)
            for phone_ in list_of_phone:
                phone.append(int(phone_[0]))
            pphone = phone

    print(f'{gr}Total de contas: {n} {r}{str(len(phone))}{n}')
    
    stacno = 1
    endacno = 5000000
    
    From = int(stacno) - 1
    Upto = int(endacno)
    
    async def mainn():
        indexx = 0
        a = 0
        for xd in pphone[From:Upto]:
            indexx += 1
            phone = utils.parse_phone(xd)
            async with Client(f'sessions/{phone}', api_id, api_hash,phone_number=phone) as app:
                print(f'{re} User: {Style.BRIGHT + cy}{phone}{gr} -- {cy}iniciando session... ')
                try:
                   await app.join_chat(TARGET_group)
                   print(f'{re} User: {Style.BRIGHT + cy}{phone}{gr} -- Entrou no grupo para Extrair')
                except UserAlreadyParticipant:
                   time.sleep(0)
                try:
                    target_group_entity = await app.get_chat(TARGET_group)
                except Exception as e:
                    print('Erro ao coletar dados do usuario.:', e)
                    return
                
                nu = 1
                stop = 0
                flood = 0
                added = 0
                peer = 0
                userbanned = 0
                
                print(f'{re} User: {Style.BRIGHT + cy}{phone}{gr} -- Extraindo do grupo fonte')
                async for target_member in app.get_chat_members(chat_id=target_group_entity.id):
                    if target_member.user.id not in addedchutiya:
                        user_id = target_member.user.id
                        first_name = target_member.user.first_name or ''
                        last_name = target_member.user.last_name or ''
                        username = target_member.user.username or ''
                        
                        if stop == maximamem:
                            print(f'{re}Enviou {maximamem} membros, finalizando')
                            break

                        if flood == 5:
                            print(f'{re}Finalizando por erros de Flood')
                            print('Total de membros contatados ===', added)
                            break

                        if peer == 5:
                            print(f'{re}Finalizando por erros de Peer Flood')
                            print('Total de membros contatados ===', added)
                            break

                        if userbanned == 5:
                            print(f'{re}Finalizando por erros de Banimento')
                            print('Total de membros contatados ===', added)
                            break

                        user_idd = int(user_id)
                        addedchutiya.add(user_id)
                        try:
                            #await app.add_chat_members(lodabolo, user_idd.user_id, access_hash)
                            await app.send_message(user_idd,msg)
                            print(f"{gr}Message enviada para", f'{wi}{str(first_name)} {str(last_name)}')
                            stop = stop + 1
                            added = added + 1
                            time.sleep(HackingZone_dev)
                            
                        except UserPrivacyRestricted as e:
                            await asyncio.sleep(random.randint(2,3))
                            
                        except UserChannelsTooMuch as e:
                            await asyncio.sleep(0)
                            
                        except PeerFlood as e:
                            print(f'{re}Erro de Peer Flood na sua conta - Dê descanso a essa conta.', nu)
                            await asyncio.sleep(random.randint(2,5))
                            nu = nu + 1
                            peer = peer + 1

                        except UserBannedInChannel as e:
                            print(f'{re}Essa conta foi banida ou teve banimento de serviço durante a adição - A remova do script depois.', nu)
                            await asyncio.sleep(random.randint(2,5))
                            nu = nu + 1
                            userbanned = userbanned + 1

                        except FloodWait as e:
                            print(f'{gr} Detectando erro de flood, esperando um pouco{re} {e.value}', nu)
                            await asyncio.sleep(random.randint(2,5))
                            nu = nu + 1
                            flood = flood + 1

                        except RPCError as e:
                             status = e.__class__.__name__
                             print(f'{status}')
                            
        a += 1
    asyncio.run(mainn())



def checknumb():

    HackingZone_devinput = int(1)
    with open('phone.csv', 'r') as read_obj:
        csv_reader = reader(read_obj)
        list_of_rows = list(csv_reader)
        row_number = HackingZone_devinput
        col_number = 1
        value = list_of_rows[row_number - 1][col_number - 1]
        
    phonee = value
    if phonee:
            phone = utils.parse_phone(phonee)
            print(Style.BRIGHT + Fore.GREEN + f"Login {phone}")
            app = Client(f'sessions/{phone}', api_id, api_hash,phone_number=phone)
            app.start()
            try:
               if os.path.exists(f'filternumbers.csv'):
                  os.remove(f'filternumbers.csv')
               with open('numbers.csv', 'r', encoding='utf-8')as f:
                  str_list = [row[0] for row in csv.reader(f)]
                  po = 0
                  for numb in str_list:
                      lund = utils.parse_phone(numb)
                      po += 1
                      time.sleep(3)
                      print(Style.BRIGHT + Fore.BLUE + f"Checking {lund}")
                      try:
                          userinfo = app.invoke(functions.contacts.ResolvePhone(phone=f'{lund}'))
                          print(userinfo)
                          print(userinfo.users)
                          for user in userinfo.users:
                              print(user.id)
                              user_id = user.id
                              user_idd = app.resolve_peer(int(user_id))
                              access_hash = user_idd.access_hash
                              #app.add_chat_members("justtestog", user_idd.user_id, access_hash)
                              
                          print(Style.BRIGHT + Fore.YELLOW + 'Number Valid')
                          with open('filternumbers.csv', 'a', newline='', encoding='utf-8') as filter_file:
                            writer = csv.writer(filter_file)
                            writer.writerow([numb])
                      except PhoneNumberUnoccupied:
                          print("This Number is Not Occupied by Anyone")
                      except PhoneNumberInvalid:
                          print("numero de telefone invalido")
                      except PhoneNumberBanned:
                          print("numero de telefone banido")
                      except PhoneNumberOccupied:
                          print("numero ocupado")
                      except PhoneNumberFlood:
                          print("numero com flood")
                      except Exception as e:
                          print(e)
                      print()
            except Exception as e:
                print(e)
            app.stop()
    else:
       print("no phone")
    print(Style.BRIGHT + Fore.YELLOW + 'Check Done saved in filternumbers.csv')


def logintypetwo():
    if os.stat('api.csv').st_size == 0:
        print("--------------------------------------------")
        print("api.csv is empty. Cannot proceed with login.")
        print("--------------------------------------------")
        return
    if os.stat('devicelist.csv').st_size == 0:
        print("--------------------------------------------")
        print("devicelist.csv is empty. Cannot proceed with login.")
        print("--------------------------------------------")
        return
    delaybolte = int(input(f"{gr}Enter Delay Per Second You Want To Use: {re}"))
    with open('api.csv', 'r', encoding='utf-8') as f:
        Apiis = csv.reader(f)
        api = [i for i in Apiis]

    with open('devicelist.csv', 'r', encoding='utf-8') as f:
        devicee = csv.reader(f)
        device = [i for i in devicee]

    with open('phone.csv', 'r') as f:
        str_list = [row[0] for row in csv.reader(f)]
        total_phones = len(str_list)
        po = 0
        capi = 0
        dovi = 0
        for pphone in str_list:
            phone = utils.parse_phone(pphone)
            po += 1
            print(f"API ID: {gr}{api[capi][0]}, API Hash: {cy}{api[capi][1]}, Device Name: {re}{device[dovi][0]}")
            print(Style.BRIGHT + Fore.GREEN + f"{cy}Login {gr}{phone} ({po}/{total_phones})")
            app = Client(f"sessions/{phone}", api_id=int(api[capi][0]), api_hash=api[capi][1], phone_number=phone, device_model=device[dovi][0])
            app.start()
            app.join_chat('@digitaljvbots2')
            time.sleep(delaybolte)
            app.join_chat('@JVBOTSFREE')
            app.stop()
            capi += 1
            dovi += 1
            print()
        done = True
    print(Style.BRIGHT + Fore.RESET + 'All Number Login Done !' if done else "Error!")
    print(Style.BRIGHT + Fore.YELLOW + 'Press Enter to back')
    input() 


def logintypeone():

    if os.stat('api.csv').st_size == 0:
        print("--------------------------------------------")
        print("api.csv is empty. Cannot proceed with login.")
        print("--------------------------------------------")
        return
    if os.stat('devicelist.csv').st_size == 0:
        print("--------------------------------------------")
        print("devicelist.csv is empty. Cannot proceed with login.")
        print("--------------------------------------------")
        return
    delaybolte = int(input(f"{gr}Enter Delay Per Second You Want To Use: {re}"))
    with open('api.csv', 'r', encoding='utf-8') as f:
        Apiis = csv.reader(f)
        api = [i for i in Apiis]

    with open('devicelist.csv', 'r', encoding='utf-8') as f:
        devicee = csv.reader(f)
        device = [i for i in devicee]

    if not os.path.exists(f'phone.csv'):
        fp = open('phone.csv', 'x')
        fp.close()
    with open('phone.csv', mode='a', newline='') as file:
         writer = csv.writer(file)
         writer.writerow([])
         
    def remove_blank_lines(filename):
        with open(filename, 'r') as f:
            lines = f.readlines()
        with open(filename, 'w') as f:
            f.writelines(line for line in lines if line.strip())

    def remove_duplicates(lst):
        return list(set(lst))
    print()
    num_accounts = int(input(f"{gr}Enter the number of accounts you want to add:{w} "))
    
    phone_numbers = []
    print()
    for i in range(num_accounts):
        phone = input(f"{gr}Enter phone number for account {i + 1}:{re} ")
        phone_numbers.append(phone)

    remove_blank_lines('phone.csv')
    with open('phone.csv', 'r') as f:
        str_lists = [row[0] for row in csv.reader(f)]
        
    phone_numbers = remove_duplicates(phone_numbers)
    
    with open('phone.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        dovi = 0
        capi = 0
        for phone in phone_numbers:
            if phone not in str_lists:
                phones = utils.parse_phone(phone)
                print(f"API ID: {gr}{api[capi][0]}, API Hash: {cy}{api[capi][1]}, Device Name: {re}{device[dovi][0]}")
                print(Style.BRIGHT + Fore.GREEN + f"{cy}Login {gr}{phone}")
                app = Client(f"sessions/{phones}", api_id=int(api[capi][0]), api_hash=api[capi][1], phone_number=phones, device_model=device[dovi][0])
                app.start()
                app.join_chat('@digitaljvbots2')
                time.sleep(delaybolte)
                app.join_chat('@JVBOTSFREE')
                app.stop()
                dovi += 1
                capi += 1
                writer.writerow([phone])
    print()
    print(Style.BRIGHT + Fore.RESET + 'All Number Login Done !')
    print(Style.BRIGHT + Fore.YELLOW + 'Press Enter to Exit')
    input()


def csvblankremover():

    if not os.path.exists(f'phone.csv'):
        fp = open('phone.csv', 'x')
        fp.close()
    with open('phone.csv', mode='a', newline='') as file:
         writer = csv.writer(file)
         writer.writerow([])
         
    def remove_blank_lines(filename):
        with open(filename, 'r') as f:
            lines = f.readlines()
        with open(filename, 'w') as f:
            f.writelines(line for line in lines if line.strip())

    remove_blank_lines('phone.csv')
    print(f"{gr}Extra Line Removed Successfully")



def accountinfogetter():

    with open('phone.csv', 'r')as f:
        str_list = [row[0] for row in csv.reader(f)]
        po = 0
        for pphone in str_list:
            phone = utils.parse_phone(pphone)
            po += 1
            print(Style.BRIGHT + Fore.GREEN + f"Login {phone}")
            app = Client(f'sessions/{phone}', api_id, api_hash,phone_number=phone)
            app.start()
            me = app.get_me()
            print(f"{re}-------------- {gr}Account Info {re}--------------")
            print(f'{re}ID: {gr}{me.id}')
            print(f'{re}Self: {gr}{me.is_self}')
            print(f'{re}Contact: {gr}{me.is_contact}')
            print(f'{re}Mutual Contact: {gr}{me.is_mutual_contact}')
            print(f'{re}Deleted: {gr}{me.is_deleted}')
            print(f'{re}Verified: {gr}{me.is_verified}')
            print(f'{re}Scam: {gr}{me.is_scam}')
            print(f'{re}Fake: {gr}{me.is_fake}')
            print(f'{re}Support: {gr}{me.is_support}')
            print(f'{re}Premium: {gr}{me.is_premium}')
            print(f'{re}First Name: {gr}{me.first_name}')
            print(f'{re}Last Name: {gr}{me.last_name if me.last_name else None}')
            print(f'{re}Status: {gr}{me.status}')
            print(f'{re}Last Online Date: {gr}{me.last_online_date}')
            print(f'{re}Phone Number: {gr}{phone}')
            app.stop()
            print()
        done = True
    print(Style.BRIGHT + Fore.RESET + 'All Number Info Done !' if done else "Error!")
    print(Style.BRIGHT + Fore.YELLOW + 'Press Enter to back')
    input()

def limicheckandrem():
    textfor = '''First, please confirm that you will never send this to strangers:
- Unsolicited advertising of any kind
- Promotional messages
- Shocking materials
Were you going to do anything like that?'''
    
    url = 'https://pastebin.com/raw/YKbeUazQ' # url of paste
    r = requests.get(url) # response will be stored from url
    content = r.text
    with open('phone.csv', 'r')as f:
        str_list = [row[0] for row in csv.reader(f)]
        po = 0
        for pphone in str_list:
            phone = utils.parse_phone(pphone)
            po += 1
            print(Style.BRIGHT + Fore.GREEN + f"Login {phone}")
            app = Client(f'sessions/{phone}', api_id, api_hash,phone_number=phone)
            app.start()
            raj = app.get_me()
            textly = f'''Hello {raj.first_name}!

I’m very sorry that you had to contact me. Unfortunately, some actions can trigger a harsh response from our anti-spam systems. If you think your account was limited by mistake, you can submit a complaint to our moderators.

While the account is limited, you will not be able to send messages to people who do not have your number in their phone contacts or add them to groups and channels. Of course, when people contact you first, you can always reply to them.'''
            input_peer = "spambot"
            app.send_message(input_peer, "/start")
            time.sleep(0.5)
            for message in app.get_chat_history(input_peer, limit=1):
                print(f"{re}Bot Message: {gr}{message.text}")
            if message.text == 'Good news, no limits are currently applied to your account. You’re free as a bird!':
                app.send_message(input_peer, "Cool, thanks")
                print(f"{re}User Message: {gr}Cool, thanks")
                time.sleep(1)
                for messagee in app.get_chat_history(input_peer, limit=1):
                    print(f"{re}Bot Message: {gr}{messagee.text}")
                    print()
                    print(f"{Style.BRIGHT + ye}Conclusion: {re}não há limitações nessa conta")
            elif message.text == 'Unfortunately, some phone numbers may trigger a harsh response from our anti-spam systems. If you think this is the case with you, you can submit a complaint to our moderators or subscribe to Telegram Premium to get less strict limits.':
                print(f"{Style.BRIGHT + ye}Review: {gr}No Limit on Account, It will cause no Problem but it can be fixed. So trying...")
                app.send_message(input_peer, "Submit a complaint")
                print(f"{re}User Message: {gr}Submit a complaint")
                time.sleep(1)
                for messagee in app.get_chat_history(input_peer, limit=1):
                    print(f"{re}Bot Message: {gr}{messagee.text}")
                    print()
                if messagee.text == textfor:
                    app.send_message(input_peer, "No, I’ll never do any of this!")
                    print(f"{re}User Message: {gr}No, I’ll never do any of this!")
                    time.sleep(1)
                    for messageee in app.get_chat_history(input_peer, limit=1):
                        print(f"{re}Bot Message: {gr}{messageee.text}")
                        print()
                        app.send_message(input_peer, content)
                        print(f"{re}User Message: {gr}{content}")
                        time.sleep(1)
                        for messageeee in app.get_chat_history(input_peer, limit=1):
                            print(f"{re}Bot Message: {gr}{messageeee.text}")
                            print()
                            print(f"{Style.BRIGHT + ye}Conclusion: {re}Não há limitação nessa conta, mas há uma limitação para envio de mensagens ou adição de membros, enviamos uma mensagem ao telegram para tentar corrigir isso, recomendamos tentar novamente depois.")
                elif messagee.text == "You've already submitted a complaint recently. Our team’s supervisors will check it as soon as possible. Thank you for your patience.":
                        print(f"{Style.BRIGHT + ye}Conclusion: {re}Não há limitação nessa conta, mas há uma limitação para envio de mensagens ou adição de membros, enviamos uma mensagem ao telegram para tentar corrigir isso, recomendamos tentar novamente depois.")
            elif message.text == textly:
                print(f"{Style.BRIGHT + ye}Review: {gr}Account Limited, Let's try to fix this.")
                app.send_message(input_peer, "This is a mistake")
                print(f"{re}User Message: {gr}This is a mistake")
                time.sleep(1)
                for messagee in app.get_chat_history(input_peer, limit=1):
                    print(f"{re}Bot Message: {gr}{messagee.text}")
                    print()
                if messagee.text == 'If you think the limitations on your account were applied by mistake, you can submit a complaint. All complaints will be reviewed by the team’s supervisor. Please note that this will have no effect on limitations that were applied with a good reason. Would you like to submit a complaint?':
                    app.send_message(input_peer, "Yes")
                    print(f"{re}User Message: {gr}Yes")
                    time.sleep(1)
                    for messageee in app.get_chat_history(input_peer, limit=1):
                        print(f"{re}Bot Message: {gr}{messageee.text}")
                        print()
                        app.send_message(input_peer, "No! Never did that!")
                        print(f"{re}User Message: {gr}No! Never did that!")
                        for messageeee in app.get_chat_history(input_peer, limit=1):
                            print(f"{re}Bot Message: {gr}{messageeee.text}")
                            print()
                            app.send_message(input_peer, content)
                            print(f"{re}User Message: {gr}{content}")
                            time.sleep(1)
                            for messageeeee in app.get_chat_history(input_peer, limit=1):
                                print(f"{re}Bot Message: {gr}{messageeeee.text}")
                                print()
                                print(f"{Style.BRIGHT + ye}Conclusion: {re}a conta está limitada, enviamos mensagem para o spambot para tentar corrigir isso, aguarde e tente novamente depois.")
                elif messagee.text == "You've already submitted a complaint recently. Our team’s supervisors will check it as soon as possible. Thank you for your patience.":
                        print(f"{Style.BRIGHT + ye}Conclusion: {re}Conta ainda limitada, aguarde.")
            else:
                print(f"{wi}Conta com limitações severas.")
            app.stop()
            print()
        done = True
    print(Style.BRIGHT + Fore.RESET + 'tarefa finalizada' if done else "Error!")
    print(Style.BRIGHT + Fore.YELLOW + 'digite enter para sair')
    input()



def main_menu():
    clr()
    banner()
    print(Style.BRIGHT + ye+'      Selecione uma opção:'+n)
    print(Style.BRIGHT + Fore.CYAN+'   [1] Adicionar novas contas de Telegram'+n)
    print(Style.BRIGHT + Fore.CYAN+'   [2] Filtrar por contas banidas'+n)
    print(Style.BRIGHT + Fore.CYAN+'   [3] Remover uma conta do Robô'+n)
    print(Style.BRIGHT + Fore.CYAN+'   [4] Se inscreva no canal para estar atento as novidades'+n)
    print(Style.BRIGHT + Fore.CYAN+f'   [5] Adição de membros simples {re}(Grupos publicos e privados)'+n)
    print(Style.BRIGHT + Fore.CYAN+'   [11] COMPRE Números de Telegram Prontos para adicionar Membros Aquí!'+n)
    print(Style.BRIGHT + Fore.CYAN+'   [12] COMPRE Membros Fake para fazer Volume no seu grupo do Telegram Aquí!'+n)
    print(' '+Style.BRIGHT + Fore.GREEN + Back.RED+'[27] Compre Membros para INSTAGRAM, LIKES e VIEWS'+n)
    print(Style.BRIGHT + ye+'      Exit:'+n)
    print(Style.BRIGHT + Fore.CYAN+'   [0]  sair'+n)
    a = int(input('\nDigite sua escolha: '))
    if a == 1:
        login()
    elif a == 2:
        BanFilter()
    elif a == 3:
        specificaccremove()
    elif a == 4:
        url = 'https://www.youtube.com/@jvtrader6595?sub_confirmation=1'
        webbrowser.open(url)
        print('Para selecionar mais opções, abra o script novamente', url)
    elif a == 5:
        ramexadder()
    elif a == 6:
        hiddenadder()
    elif a == 7:
        ramexdaily()
    elif a == 27:
        ramexsender()
    elif a == 9:
        ramexmonthly()
    elif a == 10:
        ramexonline()
    elif a == 11:
        url = 'https://api.whatsapp.com/send?phone=5584998493595'
        webbrowser.open(url)
        print('Para selecionar mais opções, abra o script novamente', url)
    elif a == 12:
        url = 'https://www.leadsstore.me'
        webbrowser.open(url)
        print('Para selecionar mais opções, abra o script novamente', url)
    elif a == 13:
        reactionincreaser()
    elif a == 14:
        sharesincreaser()
    elif a == 15:
        changeraccount()
    elif a == 16:
        changerusername()
    elif a == 17:
        twostepverification()
    elif a == 18:
        ScamTag()
    elif a == 19:
        ramexsender()
    elif a == 20:
        setprofilepic()
    elif a == 21:
        removeprofilepic()
    elif a == 22:
        reportspamuser()
    elif a == 23:
        pmspamdm()
    elif a == 24:
        groupjoiner()
    elif a == 25:
        grouplefter()
    elif a == 26:
        loginbycsv()
    elif a == 27:
        url = 'https://www.leadsstore.me'
        webbrowser.open(url)
        print('Para selecionar mais opções, abra o script novamente', url)
    elif a == 28:
        opthree()
    elif a == 29:
        vcffiled()
    elif a == 30:
        loginusingsecurity()
    elif a == 31:
        tsender()
    elif a == 32:
        addusinggendert()
    elif a == 33:
        url = 'https://www.leadsstore.me'
        webbrowser.open(url)
        print('Para selecionar mais opções, abra o script novamente', url)
    elif a == 34:
        viewsincrement()
    elif a == 35:
        autogroupmaker()
    elif a == 36:
        groupchatcloner()
    elif a == 37:
        limicheckandrem()
    elif a == 38:
        accountinfogetter()
    elif a == 0:
        exit()
        

    clr()
    banner()
    print()
    print(f'{Style.BRIGHT + Fore.YELLOW + Back.RED}[+] De qual pais você deseja adicionar membros?:'+n)
    print(f'{Style.BRIGHT + Fore.CYAN}[1] India'+n)
    print(f'{Style.BRIGHT + Fore.CYAN}[2] USA'+n)
    print(f'{Style.BRIGHT + Fore.CYAN}[3] Bangladesh'+n)
    print(f'{Style.BRIGHT + Fore.CYAN}[4] Russia'+n)
    print(f'{Style.BRIGHT + Fore.CYAN}[5] Ukraine'+n)
    print(f'{Style.BRIGHT + Fore.CYAN}[6] Pakistan or Iran'+n)
    print(f'{Style.BRIGHT + Fore.CYAN}[7] Bhutan or China'+n)
    print(f'{Style.BRIGHT + Fore.CYAN}[8] UK'+n)
    print(f'{Style.BRIGHT + Fore.CYAN}[9] Japan'+n)
    print(f'{Style.BRIGHT + Fore.CYAN}[10] Germany'+n)
    print(f'{Style.BRIGHT + Fore.CYAN}[11] Switzerland'+n)
    print(f'{Style.BRIGHT + Fore.CYAN}[12] Brazil'+n)
    print(f'{Style.BRIGHT + Fore.CYAN}[13] Indonesia'+n)
    print(f'{Style.BRIGHT + Fore.CYAN}[14] Uzbekistan'+n)
    print(f'{Style.BRIGHT + Fore.CYAN}[15] Belgium'+n)
    print(f'{Style.BRIGHT + Fore.CYAN}[16] Cambodia or ThaiLand'+n)
    print(f'{Style.BRIGHT + Fore.CYAN}[17] Ethiopia'+n)
    print(f'{Style.BRIGHT + Fore.CYAN}[18] Nigeria'+n)
    print(f'{Style.BRIGHT + Fore.CYAN}[19] Turkey'+n)
    print(f'{Style.BRIGHT + Fore.CYAN}[20] Israel'+n)
    print()
    print(f'{Style.BRIGHT + Fore.YELLOW + Back.RED}[+] Exit Option:'+n)
    print(f'{Style.BRIGHT + Fore.CYAN}[0] voltar'+n)
    print(f'{Style.BRIGHT + Fore.CYAN}[21] sair'+n)
    c = int(input('\nDigite sua escolha: '))
    if c == 1:
        nearbyadderautoindia()
    elif c == 2:
        nearbyadderautousa()
    elif c == 3:
        nearbyadderautobangladesh()
    elif c == 4:
        nearbyadderautorussia()
    elif c == 5:
        nearbyadderautoukraine()
    elif c == 6:
        nearbyadderautopakistan()
    elif c == 7:
        nearbyadderautobhutan()
    elif c == 8:
        nearbyadderautouk()
    elif c == 9:
        nearbyadderautojapan()
    elif c == 10:
        nearbyadderautogermany()
    elif c == 11:
        nearbyadderautoswitzerland()
    elif c == 12:
        nearbyadderautobrazil()
    elif c == 13:
        nearbyadderautoindonesia()
    elif c == 14:
        nearbyadderautouzbekistan()
    elif c == 15:
        nearbyadderautobelgium()
    elif c == 16:
        nearbyadderautocombodia()
    elif c == 17:
        nearbyadderautoethiopia()
    elif c == 18:
        nearbyadderautonigera()
    elif c == 19:
        nearbyadderautoturkey()
    elif c == 20:
        nearbyadderautoisrael()
    elif c == 0:
        nearbyadder()
    elif c == 21:
        exit()

    clr()
    banner()
    print()
    print(f'{Style.BRIGHT + Fore.YELLOW + Back.RED}[+] Enviar mensagens em grupo:'+n)
    print(f'{Style.BRIGHT + Fore.CYAN}[1] Enviar mensagens em grupo - Multi Accounts (Threading)'+n)
    print(f'{Style.BRIGHT + Fore.CYAN}[2] Enviar mensagens em grupo com imagem - Multi Accounts (Threading)'+n)
    print(f'{Style.BRIGHT + Fore.CYAN}[3] Enviar mensagem em grupo com imagem - Single Account'+n)
    print(f'{Style.BRIGHT + Fore.CYAN}[4] Enviar apenas mensagem em grupo - Single Account'+n)
    print(f'{Style.BRIGHT + Fore.CYAN}[5] Enviar várias mensagens no grupo - Multi Messages'+n)
    print(f'{Style.BRIGHT + Fore.CYAN}[6] Enviar várias mensagens diferentes com imagem no grupo - Multi Messages'+n)
    print(f'{Style.BRIGHT + Fore.YELLOW + Back.RED}[+] Multi Group Message Sender:'+n)
    print(f'{Style.BRIGHT + Fore.CYAN}[7] Multi Group Sender with image - Multi Messages'+n)
    print(f'{Style.BRIGHT + Fore.CYAN}[8] Multi Group Sender - Multi Messages'+n)
    print(f'{Style.BRIGHT + Fore.CYAN}[9] Multi Group Sender with single image & message - Single Account'+n)
    print(f'{Style.BRIGHT + Fore.CYAN}[10] Multi Group Sender with only message - Single Account'+n)
    print(f'{Style.BRIGHT + Fore.YELLOW + Back.RED}[+] Repassador de mensagens em grupos:'+n)
    print(f'{Style.BRIGHT + Fore.CYAN}[11] Repassar automaticamente'+n)
    print(f'{Style.BRIGHT + Fore.CYAN}[12] Repassar automaticamente (SEM TAG)'+n)
    print(f'{Style.BRIGHT + Fore.YELLOW + Back.RED}[+] Disparo no privado:'+n)
    print(f'{Style.BRIGHT + Fore.CYAN}[13] extrator'+n)
    print(f'{Style.BRIGHT + Fore.CYAN}[14] Fazer disparo no privado'+n)
    print(f'{Style.BRIGHT + Fore.CYAN}[15] Fazer disparo no privado com imagem'+n)
    print(f'{Style.BRIGHT + Fore.YELLOW + Back.RED}[+] Exit Option:'+n)
    print(f'{Style.BRIGHT + Fore.CYAN}[16] voltar'+n)
    print(f'{Style.BRIGHT + Fore.CYAN}[17] sair'+n)
    e = int(input('\nDigite sua escolha: '))
    if e==1:
        messagesendergroup()
    elif e==2:
        messagesendergrouppic()
    elif e==3:
        messagesendergrouppicsingle()
    elif e==4:
        messagesendergroupsingle()
    elif e==5:
        messagesendergroupmultimsg()
    elif e==6:
        messagesendergroupmultimsgpic()
    elif e==7:
        messagesendergroupmultimsgpicmultigroups()
    elif e==8:
        messagesendergroupmultimsgmultigroups()
    elif e==9:
        messagesendermultigroupsinglepic()
    elif e==10:
        messagesendermultigroupsingle()
    elif e==11:
        forward_to_channels()
    elif e==12:
        forward_to_channelsnotag()
    elif e==13:
        multi_ccraper()
    elif e==14:
        messagesendering()
    elif e==15:
        messagesenderingpic()
    elif e==16:
        main_menu()
    elif e==17:
        quit()




def loginusingsecurity():
    clr()
    banner()
    print()
    print(f'{Style.BRIGHT + Fore.YELLOW + Back.RED}[+] Login avançado utilizando API ID e HASH, com Simulação de dispositivos diferentes:'+n)
    print(f'{Style.BRIGHT + Fore.CYAN}[1] Login avançado tipo 1'+n)
    print(f'{Style.BRIGHT + Fore.CYAN}[2] Login por números no arquivo CSV'+n)
    print()
    print(f'{Style.BRIGHT + Fore.YELLOW + Back.RED}[+] Exit Option:'+n)
    print(f'{Style.BRIGHT + Fore.CYAN}[0] voltar'+n)
    print(f'{Style.BRIGHT + Fore.CYAN}[3] sair'+n)
    f = int(input('\nDigite sua escolha: '))
    if f == 1:
        logintypeone()
    elif f == 2:
        logintypetwo()
    elif f == 0:
        main_menu()
    elif f == 3:
        exit()

main_menu()
