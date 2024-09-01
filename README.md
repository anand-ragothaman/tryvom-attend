
# TryVom Attend

**TryVom Attend** is a single-user attendance management software built with Django. It provides functionalities to manage attendance with a user-friendly interface. The software includes the following modules:

- **Dashboard**: Overview of attendance data and quick access to various features.
- **Category**: Manage categories related to attendance.
- **Members**: Manage members who are tracked in the attendance system.
- **Attendance**: Track and manage attendance records.
- **Report**: Generate and view attendance reports.
- **Profile**: Manage user profile and settings.

## Installation and Setup

Follow these instructions to set up and run TryVom Attend on your local machine.

### Prerequisites

Ensure you have the following installed:

- Python 3.6+
- pip (Python package installer)
- Virtualenv (optional but recommended)

### Installation Steps

1. **Clone the Repository**

   ```bash
   git clone https://github.com/anand-ragothaman/tryvom-attend.git
   cd tryvom-attend
   ```

2. **Create a Virtual Environment (Optional)**

   It’s recommended to use a virtual environment to manage dependencies.

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**

   Install the required Python packages using pip.

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations**

   Run Django’s migration commands to set up the database schema.

   ```bash
   python manage.py migrate
   ```

5. **Create a Superuser**

   Create a superuser account to access the Django admin interface.

   ```bash
   python manage.py createsuperuser
   ```

6. **Run the Development Server**

   Start the Django development server to run the application.

   ```bash
   python manage.py runserver
   ```

7. **Access the Application**

   Open your web browser and go to `http://127.0.0.1:8000/` to access the TryVom Attend application.

8. **Access Admin Interface**

   Go to `http://127.0.0.1:8000/admin/` to access the Django admin interface and manage your application. Log in using the superuser credentials created earlier.

## Usage

- **Dashboard**: View an overview of attendance data.
- **Category**: Add, edit, or delete categories related to attendance.
- **Members**: Manage member information.
- **Attendance**: Record and manage attendance for members.
- **Report**: Generate attendance reports.
- **Profile**: Update your profile and settings.

## Contributing

Feel free to contribute to the project by submitting pull requests or opening issues. Your contributions are welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Django framework for the robust web development.
- Bootstrap for front-end styling.

```
