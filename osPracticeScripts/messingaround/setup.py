from setuptools import setup

setup(name='funniest',
      description='buildtest',
      install_requires=[
      	'nose',
            'paver',
            'coverage',
      ],
      zip_safe=False,
      test_suite='nose.collector',
      tests_require=['nose'],
      )