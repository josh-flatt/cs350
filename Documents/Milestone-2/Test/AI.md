# AI

## Chat GPT Prompts

Below are some of the things I asked Chat GPT in order to take care of my milestone.

### Write a simple python script to fetch a web page from "<https://plankton-app-5fssv.ondigitalocean.app>" and see that the title is set

```python
import requests
from bs4 import BeautifulSoup

url = "https://plankton-app-5fssv.ondigitalocean.app"

try:
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (HTTP status code 200)
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Get the title tag
        title_tag = soup.find('title')
        
        if title_tag:
            # Extract the title text
            title = title_tag.get_text()
            print(f"The title is set: {title}")
        else:
            print("No title tag found on the webpage.")
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
```

### How do you set up CI/CD with Django on DigitalOcean?

Setting up continuous integration and continuous deployment (CI/CD) for a Django application on DigitalOcean involves several steps, including configuring a version control system, setting up a CI/CD pipeline, and deploying the application. Below is a high-level overview of the steps to achieve this:

1. Version Control Setup (e.g., GitHub):

- Create a repository for your Django project on a version control platform like GitHub.

2. CI/CD Pipeline Setup (e.g., GitHub Actions):

- Create a .github/workflows directory in your repository to store GitHub Actions workflows.
- Create a YAML file (e.g., main.yml) defining the CI/CD workflow using GitHub Actions.

3. Configure the CI/CD Workflow:

- Define the workflow steps, such as setting up the environment, installing dependencies, running tests, and deploying the application.

4. Configure DigitalOcean Droplet:

- Set up a DigitalOcean Droplet to host your Django application.
- Configure the necessary settings, including security groups, environment variables, and database settings.

5. Deployment Script:

- Create a script to automate the deployment process on the DigitalOcean Droplet.
- This script may involve pulling the latest code from the repository, installing dependencies, migrating the database, and restarting the Django application.

6. Integrate Deployment in CI/CD Workflow:

- Modify the CI/CD workflow to include a step that triggers the deployment script on the DigitalOcean Droplet after a successful build and tests.

7. Test and Optimize:

- Test the CI/CD pipeline to ensure it deploys the application correctly.
- Optimize the pipeline and deployment script as needed for your specific application requirements.

Here's a simplified example of a GitHub Actions workflow (main.yml) for a Django application:

```
name: Django CI/CD

on:
  push:
    branches:
      - main

jobs:
  deploy:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v2

    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: 3.8

    - name: Install dependencies
      run: pip install -r requirements.txt

    - name: Run tests
      run: python manage.py test

    - name: Deploy to DigitalOcean
      run: bash deploy_script.sh
```

In this example, replace deploy_script.sh with your actual deployment script.

This is a basic outline, and depending on your specific requirements, you may need to tailor the steps and configurations accordingly. Additionally, you can use tools like Docker for containerization and other CI/CD platforms based on your preferences.
