#!/bin/bash

/usr/local/bin/goss -g /root/goss.yaml validate --format tap --max-concurrent 1 |egrep -v "ssh-access: exists: matches|exit-status: matches expectation"|sed 1d > /root/results.txt

echo "" >> /root/results.txt
echo "The common results are:" >> /root/results.txt
echo "" >> /root/results.txt

cat /root/results.txt|awk '{if ($1=="not"||$0~/SKIP/) failed=failed+1; else if ($1=="ok") ok=ok+1} END{print "ok=", ok, "failed=",failed}' >> /root/results.txt

exit 0
