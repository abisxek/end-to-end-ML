from setuptools import setup,find_packages
from typing import List

HYPHEN_E_DOT='-e .'
def get_requirements(file_path:str)-> List[str]:  #file_path is of type str and -> means it will return a List[str] in str format
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open('requirements.txt') as file:
        requirements=file.readlines()
        requirements=[req.replace("\n"," ")for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements        


setup(
    name='mlproject',
    version='0.0.1',
    author='Abishek R',
    author_email='abisxek@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)