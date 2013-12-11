from distutils.core import setup

# Dynamically calculate the version based on odd_utilities.VERSION
version_tuple = __import__('odd_utilities').VERSION
version = '.'.join([str(v) for v in version_tuple])

setup(
    name='Odd Utilities',
    version=version,
    author_email='GEWebDevTeam@govexec.com',
    packages=['odd_utilities'],
    url='https://github.com/Govexec/django-odd-utilities',
    description="Various utilities and widgets used in our other apps.",
    long_description=open('README.rm').read(),
    install_requires=[
        "Django >= 1.3",
    ]
)