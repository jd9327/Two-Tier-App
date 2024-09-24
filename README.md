# Two-Tier Flask App

A simple two-tier web application built with Flask and MySQL, demonstrating the separation of the application layer and the database layer.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
- [How to Run](#how-to-run)
- [Database Setup](#database-setup)
- [Contributing](#contributing)
- [License](#license)

## Features

- Flask web framework for building the application.
- MySQL for database management.
- Docker containers for easy deployment and isolation.

## Technologies Used

- Python
- Flask
- MySQL
- Docker

## Getting Started

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/jd9327/Two-Tier-App.git
   cd Two-Tier-App
   ```

2. **Prerequisites:**

   Ensure you have Docker and Docker Compose installed on your machine.

## How to Run

1. Build and run the Docker containers:

   ```bash
   docker-compose up --build
   ```

2. Access the application at `http://localhost:5000`.

## Database Setup

- The MySQL database is initialized with environment variables defined in the `docker-compose.yml` file.
- Modify the environment variables as needed for your configuration.

## Contributing

Contributions are welcome! Feel free to submit a pull request or open an issue for any suggestions or improvements.

### Customization

- Replace any placeholders (like URLs or specific configurations) with your actual project details.
- Feel free to add any additional sections you think are necessary, such as screenshots, usage instructions, or examples.

If you have any specific points you want to include or adjust, let me know!
