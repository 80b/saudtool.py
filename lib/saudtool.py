################
# Made by Raz  #
# Dont Skid Me.#
################

import os
import requests
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def menu():
	print(bcolors.OKCYAN + """
▒▒▒▒▒▒▒▒▒▒▒▄▄▄▄░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▄██████▒▒▒▒▒▄▄▄█▄▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▄██▀░░▀██▄▒▒▒▒████████▄▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒███░░░░░░██▒▒▒▒▒▒█▀▀▀▀▀██▄▄▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▄██▌░░░░░░░██▒▒▒▒▐▌▒▒▒▒▒▒▒▒▀█▄▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒███░░▐█░█▌░██▒▒▒▒█▌▒▒▒▒▒▒▒▒▒▒▀▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒████░▐█▌░▐█▌██▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▐████░▐░░░░░▌██▒▒▒█▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒████░░░▄█░░░██▒▒▐█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒████░░░██░░██▌▒▒█▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒████▌░▐█░░███▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▐████░░▌░███▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒████░░░███▒▒▒▒█▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒██████▌░████▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▐████████████▒▒███▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒█████████████▄████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
██████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
██████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
█████████████████▀▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
█████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒

 ######     ###    ##     ## ########  ########  #######   #######  ##       
##    ##   ## ##   ##     ## ##     ##    ##    ##     ## ##     ## ##       
##        ##   ##  ##     ## ##     ##    ##    ##     ## ##     ## ##       
 ######  ##     ## ##     ## ##     ##    ##    ##     ## ##     ## ##       
      ## ######### ##     ## ##     ##    ##    ##     ## ##     ## ##       
##    ## ##     ## ##     ## ##     ##    ##    ##     ## ##     ## ##       
 ######  ##     ##  #######  ########     ##     #######   #######  ######## 

                      The one and only Python Tool!
                        Sauds Gonna Pop Dat Skid
                             Made by Raz
                                 v1.1
                            
+=+=+=+=+=+==+=+=+=+=+==+=+=+==+==+=+=+=+=+==+=+=+=+=+=+=+=+=+=++=+=+=+=+=+=++=+=+=+=+=+=+=+
""" + bcolors.ENDC + bcolors.OKCYAN + """
What would you like to do?
[1] Ping an IP                [5] Nmap Port Scan (must have nmap installed)
[2] Credits                   [6] Geolocate an IP             
[3] Exit the application      [7] Open a NetCat file transfer (for exploiting / hacking / pentesting)
[4] View the Discord Server!  [8] What is my IP?
	""")
	print("• Dont skid me ;)")
menu()



inps = int(input('Which Option?: '))
def pingpong():
	inp = input('What is the IP you want to ping?: ')
	os.system("ping -t 10 " + inp)
	if inp == 0:
			print("• The IP is Online!")
	else:
				print("• Skid down")
while inps != 3:
	#Pinging ip
	if inps == 1:
		pingpong()
		break
	elif inps == 4:
             print('https://discord.gg/AVMQ35Pft5')
             print("Join or gay")
             break
	elif inps == 8:
    	 print('Looking up IP Address...')
    	 os.system('ifconfig')
    	 break
	elif inps == 5:
	   	ip = input('What is the IP you would like to scan?: ')
	   	os.system('nmap scan ' + ip)
	elif inps == 6:
		ipinput = input("What is the IP you would like to geolocate?: ")
		response = requests.get("https://geolocation-db.com/json/" + ipinput +  "&position=true").json()
		print(response)
	elif inps == 7:
		print('NetCat: You are listening on port 9999!')
		os.system('nc -lnvp 9999')
		break
	elif inps == 2:
		os.system('clear')
		print("""
	
..######..########..########.########..####.########..######.
.##....##.##.....##.##.......##.....##..##.....##....##....##
.##.......##.....##.##.......##.....##..##.....##....##......
.##.......########..######...##.....##..##.....##.....######.
.##.......##...##...##.......##.....##..##.....##..........##
.##....##.##....##..##.......##.....##..##.....##....##....##
..######..##.....##.########.########..####....##.....######.

+=+=+=+=+==+=+=+=+=+=+==+=+=+=+=+=+=+=+=+=+=++=+=+=+=+=+=+=+=

      This Pinger Was Made By Raz
              • Special Thanks To                     
                     Buzz
                     Saud
                           """)
		break
	else:
             print("Invalid option")
             os.system('clear')
             menu()
             inps = input('Which Option?: ')
print('Exiting, Thanks for using SaudTool')


def DevPanel():
	print("working on")
	
#Dev Panel Obfuscator	
def PanelObfuscator():
	print('Obfuscator')

#ToDo
"""
Add obfuscator for dev shit
Add dev options
Add a Premium category
"""




    
