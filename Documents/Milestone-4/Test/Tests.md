# View Tests and Coverage

## Tests For All Data Views

### Setup test framework for automated testing

The test framework is setup and ready to go using the command "python manage.py test".

### Build data tests for CRUD

All data tests for the CRUD operations of the User model are implemented. Many of these were completed in previous milestones.

### Build tests for each view

Test for each view are implemented. Many of these were completed in previous milestones.

### Compare lines of test code to lines of product code (should be 50%)

There are 577 Lines of test code and 846 lines of other code, so the number of lines of test code is 68% that of product code.

## Measured Test Coverage

### Setup tool to measure test coverage

Coverage.py was setup as the tool to measure coverage. The process is as follows:

1. If coverage is not installed, install, likely using the command "pip install coverage"
2. Navigate to the Application directory in the terminal.
3. Run this command to run all tests while measuring coverage. "coverage run --source='.' manage.py test helloapp"
4. Use the command "coverage report" to view the results.

### Ran unit tests

Ran the initial tests, and found a few failing ones, I repaired each of them so now there are 0 failing tests.

### Recorded initial test coverage

The initial coverage from all previously written tests is 96%.

### Wrote more tests until coverage reached 80%

The total coverage has already surpassed this threshold.
