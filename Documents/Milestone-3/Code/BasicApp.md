# Basic Application

## User Story/Feature Focus

The user story/feature that I chose to focus on for this milestone was the "Create Profile" Feature.

## Prototype of Core Features

### Data

I created first draft, untested versions of all the models outlined in the milestone 2 [software architecture document](../../Milestone-2/Design/Architecture.md).

### Views

I created basic versions all five of the CRUD views for the AppUser model.
* AppUser: list, detail, create, update, delete

## Automated Testing of Core Features

I created a couple of automated tests for the AppUser Model, and fixed the directory structure so they can be automatically detected.

### Deployment

I created a database.json containing one test user
I added run commands to migrate and load data from database.json
I deployed to DigitalOcean and added a button to the static landing page that leads to the AppUser list view.