#!/bin/bash

echo "Enter Integer Number"
read num

echo "Number entered is $num"

for (( i=num; i!=0;i-- ))
do
   if [ $i -ge 0 ]
   then
       echo -ne "$i\n";
   else
       echo -e "Positive integer (greater or equal to 0) is accepted.\n
	   Terminal will close after 5seconds"  && sleep 5 && exit 1;
   fi
done
