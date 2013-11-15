"""Scaffold installation script.
"""
import os
from setuptools import setup
from setuptools import find_packages


here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
CHANGES = open(os.path.join(here, 'CHANGES.rst')).read()


setup(name='pyramid_lxneng',
      version='1.3.1',
      description='pyramid_lxneng pyramid scaffold',
      long_description=README + '\n\n' + CHANGES,
      author='Eric Lo',
      author_email='lxneng@gmail.com',
      url='https://github.com/lxneng/pyramid_lxneng',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      install_requires=['pyramid', 'webhelpers'],
      include_package_data=True,
      zip_safe=False,
      entry_points="""\
      [pyramid.scaffold]
      lxneng_sqlalchemy = pyramid_lxneng.scaffolds:SQLAlchemyProjectTemplate
      lxneng_mongoengine = pyramid_lxneng.scaffolds:MongoEngineProjectTemplate
      lxneng_plugin = pyramid_lxneng.scaffolds:PluginProjectTemplate
      """,
      )
