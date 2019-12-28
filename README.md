# SenseHat Fuzzy Time Clock

A simple "clock" application for your [raspberry pi](https://www.raspberrypi.org/) and [sensehat](https://projects.raspberrypi.org/en/projects/getting-started-with-the-sense-hat). It displays a colour in the middle for the hour, and a block around the edge in a sort of clock-type pattern. The corner markers you can think of as "ears" - they tell you which way "up" is, for context when you just woke up and it is dark :)

The code is python, and should pretty much work as-is. Run the code once and it checks the time, sets the lights, and exits. Try setting it up with a cron job like this:

1. Run `crontab -e`

2. Add this line to the end of the file:

`* * * * * /usr/bin/python ~/night-clock/clock.py`

## Contributing

Issues, pull requests and other interactions are all welcome!
