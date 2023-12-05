# Internal Product Upgrade Notes - Version [1.1.0]

## Defect Fixes

### 1. Defect: Website is not Centered

#### Description

The entire web application is off-centered, instead of having equal margins on the web page on either side of it.

#### Resolution

[Document the technical steps taken to address and fix the defect. Include any code changes, bug tracking details, or other relevant information.]

### 2. Defect: Displayed time is UTC, not MDT

#### Description

There are spots in our web application, such as the date/time of when an account was created, that displays the date/time in UTC time, instead of local time.

#### Resolution

[Document the technical steps taken to address and fix the defect. Include any code changes, bug tracking details, or other relevant information.]

### 3. Defect: Navbar is not uniform across site

#### Description

When navigating from page to page, the navbar will switch from bordering the top, left, and right edges of the screen, to having spacing from the edges.

#### Resolution

[Document the technical steps taken to address and fix the defect. Include any code changes, bug tracking details, or other relevant information.]

## Feature Enhancements

### 1. Feature Enhancement: Combine User and Profile models/objects

#### Description

There are two models in our codebase that represent the same thing, and have a 1-to-1 relationship.
These should be combined to make our code and website experience more concise.

#### Enhancements

- [Enhancement 1]
- [Enhancement 2]
- [Enhancement 3]

### 2. Feature Enhancement: Correct container spacing

#### Description

All of the subcontainers in the containers on the web app do not have correct
spacing within their parent containers. These should be spaced correctly to
look nicer.

#### Enhancements

- [Enhancement 1]
- [Enhancement 2]
- [Enhancement 3]

### 3. Feature Enhancement: Remove unused code

#### Description

During initial development, our django application was moved within our codebase, and the old application is no longer used.

#### Enhancements

- [Enhancement 1]
- [Enhancement 2]
- [Enhancement 3]

## New Features/Capabilities

### 1. New Feature: Implement managed database

#### Description

A managed database must be implemented for our application. Each time that our
website is rebuilt, all production data is lost.

#### Benefits

- [Benefit 1]
- [Benefit 2]
- [Benefit 3]

### 2. New Feature: Add user-user direct messages

#### Description

A requested feature for our application is to add peer-peer messaging in the application.

#### Benefits

- [Benefit 1]
- [Benefit 2]
- [Benefit 3]

### 3. New Feature: Implement groups

#### Description

Part of our initial scope of the project included adding groups (like universities or companies).

#### Benefits

- [Benefit 1]
- [Benefit 2]
- [Benefit 3]

## Implementation Guidelines

[Include any specific instructions or guidelines for the development team regarding the new changes. This may include migration steps, API updates, or any other relevant information.]

## Testing and Quality Assurance

[Document any specific testing procedures or considerations for the QA team, including test cases for the fixed defects and newly implemented features.]

## Developer Feedback

[Encourage developers to provide feedback on the code changes and improvements. Include contact information or links for feedback submission.]

Thank you for your dedication to maintaining and enhancing our product! Your efforts contribute to the ongoing success of our development projects.
