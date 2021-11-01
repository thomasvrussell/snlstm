from setuptools import setup, find_packages

DESCRIPTION = "LSTM model for spectroscopic studies of type Ia supernovae"
LONG_DESCRIPTION = open('README.rst').read()
NAME = "snlstm"
AUTHOR = "Lei Hu"
AUTHOR_EMAIL = "hulei@pmo.ac.cn"
MAINTAINER = "Lei Hu"
MAINTAINER_EMAIL = "hulei@pmo.ac.cn"
DOWNLOAD_URL = 'https://github.com/thomasvrussell/snlstm'
LICENSE = 'MIT Licence'
VERSION = '1.0.1'

install_reqs = ['scipy>=1.5.2',
                'astropy>=4.0.2',
                'glob2>=0.7',
                'scikit-learn>=0.23.2',
                'tensorflow==1.14.0',
                'pyphot==1.1']

setup(name = NAME,
      version = VERSION,
      description = DESCRIPTION,
      long_description = LONG_DESCRIPTION,
      long_description_content_type='text/markdown',
      setup_requires = ['numpy'],
      install_requires = install_reqs,
      author = AUTHOR,
      author_email = AUTHOR_EMAIL,
      maintainer = MAINTAINER,
      maintainer_email = MAINTAINER_EMAIL,
      download_url = DOWNLOAD_URL,
      license = LICENSE,
      packages = find_packages(),
      include_package_data = True,
      classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Scientific/Engineering :: Astronomy'],
     )
