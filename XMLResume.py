import xml.etree.ElementTree as ET

class XMLResume:
	filename = ""
	tree = ""
	root = ""

	userInformation = {}
	workInformation = {}
	educationInformation = {}
	skillInformation = {}

	def __init__(self, filename):
		self.filename = filename
		self.tree = ET.parse(filename)
		self.root = self.tree.getroot()

	def setUserInformation(self):
		userInfo = self.root.find("userInformation")

		self.userInformation["name"] = userInfo.find("name").text
		self.userInformation["phonenumber"] = userInfo.find("phonenumber").text
		self.userInformation["lastUpdated"] = userInfo.find("lastUpdated").text

	def getUserInformation(self):
		return self.userInformation

	def setWorkInformation(self):
		workRoot = self.root.find("workInformation")

		companyNr = 0
		for company in workRoot.findall("company"):
			companyDict = {}
			
			companyDict["companyTitle"] = company.find("companyTitle").text
			companyDict["companyLocation"] = company.find("companyLocation").text
			companyDict["startDate"] = company.find("startDate").text
			companyDict["endDate"] = company.find("endDate").text
			companyDict["jobTitle"] = company.find("jobTitle").text
			companyDict["jobDescription"] = company.find("jobDescription").text

			self.workInformation[companyNr] = companyDict
			
			companyNr += 1

	def getWorkInformation(self):
		return self.workInformation

	def setEducationInformation(self):
		educationRoot = self.root.find("educationInformation")

		educationNr = 0
		for education in educationRoot.findall("education"):
			educationDict = {}

			educationDict["educationName"] = education.find("educationName").text
			educationDict["educationLocation"] = education.find("educationLocation").text
			educationDict["educationStart"] = education.find("educationStart").text
			educationDict["educationEnd"] = education.find("educationEnd").text

			if (education.find("educationCourse") != None):
				courseList = []
				for course in education.findall("educationCourse"):
					courseList.append(course.text)
				educationDict["educationCourse"] = courseList

			self.educationInformation[educationNr] = educationDict

			educationNr += 1

	def getEducationInformation(self):
		return self.educationInformation

	def setSkillInformation(self):
		skillRoot = self.root.find("skillInformation")

		skillNr = 0
		for skill in skillRoot.findall("skill"):
			skillDict = {}

			skillDict["skillName"] = skill.find("skillName").text
			skillDict["skillLocation"] = skill.find("skillLocation").text
			skillDict["skillTitle"] = skill.find("skillTitle").text
			skillDict["skillDescription"] = skill.find("skillDescription").text

			if (skill.find("skillStart") != None):
				skillDict["skillStart"] = skill.find("skillStart").text
			if (skill.find("skillEnd") != None):
				skillDict["skillEnd"] = skill.find("skillEnd").text

			self.skillInformation[skillNr] = skillDict

			skillNr =+ 1

	def getSkillInformation(self):
		return self.skillInformation