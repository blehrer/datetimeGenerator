#!/usr/bin/env python
# encoding: utf-8
"""
daterangeGenerator.py

Created by Brian Lehrer on 2012-11-03.
Copyright (c) 2012 __Brian Lehrer__. All rights reserved.
"""

import sys
import os
from datetime import date, datetime, timedelta

def main():
	
	# Collect date input
	print "\ndaterangeGenerator.py"
	print "author: Brian Lehrer"
	print "originally written on November 3, 2012"
	print "latest update: November 3, 2012\n"
	print "This program will generate a daterange given `year`, `month`, `day`, `delta`, and `iterations`.\n"
	print "... Year"
	year = raw_input()
	print "month (01 = January...)"
	month = raw_input()
	print "...day (01 = first of the month)"
	day = raw_input()
	dateString = year+"/"+month+"/"+day

	
	# Convert the input date to datetime format
	dt = datetime.strptime(dateString,'%Y/%m/%d').date()
	
	# Collect the delta value
	print "... delta? (every __ days)"
	delta = raw_input()
	delta = int(delta)
	
	# Collect the range in the future
	print "...iterations? (number of dates "+str(delta)+" days in the future)"
	iterations = raw_input()
	iterations = int(iterations)
	
	# show inputs:
	#print "The date you will use as your base date is "+dateString
	#print "The delta you will apply to your base date is "+str(delta)+" days"
	#print "The delta will generate "+str(iterations)+" additional dates in the future"
	
	# Define the function that generates the daterange.
	
	def getDateRange(dt, delta, iterations):
		result = [dt]
		for i in range(iterations):
			a = result[i]+timedelta(days=delta)
			result.append(a)
		#print "In datetime format, the result is: "+str(result)+\n
		formattedArray =[result[i].strftime("%Y/%m/%d") for i in range(len(result))]
		print "Date range requested: "+str(formattedArray)+"\n"
		return result
		
	
	getDateRange(dt,delta,iterations)
	
	pass



if __name__ == '__main__':
	main()

