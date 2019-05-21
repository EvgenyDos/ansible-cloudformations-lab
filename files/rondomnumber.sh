#!/bin/bash
RANGE=5
number=$RANDOM
let "number %= $RANGE"
echo "$number"
