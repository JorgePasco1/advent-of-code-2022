#!/bin/bash
exercise_number=$1
exercise_name=$2

if test -z "$exercise_number" || test -z "$exercise_name"; then
  echo "Usage: $0 <exercise_number> <exercise_name>"
  exit 1
fi

if (($exercise_number < 10)); then
  exercise_number="0$exercise_number"
fi

mkdir -p $exercise_number-$exercise_name
touch $exercise_number-$exercise_name/README.md
touch $exercise_number-$exercise_name/sample
touch $exercise_number-$exercise_name/input
cp ./skeleton.py $exercise_number-$exercise_name/main.py
