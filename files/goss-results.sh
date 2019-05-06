#!/bin/bash
/usr/local/bin/goss -g /root/goss.yaml validate --format tap --max-concurrent 1 > results.yml
/usr/local/bin/goss -g /root/goss.yaml validate --format tap --max-concurrent 1 > results-for-mail.yml
exit 0
