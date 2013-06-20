Notify.py
===
Sends an SMS to a target number when run.

This script should be chained in a shell command:

`$ do_something_long && sleep 5 && ./notify hoiio.id "something is done!`

The id file should consist of the following lines with no leading or trailing characters except whitespace.

1. App Id
2. Access Token
3. Target Number


Additional lines are ignored.

--Xofel.

##Use Cases
* Get notifed by SMS when your IDS trips.
* Set your workstation to text you when it has finished running `make`.
* Naïve notification when some one boots up your computer.

##Future Work
1. Execute `<command>` before sending SMS.
2. Wait *n* seconds before sending SMS.
