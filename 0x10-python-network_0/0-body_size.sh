#!/bin/bash
# Takes in a URL, sends a request to that URL,
# displays the size of the body of the response.
curl -s "$1" | grep "Content-Length:"| cut -d" " -f2
