import random
from faker import Faker

fake = Faker()

skills_pool = [
    "Python", "JavaScript", "Machine Learning", "SQL",
    "React", "Data Analysis", "Cloud Computing", "Docker"
]

titles = [
    "Data Scientist", "Software Engineer", "ML Engineer",
    "DevOps Specialist", "Frontend Developer"
]

def generate_profiles(n=100):
    profiles = []
    for i in range(n):
        skills = random.sample(skills_pool, random.randint(2, 5))
        profiles.append({
            "id": str(i),
            "name": fake.name(),
            "title": random.choice(titles),
            "skills": skills,
            "experience": f"{random.randint(1, 10)} years in {random.choice(skills)}",
            "summary": f"{fake.job()} specializing in {' and '.join(skills)}. {fake.paragraph()}"
        })
    return profiles