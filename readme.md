Notify.py
===
Sends an SMS to a target number when run.

This script should be chained in a shell command:

`$ do_something_long && notify.py -w 5 "something is done!`

##Usage

	$ notify.py --help
	usage: notify.py [-h] [-v] [-t] [-e EXECUTE] [-w WAIT] [-s] [-i IDENTITY]
	                 message

	positional arguments:
	  message               content of SMS to send

	optional arguments:
	  -h, --help            show this help message and exit
	  -v, --verbose         turns on console output
	  -t, --test            test mode. Prints API call but does not send SMS
	  -e EXECUTE, --execute EXECUTE
	                        command to execute using this script's permissions
	  -w WAIT, --wait WAIT  time in seconds to wait before notifying. If specified
	                        with --execute, the timer will start after the spawned
	                        process completes
	  -s, --stingy          refuse to send SMS if len(message) > 160. Always
	                        prints refusal regardless of --verbose
	  -i IDENTITY, --identity IDENTITY
	                        identity file to use. Default: ~/.notifypy

##Identity File
The id file should consist of the following lines with no leading or trailing characters except whitespace. Notifypy tries to read `~/.notifypy` if `--identity` is not specified.

1. App Id
2. Access Token
3. Target Number

Additional lines are ignored.

You should create a [Hoiio Developer Account](http://developer.hoiio.com/) and a Hoiio App in order to get the values for App Id and Access Token. Note that if you're rolling with trial credits, the target phone number can only be the number you signed up with. 

##Use Cases
* Get notifed by SMS when your IDS trips.
* Set your workstation to text you when it has finished running `make`.
* Naïve notification when some one boots up your computer.
* Send SMS on a `cron` job!
