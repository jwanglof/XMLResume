#!/usr/bin/python

import sys
from XMLResume import XMLResume
from HTMLOutput import HTMLOutput

if __name__ == '__main__':
	# Check that an argument is present
	# If it is, check that the first argument is an XML-file
	# Else just return an error message
	if (len(sys.argv) == 1):
		print("NEJ")
	elif (sys.argv[1][-3:] == "xml"):
		# Set which XML file to read
		resume = XMLResume(sys.argv[1])

		# Get all the information that will populate the resume
		resume.setUserInformation()
		resume.setWorkInformation()
		resume.setEducationInformation()
		resume.setSkillInformation()

		# print(resume.getUserInformation())
		# print(resume.getWorkInformation())
		# print(resume.getEducationInformation())
		# print(resume.getSkillInformation())

		htmlOutput = HTMLOutput()
	else:
		print("The first argument needs to be an XML-file!")