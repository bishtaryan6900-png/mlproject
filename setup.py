from setuptools import find_packages, setup
from typing import List

hp = '-e .'

def get_requirements(file_path: str) -> List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n', '') for req in requirements]
        if hp in requirements:
            requirements.remove(hp)

    return requirements

setup(
    name='mlprojects',
    version='0.0.1',
    author='aryan',
    author_email='bisht.aryan6900@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
