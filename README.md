# Campus Recruitment Management System

A Django-based web application designed to streamline and automate campus recruitment processes for universities and colleges. This system manages student, company, and job data, facilitates applications, feedback, and profile management, and provides interfaces for both Training and Placement Officers (TPOs) and students.

## Features

- **Student Management**: Track student academic records, skills, internships, certifications, and project portfolios.
- **Job Posting & Application**: Companies can post jobs, set eligibility criteria, and students can apply directly through the portal.
- **Feedback System**: Students can provide feedback on recruitment events and phases.
- **Eligibility & Results**: Automated eligibility checks based on CGPA, backlogs, and skill requirements. TPOs can view and filter placement results by branch and batch.
- **Profile Management**: Students can update profiles, including LinkedIn, GitHub, and portfolio links.
- **Admin Panel**: Powerful Django admin for managing all entities (students, companies, jobs, applications, feedback, etc.)
- **REST API**: Provides endpoints for authentication, job posting, application, feedback, and reporting.

## Technologies Used

- **Backend**: Django, Django REST Framework
- **Database**: (Default Django, customizable)
- **Admin Enhancements**: django-import-export for easy data import/export

## Getting Started

### Prerequisites

- Python 3.8+
- Django (see `requirements.txt` if available)
- pip

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/jadepossum/Campus-Recruitment-Management-System.git
    cd Campus-Recruitment-Management-System
    ```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Apply migrations:
    ```bash
    python manage.py migrate
    ```
4. Create a superuser for admin access:
    ```bash
    python manage.py createsuperuser
    ```
5. Run the development server:
    ```bash
    python manage.py runserver
    ```

### Usage

- Visit `http://localhost:8000/admin` for the Django admin interface.
- Students, TPOs, and companies can interact with the portal as per assigned roles.
- REST API endpoints are available for integration and automation.

## Project Structure

```
cmrs_web_app/
├── admin.py
├── models.py
├── views.py
├── serializers.py
├── migrations/
└── ...
```

- `models.py` - Defines the core entities: Student, Internship, Project, Certification, Jobs, Application, Feedback, etc.
- `views.py` - Contains business logic and API endpoints for login, signup, job posting, application, feedback, and reporting.
- `serializers.py` - Serializes data for API responses.
- `admin.py` - Customizes Django admin for resource management.

## Main Entities

- **Student**: Holds academic and personal details, skills, and links.
- **Project/Internship/Certification**: Student achievements portfolio.
- **Jobs & Companies**: Recruitment opportunities and employer info.
- **Application**: Tracks student job applications.
- **Feedback**: Student feedback on recruitment phases and events.

## Contribution

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is for academic and demonstration purposes. For usage or licensing details, please contact the repository owner.
