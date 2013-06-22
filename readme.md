Notify.py
===
Sends an SMS to a target number when run.

This script should be chained in a shell command:

`$ ./configure && make && make install && notify.py "installation done!`

##Usage

	$ notify.py --help
	usage: notify.py [-h] [-v] [-t] [-e EXECUTE] [-w WAIT] [-s] [-i IDENTITY]
	                 message
	
	positional arguments:
	  message               content of SMS to send
	
	optional arguments:
	  -h, --help            show this help message and exit
	  -v, --verbose         turns on console output
	  -t, --test            test mode. Prints API call but does not send SMS.
	                        Always prints regardless of --verbose
	  -e EXECUTE, --execute EXECUTE
	                        command to execute using this script's permissions
	  -w WAIT, --wait WAIT  time in seconds to wait before notifying. If specified
	                        with --execute, the timer will start after the spawned
	                        process completes
	  -s, --stingy          refuse to send SMS if len(message) > 160. Always
	                        prints refusal regardless of --verbose
	  -i IDENTITY, --identity IDENTITY
	                        identity file to use. Default: ~/.hoiioapi

##API File
The API file is a plain text document containing a single JSON object. The object contains one or more application names as keys. Each key has a JSON sub-structure containing that application's configuration parameters. The file may not contain comments.

The following is a sample `.hoiioapi`:

	{
		"notifypy": {
			"appid": "<some value>",
			"token": "<some value>",
			"number": "<some value>"
		}
	}

##Hoiio
You should create a [Hoiio Developer Account](http://developer.hoiio.com/) and a Hoiio App in order to get the values for App Id and Access Token. Note that if you're rolling with trial credits, the target phone number can only be the number you signed up with. 

##Use Cases
* Get notifed by SMS when your IDS trips.
* Set your workstation to text you when it has finished running `make`.
* Naïve notification when some one boots up your computer.
* Send SMS on a `cron` job!

##Future Work
1. Retry sending SMS for *n* times before giving up.

