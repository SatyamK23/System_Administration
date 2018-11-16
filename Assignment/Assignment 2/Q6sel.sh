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
			sum=$(($a + $b))
			echo "$sum"
			break
	elif [ "$option" = "Subtraction" ];
	then
			sub=$(($a - $b))
			echo "$sub"
			break
	elif [ "$option" = "Multiplication" ];
	then
			mult=$(($a * $b))
			echo "$mult"
			break
	elif [ "$option" = "Division" ];
	then
			div=$(($a /$b))
			echo "$div"
			if [ $b -eq 0 ]
			then
					echo -e "Division by zero is not possible\n
					Terminal closes in 5s" && sleep 5 && exit;
			fi
	        break
	else
         break
	fi
done

