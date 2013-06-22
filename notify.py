#!/usr/bin/env python

# Sends an SMS to a target number when run. --Xofel.

from urllib import urlencode
import urllib2
import json
import argparse
import os
import time

_APP_NAME = "notifypy"
_HOIIO_SMS_API = "https://secure.hoiio.com/open/sms/send"
_VERBOSE = False
_SMS_LIMIT = 160

def main():
	global _VERBOSE

	parser = argparse.ArgumentParser()
	parser.add_argument("-v", "--verbose", action="store_true", help="turns on console output")
	parser.add_argument("-t", "--test", action="store_true", help="test mode. Prints API call but does not send SMS. Always prints regardless of --verbose")
	parser.add_argument("-e", "--execute", help="command to execute using this script's permissions")
	parser.add_argument("-w", "--wait", type=int, help="time in seconds to wait before notifying. If specified with --execute, the timer will start after the spawned process completes")
	parser.add_argument("-s", "--stingy", action="store_true", help="refuse to send SMS if len(message) > 160. Always prints refusal regardless of --verbose")
	parser.add_argument("-i", "--identity", default="~/.hoiioapi", help="identity file to use. Default: ~/.hoiioapi")
	parser.add_argument("message", help="content of SMS to send")
	args = parser.parse_args()

	if args.verbose:
		_VERBOSE = True

	id_path = os.path.expanduser(args.identity)
	cred = read_credentials(id_path)
	if not cred:
		log("Unable to load credentials.")
		return
	else:
		log(str(cred))
		appid, token, dest = cred

	if args.execute:
		log("Executing: " + args.execute)
		proc = os.system(args.execute)
		log("Process completed.")

	if args.wait:
		log("Sleeping for " + str(args.wait))
		time.sleep(args.wait)

	if len(args.message) > _SMS_LIMIT and args.stingy:
		log("Refusing to send long message", always=True)
	else:
		log("Sending: " + args.message)
		send_sms(appid, token, dest, args.message, testmode=args.test)

def read_credentials(path):
	try:
		with open(path, "r") as f:
			dat = f.read()
		struct = json.loads(dat)
		app_settings = struct[_APP_NAME]
		if app_settings and app_settings["appid"] and app_settings["token"] and app_settings["number"]:
			return (app_settings["appid"], app_settings["token"], app_settings["number"])
		else:
			return None
	except IOError:
		return None

def send_sms(appid, token, dest, message, testmode=False):
	request_data = {
		"app_id" : appid,
		"access_token" : token,
		"dest" : dest,
		"msg" : message
	}

	url = _HOIIO_SMS_API + "?" + urlencode(request_data)
	if testmode:
		log("Test Mode: " + url, always=True)
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

if __name__ == "__main__":
	main()
