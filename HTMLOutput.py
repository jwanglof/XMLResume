# from datetime import date, time
import datetime

class HTMLOutput:
	filename = ""

	def __init__(self, filename=None):
		if (filename == None):
			separator = "-"

			now = datetime.datetime.now()
			dateFilename = [str(now.date()), str(now.hour), str(now.minute)]
			
			self.filename = separator.join(dateFilename)
		else:
			self.filename = filename

	def populateCompanyTable(self):
		return