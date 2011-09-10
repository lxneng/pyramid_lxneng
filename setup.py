"""Scaffold installation script.
"""
import os
import re
from setuptools import setup
from setuptools import find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
CHANGES = open(os.path.join(here, 'CHANGES.rst')).read()
version = '1.0'

setup(name='pyramid_lxneng',
      version=version,
      description='pyramid_lxneng pyramid scaffold',
      long_description=README + '\n\n' + CHANGES,
      author='Eric Lo',
      author_email='lxneng@gmail.com',
      url='http://lxneng.com',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      install_requires=['pyramid'],
      include_package_data=True,
      zip_safe=False,
      entry_points="""\
      [paste.paster_create_template]
      pyramid_lxneng = pyramid_lxneng.paster_templates:ProjectTemplate
      """,
      )