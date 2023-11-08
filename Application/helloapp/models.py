from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse_lazy

class AppUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, editable=False)

    accountCreationDate = models.DateTimeField(auto_now_add=True)

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
    appuser = models.OneToOneField(AppUser, on_delete=models.CASCADE, editable=False)

    firstName = models.CharField(max_length=50, null=True)
    lastName = models.CharField(max_length=50, null=True)
    birthDate = models.DateField(null=True)
    location = models.CharField(max_length=150, null=True)
    email = models.CharField(max_length=200, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)

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
    
    @property
    def following_profiles(self):
        """
        Get the list of profiles that the current profile is following.
        """
        follow_objects = Follow.objects.filter(follower=self)
        return [follow_object.following for follow_object in follow_objects]
    
    @property
    def follower_profiles(self):
        """
        Get the list of profiles that are following the current profile.
        """
        follow_objects = Follow.objects.filter(following=self)
        return [follow_object.follower for follow_object in follow_objects]

    @staticmethod
    def get_me(appuser):
        return Profile.objects.get_or_create(appuser=appuser)[0]

class Follow(models.Model):
    follower = models.ForeignKey(Profile, related_name='following', on_delete=models.CASCADE)
    following = models.ForeignKey(Profile, related_name='followers', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('follower', 'following')

    def __str__(self):
        return f'{self.follower} follows {self.following}'

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
    
    