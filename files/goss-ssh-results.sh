#!/bin/bash

ssh -o BatchMode=yes -o StrictHostKeyChecking=no sshuser@localhost "id" > /root/results-ssh-access

exit 0