from setuptools import setup

# reading long description from file
with open('DESCRIPTION.txt') as file:
    long_description = file.read()


# specify requirements of your package here
REQUIREMENTS = ['pygame', 'flask', 'threading', 'RPI.GPIO', 'time']

# some more details
CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Internet',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    ]

# calling the setup function 
setup(name='ovalert',
      version='1.0.0',
      description='An alarm system for system TRACY ',
      long_description=long_description,
      url='www.google.com',
      author='HSC',
      author_email='hansonchan@ophyllaventures.com',
      license='MIT',
      packages=['alert'],
      classifiers=CLASSIFIERS,
      install_requires=REQUIREMENTS,
      keywords='alarm rpi'
      )
