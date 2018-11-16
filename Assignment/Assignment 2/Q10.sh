#!/bin/bash
#Ref-1. https://misc.flogisoft.com/bash/tip_colors_and_formatting

read -p "Type your message.." msg

#Bold effect
echo -e "\033[1m $msg"

#echo -e "\033[7m $msg"
#Red Color
echo -e "\033[31m$msg"

#Green Color
echo -e "\033[32m$msg"

#Yellow Color
echo -e "\033[33m$msg"

#Blink effect
echo -e "\e[5m$msg"

#Normal 
echo -e "\033[0m $msg"

