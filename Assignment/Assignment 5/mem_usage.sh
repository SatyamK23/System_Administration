#!/bin/bash

#ps aux | tail -n +2 | sort -k 3nr | awk 'NR<8{print $2,$3}' | ./piechart.sh 
TOTAL=$(free | awk '/Mem:/ { print $2 }')
echo "$TOTAL"
for USER in $(ps haux | awk '{print $1}' | sort -u)
do
		ps haux -U $USER | awk -v user=$USER -v total=$TOTAL '{ sum += $6 } END { printf "%s %.2f\n", user, sum / total * 100; }' >> mem_usage.csv
done
