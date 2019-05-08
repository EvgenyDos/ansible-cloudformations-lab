#!/bin/bash

ssh -o BatchMode=yes -o StrictHostKeyChecking=no sshuser@localhost "id" > /root/results-ssh-access

if [[ $? -ne 0 ]]; then
  rm -rf /root/results-ssh-access
else
  echo "ok"
fi

exit 0
