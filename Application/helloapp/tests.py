from django.test import TestCase
from django.urls import reverse
import datetime
from .models import AppUser, Profile, Follow, Experience, Education, Skill, Post
from django.contrib.auth.models import User
from django.urls import reverse
from .views_functions import get_appuser, get_profile, IsUserRecordMixin, IsUserProfileMixin, IsUserPostMixin, IsUserProfileFromExpMixin, IsUserProfileFromEduMixin, IsUserProfileFromSkillMixin
from django.http import HttpRequest
from .models import AppUser

'''python3 manage.py test'''

class ModelTestCase(TestCase):
    def setUp(self):
        # Create a User
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_appuser_creation(self):
        app_user = AppUser.get_me(self.user)
        self.assertEqual(app_user.name, ' ')
        self.assertEqual(app_user.get_absolute_url(), reverse('user_detail', args=[str(app_user.id)]))

    def test_profile_creation(self):
        app_user = AppUser.get_me(self.user)
        profile = Profile.get_me(app_user)
        self.assertEqual(str(profile), f'Profile of {app_user.user.username}')
        self.assertEqual(profile.get_absolute_url(), reverse('profile_detail', args=[str(profile.id)]))

    def test_follow_model(self):
        app_user = AppUser.get_me(self.user)
        profile = Profile.get_me(app_user)
        user2 = User.objects.create_user(username='testuser2', password='testpassword2')
        app_user2 = AppUser.get_me(user2)
        profile2 = Profile.get_me(app_user2)
        follower = profile
        following = profile2
        follow = Follow.objects.create(follower=follower, following=following)
        self.assertEqual(str(follow), f'{follower} follows {following}')

    def test_experience_model(self):
        app_user = AppUser.get_me(self.user)
        profile = Profile.get_me(app_user)
        experience = Experience.objects.create(
            profile=profile,
            title='Software Engineer',
            company='Example Corp',
            location='Example City',
            employmentType='Full-time',
            startDate='2020-01-01',
            endDate='2022-12-31',
            description='Worked on various projects.'
        )
        self.assertEqual(str(experience), f"Software Engineer at Example Corp")

    def test_education_model(self):
        app_user = AppUser.get_me(self.user)
        profile = Profile.get_me(app_user)
        education = Education.objects.create(
            profile=profile,
            school='Example University',
            degree='Bachelor of Science',
            fieldOfStudy='Computer Science',
            graduationDate='2019-05-15',
            activities='Participated in clubs and organizations.',
            description='Studied computer science and mathematics.'
        )
        self.assertEqual(str(education), f"Bachelor of Science in Computer Science at Example University")

    def test_skill_model(self):
        app_user = AppUser.get_me(self.user)
        profile = Profile.get_me(app_user)
        skill = Skill.objects.create(
            profile=profile,
            skillName='Python',
            skillLevel='Advanced',
            endorsementCount=10
        )
        self.assertEqual(str(skill), 'Python')

    def test_post_model(self):
        app_user = AppUser.get_me(self.user)
        profile = Profile.get_me(app_user)
        post = Post.objects.create(
            profile=profile,
            content='This is a test post.',
        )
        self.assertEqual(str(post), f"Post by {profile.appuser.user.username}: This is a test post.")

class ViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.appuser = AppUser.get_me(self.user)
        self.profile = Profile.get_me(self.appuser)

    def test_user_add_view(self):
        url = reverse('user_add')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_profile_update_view(self):
        url = reverse('profile_edit', args=[str(self.profile.pk)])
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_experience_add_view(self):
        url = reverse('experience_add')
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_education_add_view(self):
        url = reverse('education_add')
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_skill_add_view(self):
        url = reverse('skill_add')
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_post_add_view(self):
        url = reverse('post_add')
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

class ViewFunctionTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.appuser = AppUser.get_me(self.user)
        self.profile = Profile.get_me(self.appuser)
    
    def test_hello_view(self):
        response = self.client.get(reverse('hello_view'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'helloView.html')
    
    def test_get_appuser(self):
        appuser = get_appuser(self.user)
        self.assertEqual(appuser.user, self.user)
    
    def test_get_profile(self):
        profile = get_profile(self.appuser)
        self.assertEqual(profile.appuser, self.appuser)

class MixinTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.appuser = AppUser.get_me(self.user)
        self.profile = Profile.get_me(self.appuser)
        self.post = Post.objects.create(profile=self.profile, content='Test Post Content')
        self.experience = Experience.objects.create(profile=self.profile, title='Test Title', company='Test Company', location='Test Location', employmentType='Full-Time', startDate='2023-01-01', description='Test Description')
        self.education = Education.objects.create(profile=self.profile, school='Test School', degree='Test Degree', fieldOfStudy='Test Field', graduationDate='2023-01-01', activities='Test Activities', description='Test Description')
        self.skill = Skill.objects.create(profile=self.profile, skillName='Test Skill', skillLevel='Intermediate')

    def test_is_user_record_mixin(self):
        request = HttpRequest()
        request.user = self.user
        kwargs = {'pk': self.user.pk}
        mixin = IsUserRecordMixin()
        mixin.request = request
        mixin.kwargs = kwargs

        self.assertTrue(mixin.test_func())

    def test_is_user_profile_mixin(self):
        request = HttpRequest()
        request.user = self.user
        kwargs = {'pk': self.profile.pk}
        mixin = IsUserProfileMixin()
        mixin.request = request
        mixin.kwargs = kwargs

        self.assertTrue(mixin.test_func())

    def test_is_user_post_mixin(self):
        request = HttpRequest()
        request.user = self.user
        kwargs = {'pk': self.post.pk}
        mixin = IsUserPostMixin()
        mixin.request = request
        mixin.kwargs = kwargs

        self.assertTrue(mixin.test_func())

    def test_is_user_profile_from_exp_mixin(self):
        request = HttpRequest()
        request.user = self.user
        kwargs = {'pk': self.experience.pk}
        mixin = IsUserProfileFromExpMixin()
        mixin.request = request
        mixin.kwargs = kwargs

        self.assertTrue(mixin.test_func())

    def test_is_user_profile_from_edu_mixin(self):
        request = HttpRequest()
        request.user = self.user
        kwargs = {'pk': self.education.pk}
        mixin = IsUserProfileFromEduMixin()
        mixin.request = request
        mixin.kwargs = kwargs

        self.assertTrue(mixin.test_func())

    def test_is_user_profile_from_skill_mixin(self):
        request = HttpRequest()
        request.user = self.user
        kwargs = {'pk': self.skill.pk}
        mixin = IsUserProfileFromSkillMixin()
        mixin.request = request
        mixin.kwargs = kwargs

        self.assertTrue(mixin.test_func())