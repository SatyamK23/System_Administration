TOTAL=$(free | awk '/Mem:/ { print $2 }')
for USER in $(ps haux | awk '{print $1}' | sort -u)
do
    ps hux -U $USER | awk -v user=$USER -v total=$TOTAL '{ sum += $6 } END { printf "%s %.2f\n", $USER, sum / total * 100; }'
done
