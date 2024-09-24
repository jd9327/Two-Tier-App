# Two-Tier Flask App

This project is a simple two-tier web application built with **Flask** (a Python web framework) and **MySQL** (a database management system). It demonstrates how to separate the application logic from the database layer using Docker containers.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
- [How to Run](#how-to-run)
- [Database Setup](#database-setup)
- [Creating a Custom Network](#creating-a-custom-network)
- [Contributing](#contributing)
- [License](#license)

## Features

- **User-Friendly Interface**: A simple web interface for user interactions.
- **Database Integration**: Stores messages and user data in a MySQL database.
- **Containerized Environment**: Easy setup and deployment using Docker.

## Technologies Used

- **Python**: Programming language used for the application.
- **Flask**: Web framework for building web applications in Python.
- **MySQL**: Relational database management system.
- **Docker**: Platform for developing, shipping, and running applications in containers.

## Getting Started

### Prerequisites

- **Docker**: Ensure you have Docker and Docker Compose installed on your machine.

### Clone the Repository

1. Open your terminal or command prompt.
2. Run the following command to clone the repository:

   ```bash
   git clone https://github.com/jd9327/Two-Tier-App.git
   ```

3. Navigate into the project directory:

   ```bash
   cd Two-Tier-App
   ```

## How to Run

1. **Create a Custom Network**: Before running the application, create a custom network to allow the containers to communicate:

   ```bash
   docker network create twotier
   ```

2. **Build and Run the Docker Containers**: Use the following command to build the images and start the containers:

   ```bash
   docker-compose up --build
   ```

3. **Access the Application**: Open your web browser and go to `http://localhost:5000`. You should see the application interface.

## Database Setup

- The MySQL database is automatically created when you run the application, using the configurations specified in the `docker-compose.yml` file.
- You can modify the database settings (like username and password) in the `docker-compose.yml` file as needed.

## Creating a Custom Network

In the `docker-compose.yml` file, you can define the custom network for the services. Here is an example of how to specify the network in your Docker Compose file:

```yaml
networks:
  twotier:
    driver: bridge
```

This configuration ensures that both the Flask application and the MySQL database can communicate with each other seamlessly.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## Notes

- Make sure to replace placeholders (e.g., your_username, your_password, your_database) with your actual MySQL configuration.

- This is a basic setup for demonstration purposes. In a production environment, you should follow best practices for security and performance.

- Be cautious when executing SQL queries directly. Validate and sanitize user inputs to prevent vulnerabilities like SQL injection.

- If you encounter issues, check Docker logs and error messages for troubleshooting.
