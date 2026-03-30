#!/bin/bash

CURRENT_TIME=$(date +"%H:%M")
HOUR=$(date +"%H")
MINUTE=$(date +"%M")

TOTAL_MINUTES=$((10#HOUR * 60 + 10#MINUTE))
END_MINUTE=1080
REMAINING=$((END_MINUTES - TOTAL_MINUTES))

if [ $REMAINING -le 0 ]; then
	echo "Current time is: $CURRENT_TIME. Work day has already ended!"
else
	REMAINING_HOUR=$((REMAINING / 60))
	REMAINING_MINUTE=$((REMAINING % 60))
	echo "Current time: $CURRENT_TIME. Work day ends after $REMAINING_HOUR hours and $REMAINING_MINUTE minutes."
fi
