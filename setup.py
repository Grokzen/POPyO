try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

settings = {}

settings.update(
    name = "popo",
    version = "0.1.0",
    description = "Plain Old Python Object - for Django",
    long_description = '',
    author = "Grokzen@gmail.com",
    author_email = "Grokzen@gmail.com",
    packages = ['popo'],
    scripts = [],
    data_files = [],
    install_requires = [],
    classifiers = (
        'Development Status :: 1 - Alpha',
        'Environment :: Django',
        'Environment :: Web Environment',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python :: 2.7.x',
        'Topic :: Documentation',
        'Topic :: Software Development :: Documentation',
        'Topic :: Text Processing ',
        )
    )

setup(**settings)
