# Software Architecture

These are likely more than we will implement, but it should give a good idea of what kinds of data we expect.

## Data

	- user
	   - userID
	   - userName
	   - firstName
	   - lastName
	   - email
	   - password
	   - birthDate
	   - location
	   - profilePicture
	   - isLoggedIn
	   - accountCreationDate
	   - lastLoginDate
	   Relationships:
		Many-to-Many with User (Connections/Friends) - Represented by a "Connection" entity that stores the relationship between users.
		One-to-Many with Experience.
		One-to-Many with Education.
		One-to-Many with Skill.
		One-to-Many with Post.
		One-to-Many with Messages
		One-to-Many with Company.
		Many-to-Many with Group.
	- connection
	   - connectionID
	   - userID1
	   - userID2
	   - connectionDate
	   - connectionType
	- experience
	   - experienceID
	   - UserID
	   - Title
	   - Company
	   - Location
	   - EmploymentType
	   - StartDate
	   - EndDate
	   - Description
	- education
	   - EducationID
	   - UserID
	   - School
	   - Degree
	   - FieldOfStudy
	   - GraduationDate
	   - Activities
	   - Description
	- skill
	   - SkillID
	   - UserID
	   - SkillName
	   - SkillLevel
	   - EndorsementCount
	- post
	   - PostID
	   - UserID
	   - Content
	   - Timestamp
	   - Likes
	   - Comments
	   - Shares
	- company
	   - CompanyID
	   - Name
	   - Industry
	   - Size
	   - Location
	   - Description
	   - FoundedYear
	   - Website
	- group
	   - GroupID
	   - Name
	   - Description
	   - MemberCount
	   - CreatedByUserID
	   - CreatedDate
	- message
	   - MessageID
	   - SenderUserID
	   - ReceiverUserID
	   - Content
	   - Timestamp
	   - IsRead


## Views

* user: list, detail, create, update, delete
* connection: list, detail, create, update, delete
* experience: list, detail, create, update, delete
* education: list, detail, create, update, delete
* skill: list, detail, create, update, delete
* post: list, detail, create, update, delete
* company: list, detail, create, update, delete
* group: list, detail, create, update, delete
* message: list, detail, create, update, delete

## Tests

We will develop tests for each of the functions listed in the views.