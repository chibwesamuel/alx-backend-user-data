# Session Authentication

#### Overview
This directory implements a Session Authentication system. It consists of several tasks aimed at understanding and implementing session-based authentication mechanisms without relying on external modules.

## Tasks

1. **Et moi et moi et moi!**
   - Copy all the work from the `0x06-Basic_authentication` project into this folder.
   - Implement a new endpoint `GET /users/me` to retrieve the authenticated User object.

2. **Empty session**
   - Create a class `SessionAuth` inheriting from `Auth`.
   - Set up the class and validate inheritance without overloading.

3. **Create a session**
   - Implement a method `create_session` in `SessionAuth` to generate a Session ID for a user.
   - Store the Session ID and user ID in an in-memory dictionary.

4. **User ID for Session ID**
   - Implement a method `user_id_for_session_id` in `SessionAuth` to retrieve a User ID based on a Session ID.

5. **Session cookie**
   - Add a method `session_cookie` to extract a cookie value from a request.

6. **Before request**
   - Update the request handler to validate the presence of authentication credentials.

7. **Use Session ID for identifying a User**
   - Implement a method `current_user` in `SessionAuth` to retrieve a User instance based on a Session ID.

8. **New view for Session Authentication**
   - Create a Flask view to handle authentication routes.

9. **Logout**
   - Implement session destruction method in `SessionAuth`.

10. **Sessions in database**
    - Introduce a database-backed authentication system.
    - Create a model `UserSession` and implement `SessionDBAuth` class inheriting from `SessionExpAuth`.
