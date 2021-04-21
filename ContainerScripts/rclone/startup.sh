#!/bin/sh

export RC_IP_ADDR=`hostname -i`

rclone rcd --rc-no-auth --rc-addr $RC_IP_ADDR:5572