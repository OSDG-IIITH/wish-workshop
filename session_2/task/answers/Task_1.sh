#!/bin/bash

if (( $# != 2 )) then 
    echo "Program expects two numerical arguments" 
    exit 1
else

    gcd () {
        local A=$1 B=$2
        if (( $A > $B )); then
            BIG=$A
            SMALL=$B
        else 
            BIG=$B 
            SMALL=$A 
        fi
    
        while (( $SMALL != 0 )); do
            local R=$(( $BIG % $SMALL )) 
            BIG=$SMALL
            SMALL=$R
        done
        echo $BIG
    }
    
    lcm () {
        local A=$1 B=$2 
        local GCD=$(gcd $A $B)
        LCM=$(( $A * $B / $GCD ))
        echo $LCM
    }
    
    echo "GCD: $(gcd $1 $2)"
    echo "LCM: $(lcm $1 $2)"

fi
