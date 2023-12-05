# AI Playbook

## What should I ask?

Prompt: 
I am taking a class and the instructor wants me to think of good prompts to ask ChatGPT to assist me in getting information about developing a user guide for a software engineering team project where we are making a website like LinkedIn using Django. What are some good prompts to ask?

### ChatGPT

1. **Getting Started:**
   - "What are the key steps in setting up a Django project for a professional networking website?"
   - "Can you provide a checklist for the initial setup of a Django project for a website like LinkedIn?"

2. **Database Design:**
   - "What are best practices for designing the database schema for a professional networking website?"
   - "Can you suggest guidelines for using Django models to represent user profiles and connections?"

3. **User Authentication and Authorization:**
   - "How can I implement secure user authentication in a Django project?"
   - "What Django features should I use to control user access and permissions?"

4. **Frontend Development:**
   - "What are the recommended tools and frameworks for building the frontend of a Django project?"
   - "How can I integrate JavaScript and AJAX for a smoother user experience in a Django web application?"

5. **User Interface Design:**
   - "Do you have any tips for designing an intuitive and user-friendly interface for a professional networking website?"
   - "What CSS frameworks or design principles work well with Django for creating responsive web pages?"

6. **Deployment:**
   - "What are the best practices for deploying a Django website, especially one with social features like connections and messages?"
   - "Can you recommend hosting services suitable for a Django project with moderate to high traffic?"

7. **Handling Media Files:**
   - "How can I manage and serve user-uploaded images and other media files in a Django application?"
   - "Are there any specific considerations for handling multimedia content in a social networking site built with Django?"

8. **Scalability and Performance:**
   - "What strategies can I implement to ensure the scalability of a Django project, especially in the context of a growing user base?"
   - "Are there any performance optimization techniques specific to Django web applications?"

9. **Documentation Tools:**
   - **"Which documentation tools or formats work well for creating comprehensive user guides for Django projects?"**
   - **"Are there any specific sections or details that are commonly overlooked in Django project documentation?"**

10. **Testing and Debugging:**
    - "What testing frameworks and tools are recommended for testing Django applications, especially those with complex features?"
    - "Can you provide guidance on debugging techniques specific to Django projects?"

Remember to tailor these prompts based on the specific requirements and focus areas of your user guide for the LinkedIn-like website project.


## Documentation Tools and Formats

Prompt: Which documentation tools or formats work well for creating comprehensive user guides for Django projects?

### ChatGPT

When creating comprehensive user guides for Django projects, it's important to choose documentation tools or formats that facilitate clarity, organization, and ease of maintenance. Here are some recommended options:

1. **Sphinx with reStructuredText:**
   - *Description:* Sphinx is a widely-used documentation tool that works seamlessly with reStructuredText, a lightweight markup language. It supports automatic generation of documentation from source code comments.
   - *Advantages:* Provides a clean and organized structure, supports cross-referencing, and allows easy integration with code documentation.

2. **MkDocs with Markdown:**
   - *Description:* MkDocs is a simple and intuitive documentation tool that uses Markdown for content creation. It is particularly well-suited for project documentation and allows for easy customization.
   - *Advantages:* Quick setup, user-friendly, and the documentation can be versioned using Git for easy tracking of changes.

3. **Read the Docs:**
   - *Description:* Read the Docs is a hosting platform for software documentation that supports various documentation formats, including Sphinx and MkDocs. It automatically builds and updates documentation when changes are pushed to the repository.
   - *Advantages:* Streamlines the deployment process, supports versioning, and provides an accessible platform for users.

4. **GitHub Pages with Jekyll:**
   - *Description:* GitHub Pages allows you to host documentation directly from your GitHub repository. Jekyll, a static site generator, can be used with GitHub Pages to create a clean and responsive documentation site.
   - *Advantages:* Integrates with your version control system, easy to set up, and allows for collaborative editing.

5. **AsciiDoc with Asciidoctor:**
   - *Description:* AsciiDoc is a human-readable documentation format, and Asciidoctor is a tool that converts AsciiDoc files to HTML, PDF, and other formats. It provides powerful features for creating technical documentation.
   - *Advantages:* Supports a concise syntax, extensibility, and produces professional-looking output.

Choose the tool or format that aligns with your team's preferences and workflow. Additionally, consider incorporating diagrams, code examples, and interactive elements to enhance the overall user experience.


## Commonly Overlooked Documentation

Prompt: Are there any specific sections or details that are commonly overlooked in Django project documentation?

### ChatGPT

When documenting Django projects, it's crucial to provide comprehensive and clear documentation to ensure the smooth development and maintenance of the project. Here are some sections and details that are commonly overlooked but should be included in Django project documentation:

1. **Project Overview:**
   - *Description:* Provide a high-level overview of the project, including its purpose, goals, and key features. This helps newcomers quickly understand the project's context.

2. **System Requirements:**
   - *Description:* Clearly outline the system requirements for running the Django project. Specify supported Python versions, required dependencies, and any other prerequisites.

3. **Installation Instructions:**
   - *Description:* Include step-by-step instructions for setting up the development environment. Cover virtual environment setup, package installations, and database configuration.

4. **Configuration Settings:**
   - *Description:* Document all configurable settings in the project, including those in the Django settings module. Clearly explain each setting's purpose and acceptable values.

5. **Database Schema:**
   - *Description:* Provide an overview of the database schema, including models, relationships, and any custom migrations. This is essential for developers and database administrators.

6. **API Documentation:**
   - *Description:* If the Django project includes APIs, document the endpoints, request and response formats, authentication mechanisms, and any relevant details for API consumers.

7. **Security Considerations:**
   - *Description:* Highlight security best practices and considerations specific to the Django project. Include information on handling sensitive data, preventing common vulnerabilities, and securing API endpoints.

8. **Contributing Guidelines:**
   - *Description:* Encourage collaboration by providing clear guidelines for contributing to the project. Include information on code style, testing procedures, and the contribution workflow.

9. **Testing Instructions:**
   - *Description:* Document how to run tests for the Django project, including any specific configurations or dependencies required for testing. This ensures the reliability of the project.

10. **Deployment Guide:**
    - *Description:* Offer guidance on deploying the Django project to production. Include information on server setup, web server configuration, and any additional steps needed for a successful deployment.

11. **Troubleshooting and FAQs:**
    - *Description:* Compile a list of common issues, error messages, and their solutions. Include a frequently asked questions (FAQ) section to address recurring queries.

12. **License Information:**
    - *Description:* Clearly state the project's license and include a copy of the license text. This ensures that users understand the terms under which they can use, modify, and distribute the project.

By including these often overlooked sections, you'll contribute to a more comprehensive and user-friendly documentation for your Django project.
