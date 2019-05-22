#!/bin/bash
RANGE=7
number=$RANDOM
let "number %= $RANGE"
echo "$number"
