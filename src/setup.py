"""Create distribution for the Weather Server application
"""

from setuptools import setup, find_packages

setup(
    name='weatherserver',
    version='0.1.0',
    description='Fake Weather Server',
    author='grzes71',
    author_email='grafi71@o2.pl',
    license='MIT',
    packages=find_packages(),
    entry_points={
                    'console_scripts': ['weatherserver=weatherserver.main:main', ],
    },
    zip_safe=True
)
