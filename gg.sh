#!/bin/bash







apt install netcat -y

echo -e " _____________________________"
echo -e "*                             *"
echo -e "*    1) listoner              *"
echo -e "*                             *"
echo -e "*    2) connector             *"
echo -e "*                             *"
echo -e "*    3) file transfer (lis)   *"
echo -e "*                             *"
echo -e "*    4) exit                  *"
echo -e "*_____________________________*"

read n
case $n in
	1)echo  "enter port = "
		read -p l
		nc -lp $l
		;;
	2)echo -e " enter ip = " 
		read a
		echo  "enter port = "
		read l
		nc -nv $a $l
		;;
	3)echo  "enter port = "
		read l
		nc -lp $l -e /bin/bash
		;;
	4)exit
		;;
esac

