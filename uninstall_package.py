#tell me https://github.com/strongpapazola if this script error

from os import system
import subprocess

# old
#a = subprocess.Popen('dpkg -l | grep bbb', shell=True, stdout=subprocess.PIPE).stdout
#a = str(a.read())
#a = a.split("'")[1]
#a = a.split('\\n')
#a = a[:-1]

def shell(cmd):
 a = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE).stdout.read().decode('utf-8')
 return a

a = shell('dpkg -l | grep bbb').splitlines()


j = []
for i in a:
 i = i.split('  ')
 if i[1]:
  print(i[1])
#  system('apt purge '+i[1]+' -y')

#system('apt autoremove -y')

