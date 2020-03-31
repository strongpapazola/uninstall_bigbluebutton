from os import system
import subprocess
a = subprocess.Popen('dpkg -l | grep bbb', shell=True, stdout=subprocess.PIPE).stdout
a = str(a.read())
a = a.split("'")[1]
a = a.split('\\n')
a = a[:-1]

j = []
for i in a:
 i = i.split('  ')
 if i[1]:
  system('apt purge '+i[1]+' -y')

system('apt autoremove -y')

