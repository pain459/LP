import os

def create_wheel_setup(project_name):
    # Define content for setup.py and MANIFEST.in
    files = {
        f"{project_name}/setup.py": setup_content(project_name),
        f"{project_name}/MANIFEST.in": manifest_content(),
        f"{project_name}/README.md": readme_content(),
    }

    # Create files with content
    for file_path, content in files.items():
        with open(file_path, 'w') as f:
            f.write(content)
    
    print(f"Setup for wheel distribution created successfully in {project_name}.")

def setup_content(project_name):
    return f'''\
from setuptools import setup, find_packages

setup(
    name="{project_name}",
    version="0.1.0",
    description="A FastAPI CRUD application",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/yourusername/{project_name}",
    packages=find_packages(),
    install_requires=[
        "fastapi",
        "sqlalchemy",
        "pydantic",
        "uvicorn[standard]",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    entry_points={{
        "console_scripts": [
            "{project_name}_app = {project_name}.main:app",
        ],
    }},
    include_package_data=True,
)
'''

def manifest_content():
    return '''\
include README.md
include requirements.txt
'''

def readme_content():
    return '''\
# FastAPI CRUD Application

This is a simple FastAPI CRUD application for demonstration purposes.
'''

if __name__ == "__main__":
    project_name = input("Enter your project name: ")
    create_wheel_setup(project_name)
