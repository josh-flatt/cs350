# Internal Product Upgrade Notes - Version 1.1.0

## Defect Fixes

### 1. Defect: Website is not Centered

#### Description

The entire web application is off-centered, instead of having equal margins on the web page on either side of it.

#### Resolution

[Include detailed technical steps taken to address and fix the defect. Include any code changes, bug tracking details, or other relevant information.]

### 2. Defect: Displayed time is UTC, not MDT

#### Description

There are spots in our web application, such as the date/time of when an account was created, that displays the date/time in UTC time, instead of local time.

#### Resolution

[Include detailed technical steps taken to address and fix the defect. Include any code changes, bug tracking details, or other relevant information.]

### 3. Defect: Navbar is not uniform across site

#### Description

When navigating from page to page, the navbar will switch from bordering the top, left, and right edges of the screen, to having spacing from the edges.

#### Resolution

[Include detailed technical steps taken to address and fix the defect. Include any code changes, bug tracking details, or other relevant information.]

## Feature Enhancements

### 1. Feature Enhancement: Combine User and Profile models/objects

#### Description

There are two models in our codebase that represent the same thing and have a 1-to-1 relationship.
These should be combined to make our code and website experience more concise.

#### Enhancements

- Remove redundancy in models
- Simplify database queries
- Improve overall code maintainability

### 2. Feature Enhancement: Correct container spacing

#### Description

All subcontainers in the containers on the web app do not have correct spacing within their parent containers. These should be spaced correctly to look nicer.

#### Enhancements

- Implement consistent spacing throughout the application
- Enhance visual aesthetics and user experience
- Standardize container layouts for future scalability

### 3. Feature Enhancement: Remove unused code

#### Description

During initial development, our Django application was moved within our codebase, and the old application is no longer used.

#### Enhancements

- Increase codebase cleanliness
- Improve codebase maintainability
- Enhance overall system performance

## New Features/Capabilities

### 1. New Feature: Implement managed database

#### Description

A managed database must be implemented for our application. Each time that our website is rebuilt, all production data is lost.

#### Benefits

- Ensure data persistence during application rebuilds
- Facilitate easier data management and backups
- Enhance overall application reliability

### 2. New Feature: Add user-user direct messages

#### Description

A requested feature for our application is to add peer-peer messaging in the application.

#### Benefits

- Enable direct communication between users
- Enhance user engagement and collaboration
- Provide a more comprehensive communication platform

### 3. New Feature: Implement groups

#### Description

Part of our initial scope of the project included adding groups (like universities or companies).

#### Benefits

- Facilitate organization and categorization of users
- Enhance user experience with group-based features
- Enable scalability for future feature developments

## Implementation Guidelines

[Include any specific instructions or guidelines for the development team regarding the new changes. This may include migration steps, API updates, or any other relevant information.]

## Testing and Quality Assurance

[Document any specific testing procedures or considerations for the QA team, including test cases for the fixed defects and newly implemented features.]

## Developer Feedback

[Encourage developers to provide feedback on the code changes and improvements. Include contact information or links for feedback submission.]

Thank you for your dedication to maintaining and enhancing our product! Your efforts contribute to the ongoing success of our development projects.
