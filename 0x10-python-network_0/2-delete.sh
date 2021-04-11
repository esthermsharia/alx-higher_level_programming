#!/bin/bash
# Sends a DELETE request to the URL passed as 1st argument and displays the body of the respose
curl -s "$1" -X DELETE
