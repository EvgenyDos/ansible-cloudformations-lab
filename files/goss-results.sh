#!/bin/bash
touch /root/results.yml
touch /root/results-for-mail.yml
/usr/local/bin/goss -g /root/goss.yaml validate --format tap --max-concurrent 1 > /root/results.yml
/usr/local/bin/goss -g /root/goss.yaml validate --format tap --max-concurrent 1 > /root/results-for-mail.yml

exit 0
