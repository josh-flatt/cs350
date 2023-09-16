# Milestone 2 - Code  - Evan Duffield

Prototype a core feature of the application


## What I did for Milestone 2

### Containerizing our application

Our team members were using a combination of either Windows or Linux machines. This became an issue during documentation as setting up the same environment on different OS required a lot of time to create directions. Using a containerization platform will allow us all to have the same development environment regardless of OS.

To do this, I decided to containerize our application using Docker. The setup can be seen in the Dockerfile in our project directiory, and the commands to run the server are in the project readme. The benefit of this is that the team no longer need to configure a virtual environment for local development, and we can divide the application and database easily to help provide redundancy.

### Prototype

Several of our team members are also in the BACS350 class, which recently completed a project to create profile views using templates and userdata. Creating and linking users together using a frontend is our of our scope at the moment, however I was able to implement Python code of a FriendsList and User class in the file User.py.

The friends list will keep track of the user ids that the profile is linked with, and has methods for sending out friend requests, accepting or rejecting them, and giving a preview of the list based on filtering criteria. The User class manages all of the data that would be associated with a business social media account, and includes accessing methods to read and modify the account.

A basic Testing.py script was also created to assure methods were passing test cases.

### Status Video 

I created a summary of the code work completed.  View the video at 
[Milestone 2 - Code](https://drive.google.com/file/d/1LXRsAofR0VVSqFwLMK_SfsdjCU4iK3fS/view?usp=sharing)


## What I will do for Milestone 3

Ill work on having a temporary database setup so we can have a dummy list of users to develop our Django templates with.

## Concerns and Challenges

DigitalOcean has some odd features when hosting an application, Docker could be difficult to setup with multiple containers this next milestone.
