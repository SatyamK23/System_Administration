#!/bin/bash

CPU=$(top -b -n1 >> Log.txt)
MEM=$(top -b -n1 | grep "KiB Mem" | head -1 >> Memory_log.txt )

