# Basic authentication

## Overview
This repository contains a simple API implementation with basic authentication. It offers functionality for user management and authentication using Flask, Python's micro web framework.

## Learning Outcomes
- Understanding of authentication concepts
- Base64 encoding and decoding
- Implementation of Basic authentication
- Handling HTTP status codes and error responses

### Installation and Setup
1. Clone the repository and navigate into the project directory.
   ```bash
   git clone <repository-url>
   cd <project-directory>
   ```

2. Install project dependencies using pip.
   ```bash
   pip3 install -r requirements.txt
   ```

3. Start the server with the following command:
   ```bash
   API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app
   ```

### Usage
You can interact with the API using curl commands or any HTTP client.

#### Example API Requests:
1. Check API status:
   ```bash
   curl "http://0.0.0.0:5000/api/v1/status"
   ```

2. Unauthorized Access:
   ```bash
   curl "http://0.0.0.0:5000/api/v1/unauthorized"
   ```

3. Forbidden Access:
   ```bash
   curl "http://0.0.0.0:5000/api/v1/forbidden"
   ```

## Tasks
#### Task 0: Simple Basic API
- Download and start the project.
- Install dependencies and start the server.

#### Task 1: Error handler - Unauthorized
- Implement an error handler for unauthorized requests (HTTP status code 401).

#### Task 2: Error handler - Forbidden
- Implement an error handler for forbidden requests (HTTP status code 403).

#### Task 3: Auth class
- Create an Auth class to manage API authentication.

#### Task 4: Define excluded paths
- Update the Auth class to define routes that don't need authentication.

#### Task 5: Request validation
- Validate all requests to secure the API.

#### Task 6: Basic auth
- Implement Basic authentication class and integrate it into the application.

#### Task 7: Basic - Base64 part
- Add methods to handle Base64 encoding and decoding for Basic authentication.

#### Task 8: Basic - Base64 decode
- Implement method to decode Base64 authorization header.

#### Task 9: Basic - User credentials
- Extract user credentials from decoded Base64 authorization header.

#### Task 10: Basic - User object
- Retrieve User instance based on email and password.

#### Task 11: Basic - Overload current_user
- Overload current_user method to retrieve User instance for a request.

#### Task 12: Basic - Allow password with ":"
- Allow passwords containing ":" in user credentials.

#### Task 13: Require auth with stars
- Update require_auth method to support wildcard (*) in excluded paths.

### Contributors
- [Samuel Mukosa Chibwe](https://github.com/chibwesamuel)

### License
This project is licensed under the [MIT License](LICENSE).
