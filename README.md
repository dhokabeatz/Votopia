# Votopia

Welcome to **Votopia**, a revolutionary eVoting platform designed to streamline the voting process for schools and educational institutions. Votopia empowers students to exercise their democratic rights conveniently and securely, eliminating the need to travel to polling centers.

![Screenshot of Votopia](static/images/login_page.png)

## Overview

**Votopia** modernizes traditional voting methods, which can be cumbersome and time-consuming. This user-friendly web application facilitates seamless voting for various student positions, from class representatives to student council members. Our platform simplifies the voting process and ensures accessibility for all students, regardless of their location.

### Author

- [Henry Agyemang](mailto:amglna2020@gmail.com)

## Deployed Site

You can access the live application here: [Votopia](https://votopia-portfolio-app.onrender.com)

## Installation

To get started with Votopia locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/dhokabeatz/votopia
   ```

2. Navigate to the project directory:
   ```bash
   cd votopia
   ```

3. Install the necessary dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Make migrations to the database:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```
   (follow the prompt to create one)

6. Run the application:
   ```bash
   python manage.py runserver
   ```

## Usage

Once the application is running on localhost, you can:

- Register as a voter
- Create an election using superuser credentials
- Vote securely from any location
- View real-time results after the election concludes

## Contributing

Contributions to **Votopia** are welcome! If you have suggestions for improvement or new features, follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b your-branch-name`.
3. Make your changes.
4. Commit your changes: `git commit -m 'Add some feature'`.
5. Push to the branch: `git push origin your-branch-name`.
6. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
