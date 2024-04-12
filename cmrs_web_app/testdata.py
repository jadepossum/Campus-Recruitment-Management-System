import random
from faker import Faker
from django.utils import timezone
from models import Jobs, Users, Student, Internship, Project, UserDefinedTable, Certification

fake = Faker()

# Generate test data for Jobs model
for _ in range(60):
    Jobs.objects.create(
        Title=fake.job(),
        id=random.randint(1, 100000),  # Random ID
        Description=fake.text(max_nb_chars=500)
    )

# Generate test data for Users model
for _ in range(60):
    Users.objects.create(
        name=fake.name(),
        id=random.randint(1, 100000)  # Random ID
    )

# Generate test data for Student model
for _ in range(60):
    Student.objects.create(
        roll_number=fake.unique.bothify(text='##JJ#A####'),
        name=fake.name(),
        email=fake.email(),
        cgpa=random.uniform(6, 10),
        skills=', '.join(fake.words(nb=5)),
        twelthPercentage=random.uniform(50, 100),
        tenthCGPA=random.uniform(6, 10),
        BackLogCount=random.randint(0, 5),
        Gap=random.choice([True, False]),
        github_profile=fake.url(),
        linkedin_profile=fake.url(),
        portfolio_website=fake.url()
    )

# Generate test data for Internship model
for student in Student.objects.all():
    for _ in range(random.randint(0, 3)):  # Random number of internships per student
        Internship.objects.create(
            roll_number=student,
            company_name=fake.company(),
            role=fake.job(),
            start_date=fake.date_between(start_date='-3y', end_date='today'),
            end_date=fake.date_between(start_date='today', end_date='+3y'),
            responsibilities=fake.text(max_nb_chars=200)
        )

# Generate test data for Project model
for student in Student.objects.all():
    for _ in range(random.randint(0, 5)):  # Random number of projects per student
        Project.objects.create(
            roll_number=student,
            title=fake.catch_phrase(),
            description=fake.text(max_nb_chars=500),
            technologies_used=', '.join(fake.words(nb=3)),
            github_repo_url=fake.url()
        )

# Generate test data for UserDefinedTable model
for student in Student.objects.all():
    for _ in range(random.randint(0, 2)):  # Random number of user defined tables per student
        UserDefinedTable.objects.create(
            roll_number=student,
            title=fake.sentence(nb_words=3),
            context=fake.text(max_nb_chars=200)
        )

# Generate test data for Certification model
for student in Student.objects.all():
    for _ in range(random.randint(0, 4)):  # Random number of certifications per student
        Certification.objects.create(
            roll_number=student,
            title=fake.sentence(nb_words=3),
            url=fake.url(),
            skills=', '.join(fake.words(nb=3)),
            domain_technology=fake.word(),
            year_earned=fake.date_time_this_decade()
        )
