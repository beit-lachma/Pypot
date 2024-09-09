from setuptools import setup, find_packages

def readme_file_contents():
    with open('README.rst') as readme_file:
        data = readme_file.read()
    return data

setup(
    name='pypot',
    version='1.0.0',
    description='Simple TCP honeypot',
    long_description=readme_file_contents(),
    author='beth',
    author_email='beth131313131313@gmail.com',
    license='MIT',
    packages=find_packages(),
    zip_safe=False,
    install_requires=[]
)