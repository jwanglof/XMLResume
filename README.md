XMLResume
=========

Create a beautifully-looking resume from an XML-file

======

### Information about you:
```
<userInformation>
	<name>Your name</name>
	<phonenumber>070-86 01 911</phonenumber>
	<lastUpdated>2014-01-23</lastUpdated>
</userInformation>
```

### Information about your work-related skills
```
<companyTitle>Company title</companyTitle>
<companyLocation>Company location</companyLocation>
<startDate>When I begun at the company (date-format)</startDate>
<endDate>When I quit the company (date-format)</endDate>
<jobTitle>Job title</jobTitle>
<jobDescription>Job description</jobDescription>
```

### Information about your education
```
<educationName>Name of the education</educationName>
<educationLocation>Education location</educationLocation>
<educationStart>Start date of the education (date-format)</educationStart>
<educationEnd>End date of the education (date-format)</educationEnd>
```
##### Optional
```
<educationCourse>Add a course on the education. Can be used multiple times</educationCourse>
```

### Information about other skills
```
<skillName>Name of the skill</skillName>
<skillLocation>Skill location</skillLocation>
<skillTitle>Skill title</skillTitle>
<skillDescription>Skill description</skillDescription>
```
##### Optional
```
<skillStart>Start date (date-format)</skillStart>
<skillEnd>End date (date-format)</skillEnd>
```

## Specified formats
#### Date-format
* YYYY-MM-DD
* YYYY-MM
* YY-MM