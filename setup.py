#!/usr/bin/env python
 
import sys, os
from setuptools import setup, find_packages
 
setup(
        name = "MegaWiki",
        version = "0.1",
        description = "A powerful Wiki example!",
        author = "Your Name Here",
        author_email = "Your E-Mail Here",
        license = "MIT",
        packages = find_packages(),
        include_package_data = True,
        paster_plugins = ['PasteScript', 'WebCore'],
        install_requires = ['WebCore', 'SQLAlchemy', 'Beaker', 'Genshi', 'textile']
    )
