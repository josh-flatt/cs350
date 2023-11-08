from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse_lazy

class AppUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, editable=False)

    accountCreationDate = models.DateTimeField(auto_now_add=True)

    # Should these connections all be symmetrical?
    userConnections = models.ManyToManyField('self', through='UserConnection', symmetrical=True, editable=False)
    userGroupConnections = models.ManyToManyField('self', through='UserGroupConnection', symmetrical=True, editable=False)

    # One-to-Many with Post
    # One-to-Many with Message

    def __str__(self):
        return f'{self.user.username}'
    
    def get_absolute_url(self):
        return reverse_lazy('user_detail', args=[str(self.id)])
    
    @property
    def name(self):
        return self.user.first_name + ' ' + self.user.last_name
    
    @staticmethod
    def get_me(user):
        return AppUser.objects.get_or_create(user=user)[0]
    
    def save(self,*args,**kwargs):
        created = not self.pk
        super().save(*args,**kwargs)
        if created:
            Profile.objects.create(appuser=self)

class Profile(models.Model):
    appuser = models.OneToOneField(AppUser, on_delete=models.CASCADE, related_name='appuser', editable=False)

    firstName = models.CharField(max_length=50, null=True)
    lastName = models.CharField(max_length=50, null=True)
    birthDate = models.DateField(null=True)
    location = models.CharField(max_length=150, null=True)
    email = models.CharField(max_length=200, null=True)
    profilePicture = models.CharField(max_length=200, null=True)
    
    # Add other one-to-many relationships as needed
    # Add in foreign key fields on the many side and define property here
    # One-to-Many with Education
    # One-to-Many with Skill

    # One-to-Many with Company

    def __str__(self):
        return f'Profile of {self.appuser.user.username}'
    
    def get_absolute_url(self):
        return reverse_lazy('profile_detail', args=[str(self.id)])
    
    @property
    def name(self):
        return 'Profile of ' + self.appuser
    
    @property
    def posts(self):
        return Post.objects.filter(profile=self)
    
    @property
    def experiences(self):
        return Experience.objects.filter(profile=self)
    
    @property
    def educations(self):
        return Education.objects.filter(profile=self)
    
    @property
    def skills(self):
        return Skill.objects.filter(profile=self)
    
    @staticmethod
    def get_me(appuser):
        return Profile.objects.get_or_create(appuser=appuser)[0]

# Should Companies connect with Users through groups?
class UserGroup(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    memberCount = models.PositiveIntegerField()
    createdByUserID = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    createdDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class UserConnection(models.Model):
    connectionID = models.AutoField(primary_key=True)
    userID1 = models.ForeignKey(AppUser, on_delete=models.CASCADE, related_name='user1ID')
    userID2 = models.ForeignKey(AppUser, on_delete=models.CASCADE, related_name='user2ID')
    connectionDate = models.DateTimeField(auto_now_add=True)
    connectionType = models.CharField(max_length=50)

    def __str__(self):
        return f"Connection between {self.userID1} and {self.userID2}"

class UserGroupConnection(models.Model):
    connectionID = models.AutoField(primary_key=True)
    userID = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    userGroupID = models.ForeignKey(UserGroup, on_delete=models.CASCADE)
    connectionDate = models.DateTimeField(auto_now_add=True)
    connectionType = models.CharField(max_length=50)

    def __str__(self):
        return f"Connection between {self.userID} and {self.userGroupID}"

class Experience(models.Model):
    experienceID = models.AutoField(primary_key=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, editable=False)
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    employmentType = models.CharField(max_length=100)
    startDate = models.DateField()
    endDate = models.DateField(null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.title} at {self.company}"

class Education(models.Model):
    educationID = models.AutoField(primary_key=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, editable=False)
    school = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    fieldOfStudy = models.CharField(max_length=200)
    graduationDate = models.DateField()
    activities = models.TextField()
    description = models.TextField()

    def __str__(self):
        return f"{self.degree} in {self.fieldOfStudy} at {self.school}"

class Skill(models.Model):
    skillID = models.AutoField(primary_key=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, editable=False)
    skillName = models.CharField(max_length=100)
    skillLevel = models.CharField(max_length=50)
    endorsementCount = models.PositiveIntegerField(default=0, editable=False)

    def __str__(self):
        return self.skillName

class Post(models.Model):
    postID = models.AutoField(primary_key=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, editable=False)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Post by {self.profile.appuser.user.username}: {self.content[:50]}"

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
    senderUserID = models.ForeignKey(AppUser, on_delete=models.CASCADE, related_name='sent_messages')
    receiverUserID = models.ForeignKey(AppUser, on_delete=models.CASCADE, related_name='received_messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    isRead = models.BooleanField(default=False)

    def __str__(self):
        return f"Message from {self.senderUserID} to {self.receiverUserID}: {self.content[:50]}"