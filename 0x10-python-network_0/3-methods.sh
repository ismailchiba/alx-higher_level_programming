#!/bin/bash
# displays all HTTP methods the server will accept.
curl -sL "$1" | grep "Allow" | cut -d ' ' -f 2-
