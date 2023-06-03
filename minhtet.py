import os,time,platform
os.system('clear')
print('[•] Checking Updates...')
os.system('git pull')
green = ('\033[1;32m')
white = ('\033[1;37m')
red = ('\033[1;31m')

import getpass

attemp = 0

while attemps < 12345677901:

username  = input(' \033[0;95mEnter Username : ')

if username  == 'MMHtet'

print(' \033[0;97mYou Have Successfully Logged in.')

break

else:

print(' Incorrect username ')

attemps += 1

continue

os.system('clear')

print('<------------------------------------>')
bit = platform.architecture()[0]
if bit=='64bit':
    print(f'{red}[•] Join Over Facebook Group {white}')
    os.system('xdg-open https://facebook.com/groups/1422983921406005//')
    time.sleep(0.05)
    import trt1
elif bit=='32bit':
    import trt32
else:
    print(f'{green}[×] Sorry System Not Support{white}')
