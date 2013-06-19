#!/usr/bin/env python

# Sends an SMS to a target number when run.
# This script should be chained in a shell command:
# $ do_something_long && sleep 5 && ./notify hoiio.id "something is done!"
# 
# The id file should consist of the following lines with no leading or trailing characters except whitespace.
# 1. App Id
# 2. Access Token
# 3. Target Number
# Additional lines are ignored.
#
# Usage: notify.py <id file> <message>
#
# --Xofel.

import sys
from urllib import urlencode
import urllib2
import json

# Exit codes.
_EXIT_SYNTAX = 1
_HOIIO_SMS_API = "https://secure.hoiio.com/open/sms/send"

def main():
	id_file, message = parse_args()
	with open(id_file, "r") as f:
		appid = f.readline().strip()
		token = f.readline().strip()
		dest = f.readline().strip()

	send_sms(appid, token, dest, message)

def parse_args():
	if len(sys.argv) != 3:
		print usage()
		sys.exit(_EXIT_SYNTAX)

	id_file = str(sys.argv[1])
	message = str(sys.argv[2])

	return (id_file, message)

def send_sms(appid, token, dest, message):
	request_data = {
		"app_id" : appid,
		"access_token" : token,
		"dest" : dest,
		"msg" : message
	}

	url = _HOIIO_SMS_API + "?" + urlencode(request_data)
	req = urllib2.Request(url)
	resp_data = urllib2.urlopen(req).read()

	resp = json.loads(resp_data)
	if "status" in resp.keys() and resp["status"] == "success_ok":
		print "SMS sent."
	else:
		print "Failed to send SMS."

def usage():
	return "usage: notify.py <id file> <message>"

if __name__ == '__main__':
	main()
