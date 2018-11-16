#!/bin/bash

#Calculating last date of month, which is set to 0.
for i in {0..24};
do 
		date -d "-$(date +%d) days +$i month" >> last_date.txt
done

