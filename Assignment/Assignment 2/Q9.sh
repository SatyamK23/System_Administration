#!/bin/bash

Factorial()
{
		num=$1
		fact=1
		while [ $num -ge 1 ]
		do
		   fact=`expr $fact \* $num `
		   num=`expr $num - 1`
		done
		echo  "$fact" | bc
} 

Factorial $1

