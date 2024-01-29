# ALX Backend User Data

In this project, I implement a user authentication service using Python's Flask framework and SQLAlchemy for database operations. The service allows users to register, log in, log out, view their profile, reset their password, and update their password.

## Learning Outcomes
Throughout this project, I've gained a deep understanding of several key concepts in web development and API design. Firstly, I've learned how to declare API routes in a Flask application, enabling me to define endpoints for handling various client requests. Secondly, I've mastered the techniques for getting and setting cookies, which are essential for maintaining session state and user authentication across HTTP requests. Additionally, I've become proficient in retrieving request form data, allowing me to process user input effectively. Finally, I've learned how to return various HTTP status codes, enabling me to communicate the outcome of each request accurately. These learning outcomes have equipped me with the skills needed to build secure and efficient web applications using Flask and SQLAlchemy.

## Tasks

1. **User Model**: In this task, I create a SQLAlchemy model named User for a database table named users, defining attributes such as id, email, hashed_password, session_id, and reset_token.

2. **Create User**: Here, I implement the add_user method to save user data to the database.

3. **Find User**: In this task, I implement methods to find and update user data in the database.

4. **Hash Password**: For this task, I define a method to hash passwords using bcrypt.

5. **Register User**: Here, I implement user registration with password hashing and error handling for existing users.

6. **Basic Flask App**: In this task, I set up a basic Flask app with a single route returning a JSON payload.

7. **Register User Endpoint**: In this task, I implement an endpoint to register users via POST request.

8. **Credentials Validation**: Here, I implement validation for user login credentials.

9. **Generate UUIDs**: In this task, I implement a function to generate UUIDs for session IDs.

10. **Get Session ID**: Here, I create a method to generate and store session IDs for users.

11. **Log In**: In this task, I implement a login endpoint to authenticate users and set session cookies.

12. **Find User by Session ID**: Here, I implement a method to retrieve user data using session IDs.

13. **Destroy Session**: In this task, I implement a method to invalidate session IDs.

14. **Log Out**: Here, I implement a logout endpoint to destroy user sessions.

15. **User Profile**: In this task, I create an endpoint to fetch user profiles.

16. **Generate Reset Password Token**: Here, I implement a method to generate and store reset password tokens.

17. **Get Reset Password Token**: In this task, I implement an endpoint to request reset password tokens.

18. **Update Password**: Here, I implement a method to update user passwords using reset tokens.

19. **Update Password Endpoint**: In this task, I implement an endpoint to update user passwords.

20. **End-to-End Integration Test**: Finally, I write integration tests for all implemented endpoints to ensure functionality and reliability.