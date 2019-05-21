#!/bin/bash
RANGE=1
number=$RANDOM
let "number %= $RANGE"
echo "$number"
