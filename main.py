#!/usr/bin/python

import sys
from XMLResume import XMLResume
from HTMLOutput import HTMLOutput

if __name__ == '__main__':
	# Check that an argument is present
	# If it is, check that the first argument is an XML-file
	# Else just return an error message
	if (len(sys.argv) == 1):
		print("Error: You need to at least specify which XML file to read your resume from.")
		print("Hint, type python main.py help to see the supported commands.")
	elif (sys.argv[1] == "help"):
		print("usage: python <XMLResume.xml> [htmlOutputFile.<html/htm>] [templateFile.<html/htm>]")
	elif (sys.argv[1][-3:] == "xml"):
		htmlOutputFile = None
		templateFile = None

		# Check if the user specified an output HTML file
		if (len(sys.argv) == 3):
			htmlOutputFile = sys.argv[2]

		#  Check if the user specified a template file
		if (len(sys.argv) == 4):
			templateFile = sys.argv[3]

		# Set which XML file to read
		resume = XMLResume(sys.argv[1])

		# Get all the information that will populate the resume
		resume.setInformation()
		resume.setWorkInformation()
		resume.setEducationInformation()
		resume.setSkillInformation()

		# print(resume.getInformation())
		# print(resume.getWorkInformation())
		# print(resume.getEducationInformation())
		# print(resume.getSkillInformation())

		htmlOutput = HTMLOutput(htmlOutputFile, templateFile)
		htmlOutput.addInformation(resume.getInformation())
		htmlOutput.addWorkInformation(resume.getWorkInformation())
		htmlOutput.write()
	else:
		print("The first argument needs to be an XML-file!")