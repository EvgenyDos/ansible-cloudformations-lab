#!/bin/bash

set timeout 20

echo " StrictHostKeyChecking no" >> /root/.ssh/config

#ssh sshuser@localhost "id" > /root/results-ssh-access

exit 0
