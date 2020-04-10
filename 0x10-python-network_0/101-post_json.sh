#!/bin/bash
# This script sends a POST request to the URL passed in the form of JSON data, and displays the body of the response.
curl -sH "Content-Type: application/json" -X POST -d @"$2" "$1"
