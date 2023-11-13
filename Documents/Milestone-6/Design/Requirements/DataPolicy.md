# Database Management Policy and Practices

## Movement to DigitalOcean Managed Database

We will move to DigitalOcean's Managed Database service. We are already using DigitalOcean and
the platform offers significant preconfiguration that makes setup easy. We have refrained from
moving beyond a dev database up until this point because we we still making significant structural
changes to our data models.

## Using Django's form and model validation

Our application uses crispy forms to interface with Django's form validation mechanisms.
This helps ensure that the information entered into the system is consistent with our data
models and helps maintain our database's integrity.

## Security and Logging

We use custom mixins and Django's user and auth modules which provide a secure way to authenticate users, and to ensure that forms and views can only be accessed by users with the appropriate authorization. This access control helps safeguard the integrity of the database.

## Documentation

All model changes, migrations, and backups will be documented after the set up of the managed database. Some step by step procedures regarding data management are outlined in the operations document.