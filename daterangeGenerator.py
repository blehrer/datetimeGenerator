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
	dateRangeGenerator()
		

def dateRangeGenerator():
	"""docstring for dateRangeGenerator"""
	inputs = collectInputs()
	cInputs = convertInputs(inputs)
	result = getDateRange(cInputs)
	modifiedOutput = modifyOutput(result)
	doitAgain()
	
def doitAgain():
	repeatIt = raw_input("\n\n\nWould you like to do this again? (y/n):  ")
	if repeatIt == "y":
		print "\n\nOK\n\n"
		dateRangeGenerator()
	elif repeatIt == "n":
		print "\n"	
	
def collectInputs():	
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
	print "Specify a start date:"
	year = raw_input("... Year:  ")
	month = raw_input("... Month (01 -12):  ")
	day = raw_input("... Date:  ")
	delta = raw_input("\nDelta between days:  ")	
	iterations = raw_input("...number of dates "+str(delta)+" days in the future:  ")
	inputs = [year,month,day,delta,iterations]
	return inputs

def convertInputs(inputs):
	year = inputs[0]
	month = inputs[1]
	day = inputs[2]
	delta = inputs[3]
	iterations = inputs[4]
	
	# Convert the input date to datetime format
	dateString = year+"/"+month+"/"+day
	dt = datetime.strptime(dateString,'%Y/%m/%d').date()
	de = int(delta)
	it = int(iterations)
	
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
	cInputs = [dt,de,it]	
	return cInputs

def getDateRange(cInputs):
	dt = cInputs[0]
	de = cInputs[1]
	it = cInputs[2]
	result = [dt]
	for i in range(it):
		a = result[i]+timedelta(days=de)
		result.append(a)
	formattedArray =[result[i].strftime("%Y/%m/%d") for i in range(len(result))]
	print "\nDate range requested: "+str(formattedArray)+"\n"
	return result

def modifyOutput(result):
	prepend = raw_input("\nType anything you would like to prepend to each date string here: ")
	postpend = raw_input("\nType anything you would like to append to the end of each date string here:  ")
	format = raw_input("\nThis is where you decide on the format of the output.\n - Type `a` if you would like your results as an array.\n - Type `p` if you want them printed on seperate lines.\n - If you don't want to use this functionality you can just prese Enter/Return to skip this.  ")
	modifiedOutput = []
	for r in range(len(result)):
		mo = prepend+str(result[r])+postpend
		modifiedOutput.append(mo)
	if format=='a':
		print modifiedOutput
	elif format=='p':
		for e in range(len(modifiedOutput)):
			print str(modifiedOutput[e])
	print "\n"
	return modifiedOutput
	
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

