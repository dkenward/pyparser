from setuptools import setup, find_packages
#import versioneer

DISTNAME = 'mylib'
LICENSE = 'GPL'
AUTHOR = "The MyLib Development Team"
EMAIL = "ouremail@emails.com"
URL = "bitbucket.com"
DOWNLOAD_URL = ''
CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Environment :: Console',
    'Operating System :: OS Independent',
    'Intended Audience :: Science/Research',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Cython',
    'Topic :: Scientific/Engineering']

VERSION = 0.1
DESCRIPTION = ("Short description")
LONG_DESCRIPTION = """
This is a long description of the api
"""

setup(name=DISTNAME,
      maintainer=AUTHOR,
      #version=versioneer.get_version(),
      version=VERSION,
      packages=find_packages(include=['mylib', 'mylib.*']),
      package_data={'': ['templates/*', '_libs/*.dll']},
      #ext_modules=maybe_cythonize(extensions, compiler_directives=directives),
      maintainer_email=EMAIL,
      description=DESCRIPTION,
      license=LICENSE,
      #cmdclass=cmdclass,
      url=URL,
      download_url=DOWNLOAD_URL,
      long_description=LONG_DESCRIPTION,
      classifiers=CLASSIFIERS,
      platforms='any',
      #python_requires='>=2.7,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*,!=3.4.*',
      #**setuptools_kwargs
      )
