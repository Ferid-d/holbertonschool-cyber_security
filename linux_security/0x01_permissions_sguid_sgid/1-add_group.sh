#!/bin/bash
sudo groupadd "$1"
sudo chown :"$1" "$2"
sudo chgrp g=r+x "$2" 
