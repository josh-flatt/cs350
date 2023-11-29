# Overview of Milestone 5 Design - Evan Duffield

* What did I do?
    * Created a guide of Design Patterns for the project.
    * Refactored and cleaned up methods/code in the project.
    * Tested the app's core functions.
    * Turned debugging off, checked for any exposed ports on the server.
* What will I do?  Code for Milestone 6
    * Help finish the last user stories before the end of the semester.
* What challenges do I have?
    * Refactoring a large project without breaking anything.
* Engineering investment
    * I spent about 6 hours on Design for Milestone 5
    * Our team met for 2 hours.
* 5-minute Video Demo
    * [Milestone 5 - Design](https://drive.google.com/file/d/178AQaCqk-bsFxKtv5c-KI2F8hKQ_fy6s/view?usp=sharing)

## Design Pattern Catalog

Example code from the project can be found in the presentation in the same folder.

After reviewing the project: I decided on these design patterns to choose for the catalog:

* Keep requirements.txt updated. This is so the team isn't stuck trying to figure out how to get the proper version of a dependency someone adds to the project.
* Separate local imports from modules. It can be difficult to trace local module use in the project when it is imported in the middle of a large group of Django modules.
* Maintain a Model-View-Controller design pattern using Django's Model-View-Template pattern. I have been on a lot of projects where people wanted to take a Java approach of having one class per file. Since this application is relatively simple, so we wanted to keep as few files as possible. models.py, views_classes.py, vews_functions.py, and the templates all form Django's Model-View-Template, which focuses more on the front-end than a controller.


## Refactoring

Example code from the project can be found in the presentation in the same folder.

Overall the project was already fairly factored. variables were declared when reused in most places, and when they weren't such as for the a variable in the dispatch methods in views_functions.py I inlined the variable. I also went through the imported modules and removed anything not in use to improve our performance. I also renamed the IsUserProfileFromExpMixin and IsUserProfileFromEduMixin methods to be more clear and verbose in views_functions.py.

## Help with implementation

I helped with implementation this Milestone by testing the application and making modifications for production. This involved:

* Tested the app's major functions, experimented with input limits to assure a crash couldn't occur as a result.
* Changing settings.py to be production ready. The most important part of this was setting DEBUG to False, so attackers cant find out our Django version data by giving a bad url.
* Making sure our web server's HTTP/HTTPS ports were the only open ports. This was done with a traceroute to our digitalocean app, before using the resulting IP to do a port scan.
* Adding css in some rough areas into the html to make things centered and presentable.

## AI Prompts

ChatGPT was able to help a lot with refactoring and coming up with large strings to test input on the website. Here are some of the prompts I asked:

* What are some design patterns that can help organize a large Django project?
* What are some examples of design patterns?
* How would you refactor this method?
* What is the standard for storing local modules in a django project?
* What could this method be renamed to make it more maintainable?
* Give me some strings to test input limits on my website.
