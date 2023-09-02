# Milestone 1 - Design  - Evan Duffield

Choose the technology to use for the project.


## What I did for Milestone 1

### Web Framework and Language

After consulting my team on what development tools they would want to use, I decided to host everything on AWS. Here is an outline of the project:

- Frontend: Django templates / Jinja
 - Easy solution for static webpages
 - Most groupmembers are Javascript novices, will allow simple scripting
- Backend: Python/Django with PostgreSQL
 - Group wants experience with traditional SQL database, SQL fits project
 - Everyone in the group is familiar with python
- Container: Docker
 - Will allow for easier scripting to update the server in a CI/CD pipeline
 - Docker provides simple Django and PostgreSQL containers that we can use
- CI/CD: GitHub Actions
 - Kept in the repository, can build docker containers out of new code
 - We can script GitHub actions into updating an AWS instance whenever new code is pushed
- Hosting: AWS / Managed by: Terraform / Monitored by: Komiser and Cartograpy
 - AWS: We can set up an ec2 server to run our website 24/7
 - Terraform: Configuration language that helps you manage the cloud resources for an application
 - Komiser: Keeps track of what resources are up and how much they are costing the account holder
 - Cartography: Builds a relational graph of the user's cloud resources for security / redundancy purposes


### Status Video 

I created a summary of the design work completed.  View the video at 
[Milestone 1 - Design](Video.md)


## What I will do for Milestone 2

I'll containerize our application with docker and have github actions be linked to an AWS EC2 instance to run our website.

## Concerns and Challenges

Making sure team can properly use docker when developing on their own computer. AWS hosting prices are also a concern.
