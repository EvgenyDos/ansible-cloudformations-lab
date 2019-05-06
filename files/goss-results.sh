#!/bin/bash
touch /root/results.yml
touch /root/results-for-mail.yml
goss -g /root/goss.yaml validate --format tap --max-concurrent 1 > /root/results.yml
goss -g /root/goss.yaml validate --format tap --max-concurrent 1 > /root/results-for-mail.yml

if [ $? -eq 0 ]
then
  echo "Success: zaebis."
  exit 0
else
  echo "Failure: nezaebis" >&2
  exit 1
fi

exit 0
