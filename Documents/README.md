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

2. Install Python, Docker

3. Docker setup

Build the container after making source changes:

```
sudo docker build -t bridgeout .
```

Run the server:

```
sudo docker run -d -p 8000:8000 bridgeout
```

Navigate to:

```
http://localhost:8000/
```

View container tags, kill server:

```
sudo docker stats

sudo docker kill "Container name"

```

4. Dockerless - Python virtual environment

Create the virtual environment:

```
python3 -m venv venv

// Windows

python -m venv venv
```

Enter the virtual environment:

```
source ./venv/bin/activate

// Windows

source .\venv\bin\activate.bat
```

Install requirements:

```
pip install -r requirements.txt
```

Run app:

```
python3 manage.py runserver

// Windows

python manage.py runserver
```