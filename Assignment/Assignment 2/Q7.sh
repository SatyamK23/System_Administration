#!/bin/bash

echo -ne "Enter two real number\n"
read a b

echo -n "Select your choice"
options=("Addition" "Subtraction" "Multiplication" "Division" "Quit")

select opt in "${options[@]}"
do
	case $opt in 
		"Addition")
				echo "scale=4;$a + $b" | bc
				break
				;;
		"Subtraction")
				echo "scale=4;$a - $b" | bc
				break
				;;
		"Multiplication")
				echo "scale=4;$a * $b" | bc
				break
				;;
		"Division")
		    if [ $b = 0 ];
		    then
			   echo -e "Division by Zero is not possible.\n
			   Terminal closes in 5s" && sleep 5 && exit 1;
			else
				echo "scale=4; $a / $b" | bc 
		     fi
            break
		    ;;
		"Quit")
				break
				;;
	esac
done


