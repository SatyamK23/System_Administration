#!/bin/bash
value=$1
par=s/GRUB_TIMEOUT=.*/GRUB_TIMEOUT=${value}/
sudo -S sed -i "$par" /etc/default/grub
sudo grub-mkconfig -o /boot/grub/grub.cfg

