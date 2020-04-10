#!/bin/bash
# This script sends a request to the URL passed and displays the status code.
curl -so /dev/null -w "%{http_code}" "$1"
