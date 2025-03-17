from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="image_processing_ferreedu",
    version="0.0.1",
    author="Eduardo da Silva Ferreira",
    author_email="eduardo.s.ferreira@gmail.com",
    description="Image processing package. This project belongs to Karina Tiemi Kato, Tech Lead, Machine Learning Engineer, Data Scientist Specialist at Take. This package is a demo for simulation of upload on the Test Pypi website, and it's from the Bootcamp developer full stack Python class. E-mail: karinatkato@gmail.com.",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ferreirasilvaeduardo/image-processing-package-ferreedu",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.11',
)