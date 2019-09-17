
'''
montra-client-python - Montra API wrapper client for Python
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**montra-client-python** is a Python client for the Montra API.
Install it with::
    $ pip install montra-client-python
And learn to use it by reading the `documentation`_.
:copyright: (c) 2019, Universidade de Aveiro, DETI/IEETA, Bioinformatics Group - http://bioinformatics.ua.pt/
Resources
^^^^^^^^^
* `Documentation <https://github.com/bioinformatics-ua/montra-client-python>`_
* `Issue Tracker <https://github.com/bioinformatics-ua/montra-client-python/issues>`_
* `Code <https://github.com/bioinformatics-ua/montra-client-python>`_
'''


import sys
import setuptools
from distutils.core import setup


if sys.version_info < (2, 7):
    raise NotImplementedError('Sorry, you need Python 2.7 to use montra-client')


# We cannot simply import becas; becas.__version__ because requests might
# not be installed and we would fail with an ImportError
def get_version(filepath='montra.py'):
    import re
    VERSION_REGEX = re.compile(r"^__version__ = '(\d+\.\d+(-dev)?)'$")

    with open(filepath, 'rt') as infile:
        for line in infile:
            match = VERSION_REGEX.match(line)
            if match:
                return match.group(1)
    raise ValueError("Could not find version in file %s" % filepath)


with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='montra',
      version=get_version(),
      description='Montra API client wrapper for Python.',
      long_description=long_description,
      long_description_content_type="text/markdown",
      author='Pedro Freire',
      author_email='pedrofreire@ua.pt',
      license='CC-BY-NC',
      url='https://github.com/bioinformatics-ua/montra-client-python',
      download_url='https://github.com/bioinformatics-ua/montra-client-python/tags',
      bugtrack_url='https://github.com/bioinformatics-ua/montra-client-python/issues',
      install_requires=['requests>=1.2.0'],
      py_modules=['montra'],
      scripts=['montra.py'],
      platforms='any',
      setup_requires=['wheel'],
      classifiers=[
          'Intended Audience :: Science/Research',
          'Intended Audience :: Developers',
          'Topic :: Software Development',
          'Topic :: Scientific/Engineering',
          'Topic :: Scientific/Engineering :: Bio-Informatics',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.7'],
      keywords=[
          'montra',
          'biomedical',
          'database',
          'catalogue',
          'ehden',
      ],
)