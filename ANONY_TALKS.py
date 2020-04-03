red='\033[1;31m'
rset='\033[0m'
grn='\033[1;32m'
ylo='\033[1;33m'
blue='\033[1;34m'
cyan='\033[1;36m'
pink='\033[1;35m'
end = '\033[1;m'
import os

print      (red + 'MADE BY ARO' + rset)
print (" ")
print("•==============================•")
print("•                              •")
print("•    [1] listoner              •")
print("•                              •")
print("•    [2] connector             •")
print("•                              •")
print("•    [3] file transfer (lis)   •")
print("•                              •")
print("•    [4] exit                  •")
print("•==============================•")
a = int(input())
if a==1:
    p = int(input(red + "enter port = "+ rset))
    os.system("nc -lp{}".format(p))
if a==2:
    l = input(red + "enter ip = "+ rset)
    print (" ")
    p = input(grn + "enter port = "+ rset)
    os.system("nc -nv {} {}".format(l,p))
if a==3:
    p = int(input(red +"enter port = "+ rset))
    os.system("nc -lp{} -e /bin/bash".format(p))
if (a!=1 and a!=2 and a!=3 and a!=4):
    print (blue +"sorry,run again this program"+ rset)

