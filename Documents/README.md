# BridgeOut Project

## BridgeOut - Primary Business Objective

The goal of this project is to develop a web application modeled after the professional social networking site LinkedIn.
Our project has a tentative name of BridgeOut. We intend, at minimum, to develop the core functionality of the site.

## Milestones
* [Project Milestones](Misc-Docs/Milestones.md) - The
project is done by a series of milestones.

### Milestone 1 - Project Charter
* [Project Charter](Milestone-1/Requirements/Index.md) - The first milestone is to 
make key decisions about the project scope and how to meet the key objectives
with technology.
    * [Requirements](Milestone-1/Requirements/Index.md)
    * [Design](Milestone-1/Design/Index.md)
    * [Code](Milestone-1/Code/Index.md)
    * [Test](Milestone-1/Test/Index.md)

### Project Notes - Setting up a development environment - Evan Duffield

1. Clone the repository

2. Create a python virtual environment

```
python3 -m venv venv

// Windows

python -m venv venv
```

3. Enter the python virtual environment

```
source ./venv/bin/activate

// Windows

source .\venv\bin\activate.bat
```

4. Install Django

```
pip install django
```

5. Run app

```
python3 manage.py runserver

// Windows

python manage.py runserver
```