#!/usr/bin/env python

import sys
import os
import time
from urllib import urlencode
import urllib2

# Exit codes.
_EXIT_SYNTAX = 1
_HOIIO_SMS_API = "https://secure.hoiio.com/open/sms/send"

# Script globals.
_def_dest = ""
_hoiio_appid = ""
_hoiio_access_token = ""

def main():
	send_sms("xyz", "abc", "82998500", "hello world")
	# (should_exec, command, should_wait, duration, idf, message = parse_args()

	# if _should_exec:
	# 	proc = os.system(_command)
	# 	print "Spawned process:", str(proc)

	# if _should_wait:
	# 	print "Sleeping for", _wait_duration, "seconds"
	# 	time.sleep(_wait_duration)

	# print "Notifying..."
	# success = send_sms()

	# if not success:
	# 	print "Failed to send SMS."
	# else:
	# 	print "SMS sent."

def parse_args():
	pass

def send_sms(appid, token, dest, message):
	request_data = {
		"app_id" : appid,
		"access_token" : token,
		"dest" : dest,
		"msg" : message
	}

	url = _HOIIO_SMS_API + "?" + urlencode(request_data)
	req = urllib2.Request(url)
	resp = urllib2.urlopen(req).read()

	print resp

def usage():
	print "usage: notify.py [-e <command>] [-t <time, seconds>] <id file> <message>"
	sys.exit(_EXIT_SYNTAX)

if __name__ == '__main__':
	main()
