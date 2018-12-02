#!/bin/bash

#ps aux | tail -n +2 | sort -k 3nr | awk 'NR<8{print $2,$3}' | ./piechart.sh 
for USER in $(ps haux | awk '{print $1}' | sort -u); 
do 
		ps haux | awk -v user=$USER '$1 ~ user { sum += $3} END {print user, sum;}' >> cpu.csv ;
done
