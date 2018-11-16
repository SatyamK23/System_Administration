#!/bin/bash

echo -ne "Enter two number\n"
read a b

echo -n "Select your choice"
options=("Addition" "Subtraction" "Multiplication" "Division" "Quit")

select opt in "${options[@]}"
do
   case $opt in 
		"Addition")
			sum=$(($a + $b))
	    	echo "$sum"
		    break
		    ;;
		"Subtraction")
			sub=$(($a - $b))
		    echo "$sub"
		    break
		    ;;
		"Multiplication")
			mult=$(($a * $b))
		    echo "$mult"
		    break
		    ;;
		"Division")
			div=$(($a / $b))
		    echo "$div"
		    if [ $b -eq 0 ]
		    then
		       echo -e "Division by Zero is not possible.\n
			     Terminal closes in 5s" && sleep 5 && exit 1;
		    fi
		    break
		    ;;
		"Quit")
		    break
		    ;;
   esac
done


