from setuptools import setup, find_packages
from typing import List

def get_requirements() -> List[str]:
    "This function will return the list of requirements "

    requirements_lst: List[str] = []
    try:
        with open("requirements.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                requirements=line.strip()
                if requirements.startswith("-e ."):
                    continue
                else:
                    requirements_lst.append(requirements)
    except FileNotFoundError:
        print("The requirements.txt file is not found.")

    return requirements_lst


setup(
    name="Network_security_project",
    version="0.1.0",
    author="Parag",
    author_email="",
    packages=find_packages(),
    install_requires=get_requirements(),
)