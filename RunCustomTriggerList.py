#!/usr/bin/env python3


##########################################################################################
# General Information
##########################################################################################
#
#	Script created By William Grzybowski December 15, 2020
#
#	Version 1.0	- Initial Creation of Script.
#
#	This script was built to run a comma seperated list of custom triggers from
#	JAMF VAriable $4.
#	
#	This allowes you to reuse policies with custom triggers but not have to maintain
#	more than one policy.
#
##########################################################################################


##########################################################################################
# License information
##########################################################################################
#
#	Copyright (c) 2020 William Grzybowski
#
#	Permission is hereby granted, free of charge, to any person obtaining a copy
#	of this software and associated documentation files (the "Software"), to deal
#	in the Software without restriction, including without limitation the rights
#	to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#	copies of the Software, and to permit persons to whom the Software is
#	furnished to do so, subject to the following conditions:
#
#	The above copyright notice and this permission notice shall be included in all
#	copies or substantial portions of the Software.
#
#	THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#	IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#	FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#	AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#	LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#	OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#	SOFTWARE.
#
##########################################################################################


##########################################################################################
# Imports
##########################################################################################
import time, sys, subprocess


##########################################################################################
# Variables
##########################################################################################
# Get Custom Events Name from User interface. JAMF variable $4
myPolicyToRun = sys.argv[4]

# Make Custom Events into a list for the for loop
myPolicyToRunList = myPolicyToRun.split(", ")


##########################################################################################
# Core Script
##########################################################################################
# Run the policies for each Custom Events.
for x in myPolicyToRunList:
	customEvent = (x)
	
	sys.stderr.write("\nNow running custom event: " + customEvent + "\n")
	subprocess.call(['/usr/local/jamf/bin/jamf', 'policy', '-event', customEvent])
	
	time.sleep(5)
