# Operations Processes

## Data Migration Plan

The data migrations will follow a set of steps to maintain data integrity.
1. Complete each step of the data backup plan.
2. Test the new migration on a development server using the Django test framework.
3. Assess existing database and proposed changes to models to identify potential migration issues.
4. Use Django management command to make the migrations on the production database.
5. Run tests to assess impact.
6. Use all features of the app to assess impact.

## Data Backup Plan

The Backups will follow these steps. They will be performed pre-migration and on Mondays and Fridays.
1. Use Django's dumpdata command to process all database objects into a json file.
2. Upload the json file to the git repo's backups folder.

## Data Recovery Plan

If data is lost and must be retrieved, the json backup files can be manually accessed and the
needed elements can be retrieved. The information is then used to create a new object or to edit an existing one.

## Data Rollback Plan

In case of database compromisation, the database can be rolled back to a backup state.
First, make a backup of the compromised database if possible.
Then, clear the production database, and then load the backup json file into it.
CAUTION: This will cause the loss of all database objects created after the chosen backup file.