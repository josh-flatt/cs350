from django.db import models

class User(models.Model):
    userID = models.AutoField(primary_key=True)
    userName = models.CharField(max_length=100)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    birthDate = models.DateField()
    location = models.CharField(max_length=100)
    profilePicture = models.CharField(max_length=100)
    isLoggedIn = models.BooleanField(default=False)
    accountCreationDate = models.DateTimeField(auto_now_add=True)
    lastLoginDate = models.DateTimeField(auto_now=True)

    # Should these connections all be symmetrical?
    userConnections = models.ManyToManyField('self', through='UserConnection', symmetrical=True)
    groupConnections = models.ManyToManyField('self', through='GroupConnection', symmetrical=True)
    # Add other one-to-many relationships as needed
    # One-to-Many with Experience
    # One-to-Many with Education
    # One-to-Many with Skill
    # One-to-Many with Post
    # One-to-Many with Message
    # One-to-Many with Company
    # Many-to-Many with Group

    def __str__(self):
        return self.userName

# Should Companies connect with Users through groups?
class Group(models.Model):
    groupID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    memberCount = models.PositiveIntegerField()
    createdByUserID = models.ForeignKey(User, on_delete=models.CASCADE)
    createdDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class UserConnection(models.Model):
    connectionID = models.AutoField(primary_key=True)
    userID1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user1ID')
    userID2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user2ID')
    connectionDate = models.DateTimeField(auto_now_add=True)
    connectionType = models.CharField(max_length=50)

    def __str__(self):
        return f"Connection between {self.userID1} and {self.userID2}"

class GroupConnection(models.Model):
    connectionID = models.AutoField(primary_key=True)
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    groupID = models.ForeignKey(Group, on_delete=models.CASCADE)
    connectionDate = models.DateTimeField(auto_now_add=True)
    connectionType = models.CharField(max_length=50)

    def __str__(self):
        return f"Connection between {self.userID} and {self.groupID}"

class Experience(models.Model):
    experienceID = models.AutoField(primary_key=True)
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    employmentType = models.CharField(max_length=50)
    startDate = models.DateField()
    endDate = models.DateField(null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.title} at {self.company}"

class Education(models.Model):
    educationID = models.AutoField(primary_key=True)
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    school = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    fieldOfStudy = models.CharField(max_length=100)
    graduationDate = models.DateField()
    activities = models.TextField()
    description = models.TextField()

    def __str__(self):
        return f"{self.degree} in {self.fieldOfStudy} at {self.school}"

class Skill(models.Model):
    skillID = models.AutoField(primary_key=True)
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    skillName = models.CharField(max_length=100)
    skillLevel = models.CharField(max_length=50)
    endorsementCount = models.PositiveIntegerField()

    def __str__(self):
        return self.skillName

class Post(models.Model):
    postID = models.AutoField(primary_key=True)
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    likes = models.PositiveIntegerField(default=0)
    comments = models.PositiveIntegerField(default=0)
    shares = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Post by {self.userID}: {self.content[:50]}"

class Company(models.Model):
    companyID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    industry = models.CharField(max_length=100)
    size = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    description = models.TextField()
    foundedYear = models.PositiveIntegerField()
    website = models.URLField()

    def __str__(self):
        return self.name

class Message(models.Model):
    messageID = models.AutoField(primary_key=True)
    senderUserID = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    receiverUserID = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    isRead = models.BooleanField(default=False)

    def __str__(self):
        return f"Message from {self.senderUserID} to {self.receiverUserID}: {self.content[:50]}"