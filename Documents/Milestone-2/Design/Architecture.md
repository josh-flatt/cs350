# Software Architecture

These are likely more entities and attributes than we will implement, but it should give a good idea of what kinds of data we expect to see in the app.

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
		Many-to-Many with User (Connections/Friends) - Represented by a "Connection" entity.
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
	   - userID
	   - title
	   - company
	   - location
	   - employmentType
	   - startDate
	   - endDate
	   - description
	- education
	   - educationID
	   - userID
	   - school
	   - degree
	   - fieldOfStudy
	   - graduationDate
	   - activities
	   - description
	- skill
	   - skillID
	   - userID
	   - skillName
	   - skillLevel
	   - endorsementCount
	- post
	   - postID
	   - userID
	   - content
	   - timestamp
	   - likes
	   - comments
	   - shares
	- company
	   - companyID
	   - name
	   - industry
	   - size
	   - location
	   - description
	   - foundedYear
	   - website
	- group
	   - groupID
	   - name
	   - description
	   - memberCount
	   - createdByUserID
	   - createdDate
	- message
	   - messageID
	   - senderUserID
	   - receiverUserID
	   - content
	   - timestamp
	   - isRead


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

We will develop automated tests for each of the CRUD functions listed in the views section. We will also develop automatic tests for any other utility functions that are required.