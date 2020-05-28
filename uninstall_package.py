#tell me https://github.com/strongpapazola if this script error

from os import system
import subprocess

def shell(cmd):
 a = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE).stdout.read().decode('utf-8')
 return a

a = shell('dpkg -l | grep bbb').splitlines()


j = []
for i in a:
 i = i.split('  ')
 if i[1]:
  system('apt purge '+i[1]+' -y')

system('apt autoremove -y')

