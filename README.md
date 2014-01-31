XMLResume
=========

Create a beautifully-looking resume from an XML-file

======

### Information about you:
```
<userInformation>
	<name>Your name</name>
	<phonenumber>004670-86 01 911</phonenumber>
	<email>jwanglof@gmail.com</email>
	<lastUpdated>2014-01-23</lastUpdated>
	<resumeLanguage>English</resumeLanguage>
</userInformation>
```

### Information about your work-related skills
```
<workInformation>
	<company>
		<companyTitle>Company title</companyTitle>
		<companyLocation>Company location</companyLocation>
		<startDate>When I begun at the company (date-format)</startDate>
		<endDate>When I quit the company (date-format)</endDate>
		<jobTitle>Job title</jobTitle>
		<jobDescription>Job description</jobDescription>
	</company>
</workInformation>
```

### Information about your education
```
<educationInformation>
	<education>
		<educationName>Name of the education</educationName>
		<educationLocation>Education location</educationLocation>
		<educationStart>Start date of the education (date-format)</educationStart>
		<educationEnd>End date of the education (date-format)</educationEnd>
		<educationCourse>#OPTIONAL# Add a course on the education. Can be used multiple times</educationCourse>
	</education>
</educationInformation>
```

### Information about other skills
```
<skillInformation>
	<skill>
		<skillName>Name of the skill</skillName>
		<skillLocation>Skill location</skillLocation>
		<skillTitle>Skill title</skillTitle>
		<skillDescription>Skill description</skillDescription>
		<skillStart>#OPTIONAL# Start date (date-format)</skillStart>
		<skillEnd>#OPTIONAL# End date (date-format)</skillEnd>
	</skill>
</skillInformation>
```

## Specified formats
#### Date-format
* YYYY-MM-DD
* YYYY-MM
* YY-MM