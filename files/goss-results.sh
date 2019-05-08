#!/bin/bash

/usr/local/bin/goss -g /root/goss.yaml validate --format tap --max-concurrent 1 |egrep -v "ssh-access: exists: matches|exit-status: matches expectation" > /root/results.txt

echo "The common results are:" >> /root/results.txt
echo "" >> /root/results.txt
cat /root/results.txt|awk '{if ($1=="not") notok=notok+1; if ($1=="ok") ok=ok+1} END{print "ok=", ok, "notok=",notok}' >> /root/results.txt

exit 0
