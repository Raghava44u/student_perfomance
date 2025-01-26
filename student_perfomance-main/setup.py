from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path: str) -> List[str]:
    '''
    Function to return a list of requirements
    '''
    HYPEN_E_DOT = '-e .'
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name='student_performance',
    version='0.0.1',
    author='Raghava',
    author_email='raghavadasari44@gmail.com',
    packages=find_packages(),  # Corrected: Added parentheses to call the function
    install_requires=get_requirements('requirements.txt')
)
