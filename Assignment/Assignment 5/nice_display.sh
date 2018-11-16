#!/bin/bash

echo "Displaying of Top 5 Process"
ps -eo user,pid,pcpu,pri,ni --sort=pcpu | tail -n 5

