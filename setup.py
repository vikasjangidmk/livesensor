from setuptools import find_packages, setup



def get_requirements()->list[str]:
    requirements_list = list[str] = []
    return requirements_list





setup(
name='Sensor',
version="0.0.1",
author="Vikas",
author_email="vikasjangidmk@gmail.com",
packages=find_packages(),
    install_requires = get_requirements(), #["pymongo"]
    
)