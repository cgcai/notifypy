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
# --Xofel.

from urllib import urlencode
import urllib2
import json
import argparse
import os
import time

_HOIIO_SMS_API = "https://secure.hoiio.com/open/sms/send"
_VERBOSE = False

def main():
	global _VERBOSE

	parser = argparse.ArgumentParser()
	parser.add_argument("-v", "--verbose", action="store_true", help="turns on console output")
	parser.add_argument("-t", "--test", action="store_true", help="test mode. Prints API call but does not send SMS")
	parser.add_argument("-e", "--execute", help="command to execute using this script's permissions")
	parser.add_argument("-w", "--wait", type=int, help="time in seconds to wait before notifying. If specified with --execute, the timer will start after the spawned process completes")
	parser.add_argument("-s", "--stingy", action="store_true", help="refuse to send SMS if len(message) > 160. Always prints refusal regardless of --verbose")
	parser.add_argument("identity", help="identity file to use")
	parser.add_argument("message", help="content of SMS to send")
	args = parser.parse_args()

	if args.verbose:
		_VERBOSE = True

	with open(args.identity, "r") as f:
		appid = f.readline().strip()
		log("App ID: " + appid)
		token = f.readline().strip()
		log("App Token: " + token)
		dest = f.readline().strip()
		log("Dest: " + dest)

	if args.execute:
		log("Executing: " + args.execute)
		proc = os.system(args.execute)
		log("Process completed.")

	if args.wait:
		log("Sleeping for " + str(args.wait))
		time.sleep(args.wait)

	if len(args.message) > 160 and args.stingy:
		log("Refusing to send long message", always=True)
	else:
		log("Sending: " + args.message)
		send_sms(appid, token, dest, args.message, testmode=args.test)

def send_sms(appid, token, dest, message, testmode=False):
	request_data = {
		"app_id" : appid,
		"access_token" : token,
		"dest" : dest,
		"msg" : message
	}

	url = _HOIIO_SMS_API + "?" + urlencode(request_data)
	if testmode:
		print url
	else:
		req = urllib2.Request(url)
		resp_data = urllib2.urlopen(req).read()

		resp = json.loads(resp_data)
		if "status" in resp.keys() and resp["status"] == "success_ok":
			log("SMS sent.")
		else:
			log("Failed to send SMS.")

def log(message, always=False):
	if _VERBOSE or always:
		print message

if __name__ == '__main__':
	main()
