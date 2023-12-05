# Internal Product Upgrade Notes - Version 1.1.0

## Defect Fixes

### 1. Defect: Website is not Centered

#### Description

The entire web application is off-centered, instead of having equal margins on the web page on either side of it.

#### Resolution

Consider adjusting the CSS styling for the main container of your web application. You may use the `margin: auto;` property to center the container horizontally. Additionally, ensure that the container has sufficient width to prevent any overflow issues.

### 2. Defect: Displayed time is UTC, not MDT

#### Description

There are spots in our web application, such as the date/time of when an account was created, that displays the date/time in UTC time, instead of local time.

#### Resolution

Review the code responsible for displaying date and time. Utilize JavaScript's `toLocaleString` method to convert UTC timestamps to the user's local time. Ensure that the application correctly detects and uses the user's timezone to provide an accurate and user-friendly experience.

### 3. Defect: Navbar is not uniform across site

#### Description

When navigating from page to page, the navbar will switch from bordering the top, left, and right edges of the screen, to having spacing from the edges.

#### Resolution

Evaluate the CSS styling for the navbar and standardize it across all pages. Check for any conditional styling that might be causing variations. Consider creating a separate CSS file for the navbar styles and include it consistently on all pages to ensure a uniform appearance.

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

#### Feasibility and Impact

- **Feasibility:** Feasible with cloud database solutions like AWS RDS or Google Cloud SQL.
- **Impact:** High. Enhances data reliability and management, crucial for a seamless user experience.

### 2. New Feature: Add user-user direct messages

#### Description

A requested feature for our application is to add peer-peer messaging in the application.

#### Benefits

- Enable direct communication between users
- Enhance user engagement and collaboration
- Provide a more comprehensive communication platform

#### Feasibility and Impact

- **Feasibility:** Feasible with real-time messaging libraries like Socket.IO or Pusher.
- **Impact:** Medium to High. Significantly improves user communication and engagement.

### 3. New Feature: Implement groups

#### Description

Part of our initial scope of the project included adding groups (like universities or companies).

#### Benefits

- Facilitate organization and categorization of users
- Enhance user experience with group-based features
- Enable scalability for future feature developments

#### Feasibility and Impact

- **Feasibility:** Feasible with proper database and permission management.
- **Impact:** High. Fosters community building, personalizing user experience, and supporting future scalability.

## Implementation Guidelines

[Include any specific instructions or guidelines for the development team regarding the new changes. This may include migration steps, API updates, or any other relevant information.]

## Testing and Quality Assurance

[Document any specific testing procedures or considerations for the QA team, including test cases for the fixed defects and newly implemented features.]

## Developer Feedback

[Encourage developers to provide feedback on the code changes and improvements. Include contact information or links for feedback submission.]

Thank you for your dedication to maintaining and enhancing our product! Your efforts contribute to the ongoing success of our development projects.
