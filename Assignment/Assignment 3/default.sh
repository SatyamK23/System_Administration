value = $
echo "Enter value for changing boot order"
bo = s/GRUB_DEFAULT=.*/GRUB_DEFAULT=${value}/
sudo -S sed -i "$bo" /etc/default/grub
sudo grub-mkconfig -o /boot/grub/grub.cfg
