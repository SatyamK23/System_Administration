#!/bin/bash

ps aux | tail -n +2 | sort -k 3nr | awk 'NR<8{print $2,$3}' | ./piechart.sh 
