#!/bin/bash
RANGE=3
number=$RANDOM
let "number %= $RANGE"
echo "$number"
