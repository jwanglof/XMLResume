# from datetime import date, time
import datetime
import os

class HTMLOutput:
	outputFilename = ""
	templateFile = ""
	rootDir = ""

	openedFile = ""
	outputFile = ""

	informationTags = ["fullName", "phonenumber", "email", "lastUpdated"]
	information = ""

	workInformationTags = ["companyTitle", "companyLocation", "startDate", "endDate", "jobTitle", "jobDescription"]
	workInformation = ""

	def __init__(self, outputFilename=None, templateFile=None):
		rootDir = os.getcwd()

		self.outputFilename = rootDir +"/output_html/user_created/"

		if (outputFilename == None):
			separator = "-"

			now = datetime.datetime.now()
			dateFilename = [str(now.date()), str(now.hour), str(now.minute)]
			
			self.outputFilename += separator.join(dateFilename)
		else:
			self.outputFilename += outputFilename

		# Sef a default template file
		templateFile = rootDir +"/output_html/templates/basic_template.html"
		if (templateFile != None):
			templateFile = templateFile

		self.openedFile = open(templateFile, "r", encoding="utf-8").readlines()
		self.outputFile = open(self.outputFilename, "w", encoding="utf-8")

	def __del__(self):
		self.outputFile.close()

	def addInformation(self, information):
		for tag in self.informationTags:
			self.openedFile = [s.replace(tag, information[tag]) for s in self.openedFile]

	def addWorkInformation(self, information):
		print(information)

	def write(self):
		for row in self.openedFile:
			self.outputFile.write(row)