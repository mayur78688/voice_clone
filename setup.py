from setuptools import setup, find_packages

setup(
    name='new',
    version='0.1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'your_script_name = your_package.module:main_function',
        ],
    },
    author='mayur',
    author_email='mayur900mane@gmail.com',
    description='A short description of your project',
    long_description='A longer description of your project',
    url='https://github.com/mayur78688/voice_clone.git',
    
)
