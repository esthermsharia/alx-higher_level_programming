#!/bin/bash
# Takes in a URL as an argument, sends a POST request tothe passed URL, and displays the body of the response.
curl -s "$1" -X POST -d "email=hr@hr@holbertonschool.com&subject=I will always be here for PLD"
