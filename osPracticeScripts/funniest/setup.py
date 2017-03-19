from setuptools import setup

setup(name='funniest',
      version='0.1',
      description='The funniest joke in the world',
      url='http://github.com/storborg/funniest',
      author='Flying Circus',
      author_email='flyingcircus@example.com',
      license='MIT',
      packages=['funniest'],
      install_requires=[
      	'markdown',
      ],
      zip_safe=False,
      scripts=['bin/funniest-joke'],
      entry_points={
      	'console_scipts':['funniest-joke=funniest.command_line:main']
      },
      test_suite='nose.collector',
      tests_require=['nose'],
      )