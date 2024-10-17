#!/bin/bash

ip=$1

p1=`echo $ip | cut -d'.' -f1`
if [ -z "$p1" ]; then 
    echo "An IP address is of form and range [0-255].[0-255].[0-255].[0-255] without square brackets"
    exit 1
fi

p2=`echo $ip | cut -d'.' -f2`
if [ -z "$p2" ]; then 
    echo "An IP address is of form and range [0-255].[0-255].[0-255].[0-255] without square brackets"
    exit 1
fi

p3=`echo $ip | cut -d'.' -f3`
if [ -z "$p3" ]; then 
    echo "An IP address is of form and range [0-255].[0-255].[0-255].[0-255] without square brackets"
    exit 1
fi

p4=`echo $ip | cut -d'.' -f4`
if [ -z "$p4" ]; then 
    echo "An IP address is of form and range [0-255].[0-255].[0-255].[0-255] without square brackets"
    exit 1
fi

print_number=""

for (( i=4; i>0; i-- )); do
    number=$(eval echo "\$p$i");
    while (( $number > 0 )); do
        R=$(($number % 2 ))
        print_number="$R$print_number"
        number=$((number/2))
    done
    if (( $i != 1 )) then
        print_number=" $print_number"
    fi
done

echo $print_number
