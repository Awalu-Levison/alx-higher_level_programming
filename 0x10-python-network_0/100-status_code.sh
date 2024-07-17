#!/bin/bash
curl -s -o /dev/null "%[http_code]" "$1"
