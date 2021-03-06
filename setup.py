from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'python-dateutil'
]

test_requirements = []

setup(
    name='python-reporter-app',
    version='0.1.2',
    author='Myles Braithwaite',
    author_email='me@mylesbraithwaite.com',
    description='A Python Library for Reporter App.',
    keywords='reporterapp',
    url='https://github.com/myles/python-reporter-app',
    packages=['reporter-app'],
    package_dir={'reporter-app': 'reporterapp'},
    include_package_data=True,
    long_description=readme,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
    ],
    license='MIT license',
    install_requires=requirements,
    extras_require={
        'dropbox': ['dropbox'],
        'cli': ['click']
    },
    entry_points="""
        [console_scripts]
        reporter-app=reporterapp.cli:cli
    """,
    zip_safe=False,
    test_suite='tests',
    tests_require=test_requirements
)
