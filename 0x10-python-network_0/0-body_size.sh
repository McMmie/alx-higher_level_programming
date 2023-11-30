#!/usr/bin/env bash
# displaays the size of the body of a URL response
curl -s -w '%{size_download}\n' -o /dev/null $1
