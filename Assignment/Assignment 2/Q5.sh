#!/bin/bash

#3 numbers are a,b,c

a=$1
b=$2
c=$2

if [ $# -ne 3 ]
then 
   echo "Some arguments are missing."&& exit 1
fi

#Comparing each argument with other.
#-a is used for as an extension for argument
 if [ $1 -eq $2 -a  $1 -eq $2 ]
 then
   echo "All arguments have equal values"
 elif [[  $1 -eq $2 && $1 -ge $3  ||  $2 -eq $3 && $2 -ge $1  ||   $3 -eq $1 && $1 -ge $2  ]]
 then
   echo "Greatest Number cannot be figured out."
 elif [ $1 -gt $2 -a $1 -gt $3 ] 
 then
   echo "$1 is the Greatest Number"
  elif [ $2 -gt $3 -a $2 -gt $1 ]
  then 
	echo "$2 is the Greatest number"
  else
	echo "$3 is the Greatest number"
fi


