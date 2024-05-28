from setuptools import find_packages,setup

setup(
    name='mcqgenerator',
    version='0.0.1',
    author= 'sridhar Jakkaraju',
    author_email='bharnikumar@gmail.com',
    install_requires=("openai","langchain","stremlit","python-dotenv","PyPDP2"),
    packages=find_packages()
)