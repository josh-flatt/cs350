# Overview of Milestone 7 Test - Evan Duffield

* What did I do?
    * Created a security review checklist for our production launch.
    * Wrote an assessment report detailing the reasoning behind the checklist.
    * Gave scaling reccomendations for when our website grows.
    * Gave an estimate for the total amount of investment given to the project.
* What challenges do I have?
    * Not invoking the wrath of the DigitalOcean while security testing our app.
* Engineering investment
    * I spent about 6 hours on Test for Milestone 7
    * Our team met for 1 hour.
* 5-minute Video Demo
    * [Milestone 7 - Test](https://drive.google.com/file/d/1nVEK7djcRqR2SFpa_w999hMS26F_P_1l/view?usp=sharing)

## Security Review Checklist

See SecurityChecklist.pdf in the same directory.

## Security Assessment Report

When designing our assessment, I wanted to focus on three ways of securing the application: modifying the django project, configuring the cloud server, and testing with external tools.

When modifying the django project, one of the first important steps is to check that the DEBUG flag in settings is set to false. This is so attackers cant expose settings or credentials through intentionally triggering errors. Another step was to update all of the modules used by our project, and to see if any versions that we run have known vulnerabilities. So far, our project has passed on all of this. Another step to further secure our project would be to change the /admin/ url path to something harder to guess.

Configuring the cloud server was more straightforward. I added alerts for CPU spiking, as it could either indicate we need to urgently scale our application or that suspicious activity is being conducted. I also wanted to route all HTTP traffic to HTTPS, as people are logging into the site using credentials we dont wan't transported over plaintext without SSL. Further changes we can make down the line would involve moving all of our credentials into environment variables that are defined for the server, and isolating our database into its own server in a Virtual Private Cloud to protect it from the public internet.

Before in Milestone 5 I already port-scanned the server, so to extend on this I decided to test the application against sql injections and brute force attacks. To test SQL injections I used sqlmap, which django was properly able to deflect. I then proceeded to test if the application would stop a brute force/denial of service attack on the login form. DigitalOcean seemed to stop the brute forcing after ~120 attempts. Below is the python I used to test this:
```
import requests

def django_post():
    login_url = 'https://plankton-app-5fssv.ondigitalocean.app/accounts/login/'

    login_creds = {
        # Not real account, should trigger error 403
        'username': 'larry15',
        'password': '32r23i23',
    }

    try:
        response = requests.post(login_url, data=login_creds)

        print(f"Sent. Got status code {response.status_code} back.")

    except requests.RequestException as e:
        print(f"Error during login: {e}")

if __name__ == "__main__":
    for i in range(100000):
        print(i, end="")
        django_post()
```

## Scaling Recomendation

The most likely scenario I would see for our group needing to scale is this: we have a single small instance hosting the django application, which routes to a postgresql server. This is an affordable setup that works for 90% of our runtime, however on weekdays we have an influx of businessmen looking for new jobs on the clock. AWS would be the best cloud provider to move to for growth, as we found DigitalOcean to take too long for deployments. We would upgrade the postgresql server to have a little more capacity, and we would keep the django application on an EC2 server with similar hardware to our DigitalOcean deployment. However, during peak hours, more instances of the EC2 server would be launched with our application on it using an Auto-Scaling Group. These multiple servers will be communicating to the entire serverbase, but they will orchestrate the data into the one postgresql database.

## Engineering Investment Summary

Time investment each milestone per engineer. Estimate time and money needed for future projects.

Milestone 1:
Josh - 2 hours
Evan - 6 hours
Ryan - 4 hours
Kyle - 10 hours

Milestone 2:
Josh - 4 hours
Evan - 6 hours
Ryan - 3 hours
Kyle - Not Given

Milestone 3:
Josh - 4 hours
Evan - 5 hours
Ryan - 6 hours
Kyle - Not Given

Milestone 4:
Josh - 4 hours
Evan - 4 hours
Ryan - 5 hours
Kyle - 6 hours

Milestone 5:
Josh - 5 hours
Evan - 10 hours
Ryan - 5 hours
Kyle - 10 hours

Milestone 6:
Josh - 2 hours
Evan - Not Given
Ryan - 4 hours
Kyle - Not Given

Milestone 7:
Josh - 2 hours
Evan - 6 hours
Ryan - 4 hours
Kyle - Not Given

Average hours done per milestone: 18.7 hours

Average hours done per person each milestone: 4.67 hours

Total time: 130.9 hours

Estimated cost ($20/hr per engineer): $2618

## AI Prompts

See AI.md in the same directory.
