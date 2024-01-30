from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
    
setup(
    name='commitcleaner',
    version='0.6.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'commitcleaner=commitcleaner.cleaner:main',
        ],
    },
    author='Yonghye Kwon',
    author_email='developer.0hye@gmail.com',
    description='A tool to clean Git commit history.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords='git commit clean',
    url='https://github.com/developer0hye/commitcleaner',
)
