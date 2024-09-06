from setuptools import setup


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
    author_email='ybeti1621@gmail.com',
    license='MIT',
    packages=['pypot'],
    zip_safe=False,
    install_requires=[]
)
