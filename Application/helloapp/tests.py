from django.test import TestCase
from django.urls import reverse
import datetime

from .models import AppUser

'''python3 manage.py test'''

class AppUserModelTestCase(TestCase):
    def setUp(self):
        # Create a sample user for testing
        self.user = AppUser.objects.create(
            userName='testuser',
            firstName='John',
            lastName='Doe',
            email='test@example.com',
            birthDate='1990-01-01',
            location='Test Location',
            profilePicture='/static/profileImages/robot.jpg',
            isLoggedIn=False,
        )

    def test_user_creation(self):
        """
        Test that a user can be created with valid data.
        """
        self.assertEqual(AppUser.objects.count(), 1)
        saved_user = AppUser.objects.first()
        self.assertEqual(saved_user.userName, 'testuser')
        self.assertEqual(saved_user.firstName, 'John')
        self.assertEqual(saved_user.lastName, 'Doe')
        self.assertEqual(saved_user.email, 'test@example.com')
        self.assertEqual(saved_user.birthDate, datetime.date(1990, 1, 1))
        self.assertEqual(saved_user.location, 'Test Location')
        self.assertEqual(saved_user.profilePicture, '/static/profileImages/robot.jpg')
        self.assertFalse(saved_user.isLoggedIn)

    def test_user_str_representation(self):
        """
        Test the __str__ method of the user model.
        """
        self.assertEqual(str(self.user), 'testuser')

class UserTests(TestCase):
    def test_CreateUser(self):
        user_data = {
            'userName': 'testuser',
            'firstName': 'John',
            'lastName': 'Doe',
            'email': 'testuser@example.com',
            'birthDate': '2000-01-01',
            'location': 'Somewhere',
            'profilePicture': 'profile.jpg',
            'isLoggedIn': True,
        }

        user = AppUser.objects.create(**user_data)

        self.assertIsNotNone(user)

        created_user = AppUser.objects.get(userName='testuser')
        self.assertIsNotNone(created_user)
        self.assertEqual(created_user.userName, 'testuser')
        self.assertEqual(created_user.email, 'testuser@example.com')

    def test_ReadUser(self):
        user = AppUser.objects.create(
            userName='getuser',
            firstName='Alice',
            lastName='Smith',
            email='getuser@example.com',
            birthDate='1995-10-20',
            location='Townsville',
            profilePicture='profile2.jpg',
            isLoggedIn=True,
        )

        retrieved_user = AppUser.objects.get(userName='getuser')

        self.assertEqual(retrieved_user.userName, 'getuser')
        self.assertEqual(retrieved_user.email, 'getuser@example.com')

    def test_UpdateUser(self):
        user = AppUser.objects.create(
            userName='changeuser',
            firstName='Mark',
            lastName='Wilson',
            email='changeuser@example.com',
            birthDate='1995-08-10',
            location='Countrytown',
            profilePicture='profile4.jpg',
            isLoggedIn=True,
        )

        updated_data = {
            'userName': 'changeuser',
            'firstName': 'NewName',
            'email': 'newemail@example.com',
        }

        user_to_update = AppUser.objects.get(userName='changeuser')
        for key, value in updated_data.items():
            setattr(user_to_update, key, value)
        user_to_update.save()

        updated_user = AppUser.objects.get(userName='changeuser')

        self.assertEqual(updated_user.firstName, 'NewName')
        self.assertEqual(updated_user.email, 'newemail@example.com')

    def test_DeleteUser(self):
        user = AppUser.objects.create(
            userName='deleteuser',
            firstName='Eva',
            lastName='Brown',
            email='deleteuser@example.com',
            birthDate='2001-03-30',
            location='Villageville',
            profilePicture='profile3.jpg',
            isLoggedIn=True,
        )

        user_to_delete = AppUser.objects.get(userName='deleteuser')
        user_to_delete.delete()

        with self.assertRaises(AppUser.DoesNotExist):
            deleted_user = AppUser.objects.get(userName='deleteuser')

class DatabaseUnitTests(TestCase):
    def test_CreateUser1(self):
        user_data = {
            'userName': 'user1',
            'firstName': 'John',
            'lastName': 'Doe',
            'email': 'user1@example.com',
            'birthDate': '1990-05-15',
            'location': 'Cityville',
            'profilePicture': 'profile1.jpg',
        }


        user = AppUser.objects.create(**user_data)

        self.assertIsNotNone(user)

        created_user = AppUser.objects.get(userName='user1')
        self.assertIsNotNone(created_user)
        self.assertEqual(created_user.userName, 'user1')
        self.assertEqual(created_user.email, 'user1@example.com')

    def test_CreateUser2(self):
        user_data = {
            'userName': 'user2',
            'firstName': 'Alice',
            'lastName': 'Smith',
            'email': 'user2@example.com',
            'birthDate': '1985-10-20',
            'location': 'Townsville',
            'profilePicture': 'profile2.jpg',
        }


        user = AppUser.objects.create(**user_data)

        self.assertIsNotNone(user)

        created_user = AppUser.objects.get(userName='user2')
        self.assertIsNotNone(created_user)
        self.assertEqual(created_user.userName, 'user2')
        self.assertEqual(created_user.email, 'user2@example.com')

    def test_CreateUser3(self):
        user_data = {
            'userName': 'user3',
            'firstName': 'Eva',
            'lastName': 'Brown',
            'email': 'eva@example.com',
            'birthDate': '2001-03-30',
            'location': 'Villageville',
            'profilePicture': 'profile3.jpg',
        }


        user = AppUser.objects.create(**user_data)

        self.assertIsNotNone(user)

        created_user = AppUser.objects.get(userName='user3')
        self.assertIsNotNone(created_user)
        self.assertEqual(created_user.userName, 'user3')
        self.assertEqual(created_user.email, 'eva@example.com')

    def test_CreateUser4(self):
        user_data = {
            'userName': 'user4',
            'firstName': 'Mark',
            'lastName': 'Wilson',
            'email': 'user4@example.com',
            'birthDate': '1995-08-10',
            'location': 'Countrytown',
            'profilePicture': 'profile4.png',
        }


        user = AppUser.objects.create(**user_data)

        self.assertIsNotNone(user)

        created_user = AppUser.objects.get(userName='user4')
        self.assertIsNotNone(created_user)
        self.assertEqual(created_user.userName, 'user4')
        self.assertEqual(created_user.email, 'user4@example.com')

    def test_CreateUser5(self):
        user_data = {
            'userName': 'user5',
            'firstName': 'Laura',
            'lastName': 'Johnson',
            'email': 'user5@example.com',
            'birthDate': '1988-12-05',
            'location': 'Hometown',
            'profilePicture': 'profile5.jpg',
        }


        user = AppUser.objects.create(**user_data)

        self.assertIsNotNone(user)

        created_user = AppUser.objects.get(userName='user5')
        self.assertIsNotNone(created_user)
        self.assertEqual(created_user.userName, 'user5')
        self.assertEqual(created_user.email, 'user5@example.com')

    def test_CreateUser6(self):
        user_data = {
            'userName': 'user6',
            'firstName': 'Michael',
            'lastName': 'Williams',
            'email': 'user6@example.com',
            'birthDate': '2000-04-25',
            'location': 'Suburbia',
            'profilePicture': 'profile6.jpg',
            'isLoggedIn': False,
        }


        user = AppUser.objects.create(**user_data)

        self.assertIsNotNone(user)

        created_user = AppUser.objects.get(userName='user6')
        self.assertIsNotNone(created_user)
        self.assertEqual(created_user.userName, 'user6')
        self.assertEqual(created_user.email, 'user6@example.com')

    def test_CreateUser7(self):
        user_data = {
            'userName': 'user7',
            'firstName': 'Sophia',
            'lastName': 'Brown',
            'email': 'sophia@example.com',
            'birthDate': '1992-06-15',
            'location': 'Seaside',
            'profilePicture': 'avatar7.jpg',
        }


        user = AppUser.objects.create(**user_data)

        self.assertIsNotNone(user)

        created_user = AppUser.objects.get(userName='user7')
        self.assertIsNotNone(created_user)
        self.assertEqual(created_user.userName, 'user7')
        self.assertEqual(created_user.email, 'sophia@example.com')

    def test_CreateUser8(self):
        user_data = {
            'userName': 'user8',
            'firstName': 'Robert',
            'lastName': 'Miller',
            'email': 'user8@example.com',
            'birthDate': '1979-11-30',
            'location': 'Mountainview',
            'profilePicture': 'profile8.jpg',
        }


        user = AppUser.objects.create(**user_data)

        self.assertIsNotNone(user)

        created_user = AppUser.objects.get(userName='user8')
        self.assertIsNotNone(created_user)
        self.assertEqual(created_user.userName, 'user8')
        self.assertEqual(created_user.email, 'user8@example.com')

    def test_CreateUser9(self):
        user_data = {
            'userName': 'user9',
            'firstName': 'Olivia',
            'lastName': 'Jones',
            'email': 'user9@example.com',
            'birthDate': '1999-02-20',
            'location': 'Countryside',
            'profilePicture': 'profile9.jpg',
        }


        user = AppUser.objects.create(**user_data)

        self.assertIsNotNone(user)

        created_user = AppUser.objects.get(userName='user9')
        self.assertIsNotNone(created_user)
        self.assertEqual(created_user.userName, 'user9')
        self.assertEqual(created_user.email, 'user9@example.com')

    def test_CreateUser10(self):
        user_data = {
            'userName': 'user10',
            'firstName': '',
            'lastName': '',
            'email': 'user10@example.com',
            'birthDate': '2003-07-10',
            'location': '',
            'profilePicture': '',
        }


        user = AppUser.objects.create(**user_data)

        self.assertIsNotNone(user)

        created_user = AppUser.objects.get(userName='user10')
        self.assertIsNotNone(created_user)
        self.assertEqual(created_user.userName, 'user10')
        self.assertEqual(created_user.email, 'user10@example.com')

    def test_CreateUser11(self):
        user_data = {
            'userName': 'user11',
            'firstName': 'Emily',
            'lastName': 'Davis',
            'email': 'user11@example.com',
            'birthDate': '1994-09-20',
            'location': 'Lakeview',
            'profilePicture': 'profile11.jpg',
        }


        user = AppUser.objects.create(**user_data)

        self.assertIsNotNone(user)

        created_user = AppUser.objects.get(userName='user11')
        self.assertIsNotNone(created_user)
        self.assertEqual(created_user.userName, 'user11')
        self.assertEqual(created_user.email, 'user11@example.com')

    def test_CreateUser12(self):
        user_data = {
            'userName': 'user12',
            'firstName': 'James',
            'lastName': 'Wilson',
            'email': 'james@example.com',
            'birthDate': '1991-04-15',
            'location': 'Cityscape',
            'profilePicture': 'profile12.jpg',
        }


        user = AppUser.objects.create(**user_data)

        self.assertIsNotNone(user)

        created_user = AppUser.objects.get(userName='user12')
        self.assertIsNotNone(created_user)
        self.assertEqual(created_user.userName, 'user12')
        self.assertEqual(created_user.email, 'james@example.com')

    def test_CreateUser13(self):
        user_data = {
            'userName': 'user13',
            'firstName': 'Isabella',
            'lastName': 'Anderson',
            'email': 'user13@example.com',
            'birthDate': '2002-11-30',
            'location': 'Urbanville',
            'profilePicture': 'profile13.jpg',
        }


        user = AppUser.objects.create(**user_data)

        self.assertIsNotNone(user)

        created_user = AppUser.objects.get(userName='user13')
        self.assertIsNotNone(created_user)
        self.assertEqual(created_user.userName, 'user13')
        self.assertEqual(created_user.email, 'user13@example.com')
    
    def test_CreateUser14(self):
        user_data = {
            'userName': 'user14',
            'firstName': 'Benjamin',
            'lastName': 'Thomas',
            'email': 'user14@example.com',
            'birthDate': '1987-03-10',
            'location': 'Metropolis',
            'profilePicture': 'profile14.jpg',
            'isLoggedIn': True,
        }


        user = AppUser.objects.create(**user_data)

        self.assertIsNotNone(user)

        created_user = AppUser.objects.get(userName='user14')
        self.assertIsNotNone(created_user)
        self.assertEqual(created_user.userName, 'user14')
        self.assertEqual(created_user.email, 'user14@example.com')

    def test_CreateUser15(self):
        user_data = {
            'userName': 'user15',
            'firstName': 'Ava',
            'lastName': 'Harris',
            'email': 'ava@example.com',
            'birthDate': '2004-02-15',
            'location': 'Ruralville',
            'profilePicture': 'avatar15.jpg',
        }


        user = AppUser.objects.create(**user_data)

        self.assertIsNotNone(user)

        created_user = AppUser.objects.get(userName='user15')
        self.assertIsNotNone(created_user)
        self.assertEqual(created_user.userName, 'user15')
        self.assertEqual(created_user.email, 'ava@example.com')

    def test_CreateUser16(self):
        user_data = {
            'userName': 'user16',
            'firstName': 'Liam',
            'lastName': 'Martin',
            'email': 'user16@example.com',
            'birthDate': '1980-08-20',
            'location': 'Countryside',
            'profilePicture': 'avatar16.png',
        }


        user = AppUser.objects.create(**user_data)

        self.assertIsNotNone(user)

        created_user = AppUser.objects.get(userName='user16')
        self.assertIsNotNone(created_user)
        self.assertEqual(created_user.userName, 'user16')
        self.assertEqual(created_user.email, 'user16@example.com')

    def test_CreateUser17(self):
        user_data = {
            'userName': 'user17',
            'firstName': 'Mia',
            'lastName': 'Smith',
            'email': 'user17@example.com',
            'birthDate': '1998-01-25',
            'location': 'Hometown',
            'profilePicture': 'profile17.jpg',
        }


        user = AppUser.objects.create(**user_data)

        self.assertIsNotNone(user)

        created_user = AppUser.objects.get(userName='user17')
        self.assertIsNotNone(created_user)
        self.assertEqual(created_user.userName, 'user17')
        self.assertEqual(created_user.email, 'user17@example.com')

    def test_CreateUser18(self):
        user_data = {
            'userName': 'user18',
            'firstName': '',
            'lastName': '',
            'email': 'user18@example.com',
            'birthDate': '1996-06-10',
            'location': '',
            'profilePicture': '',
        }


        user = AppUser.objects.create(**user_data)

        self.assertIsNotNone(user)

        created_user = AppUser.objects.get(userName='user18')
        self.assertIsNotNone(created_user)
        self.assertEqual(created_user.userName, 'user18')
        self.assertEqual(created_user.email, 'user18@example.com')

    def test_CreateUser19(self):
        user_data = {
            'userName': 'user19',
            'firstName': 'Noah',
            'lastName': 'White',
            'email': 'user19@example.com',
            'birthDate': '1997-04-05',
            'location': 'Outskirts',
            'profilePicture': 'profile19.jpg',
            'isLoggedIn': False,
        }


        user = AppUser.objects.create(**user_data)

        self.assertIsNotNone(user)

        created_user = AppUser.objects.get(userName='user19')
        self.assertIsNotNone(created_user)
        self.assertEqual(created_user.userName, 'user19')
        self.assertEqual(created_user.email, 'user19@example.com')

    def test_CreateUser20(self):
        user_data = {
            'userName': 'user20',
            'firstName': 'Unique',
            'lastName': 'User',
            'email': 'unique@example.com',
            'birthDate': '1999-12-31',
            'location': 'Specialtown',
            'profilePicture': 'unique_profile.jpg',
            'isLoggedIn': True,
        }


        user = AppUser.objects.create(**user_data)

        self.assertIsNotNone(user)

        created_user = AppUser.objects.get(userName='user20')
        self.assertIsNotNone(created_user)
        self.assertEqual(created_user.userName, 'user20')
        self.assertEqual(created_user.email, 'unique@example.com')

class UserViewTests(TestCase):
    def setUp(self):
        self.user = AppUser.objects.create(
            userName='testuser',
            firstName='John',
            lastName='Doe',
            email='test@example.com',
            birthDate='1990-01-01',
            location='Test Location',
            profilePicture='/static/profileImages/robot.jpg',
            isLoggedIn=False,
        )

    def test_HelloPage(self):
        response = self.client.get("")
        self.assertEqual(response.status_code, 302)

    def test_UserListView(self):
        response = self.client.get(reverse('user_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user/list.html')

    def test_UserDetailView(self):
        response = self.client.get(reverse('user_detail', args=[str(self.user.pk)]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user/detail.html')

    def test_UserCreateView(self):
        response = self.client.get(reverse('user_add'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user/add.html')

    def test_UserUpdateView(self):
        response = self.client.get(reverse('user_edit', args=[str(self.user.pk)]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user/edit.html')

    def test_UserDeleteView(self):
        response = self.client.get(reverse('user_delete', args=[str(self.user.pk)]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user/delete.html')