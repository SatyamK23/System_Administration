#!/bin/sh

echo "Enter number :"
read num

rem=0
sum=0

while [ $num -gt 0 ]
do
   rem=$(( $num % 10 ))
   num=$(( $num / 10 ))
   sum=$(( $sum + $rem ))
done
echo "Sum of digits of number $num is $sum"
