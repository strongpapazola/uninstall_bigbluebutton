#tell me https://github.com/strongpapazola if this script error

from os import system
import subprocess
import time

a = '''
__     ___     _ _     _
\ \   / (_)___(_) |_  | |
 \ \ / /| / __| | __| | |
  \ V / | \__ \ | |_  |_|
   \_/  |_|___/_|\__| (_)

Author : https://github.com/strongpapazola/
'''

print(a)
time.sleep(3)


def shell(cmd):
 a = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE).stdout.read().decode('utf-8')
 return a

a = shell('dpkg -l | grep bbb').splitlines()

pemisah = ' '
j = []
for i in a:
 i = i.split('  ')
 if i[1]:
  j.append(i[1])
  

system('apt purge --autoremove '+str(pemisah.join(j))+' -y')

