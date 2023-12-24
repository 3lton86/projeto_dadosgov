from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="projeto_eltonfernandes",
    version="0.0.1",
    author="Elton Fernandes",
    author_email="eltonfernandes.ti@gmail.com",
    description="My short description",
    long_description=page_description,
    long_description_content_type="text/markdown",
    #url="git@github.com:3lton86/projeto_dadosgov.git"
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)