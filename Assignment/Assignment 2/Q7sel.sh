#!/bin/bash
echo -ne "Enter 2 numbers\n"
read a b

echo "Select option for calculator"

select option in\
		"Addition"\
		"Subtraction"\
		"Multiplication"\
		"Division"\
		"Exit"

do
	if [ "$option" = "Addition" ];
	then
			echo "scale=4;$a + $b" | bc
			break
	elif [ "$option" = "Subtraction" ];
	then
			echo "scale=4;$a - $b" | bc
			break
	elif [ "$option" = "Multiplication" ];
	then
			echo "scale=4; $a * $b" | bc
			break
	elif [ "$option" = "Division" ];
	then
			if [ $b =  0 ];
			then
					echo -e "Division by zero is not possible\n
					Terminal closes in 5s" && sleep 5 && exit;
			else
					echo "scale=4; $a / $b" | bc
			fi
	        break
	else
         break
	fi
done
