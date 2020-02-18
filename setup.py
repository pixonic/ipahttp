from setuptools import setup

setup(name='ipahttp',
      version='0.3.2',
      description='module for http API IPA',
      url='https://github.com/pixonic/ipahttp',
      author='Pixonic Team',
      author_email='adm-srv@pixonic.com',
      license='MIT',
      packages=['ipahttp'],
      install_requires=[
            'requests',
            'pyyaml'
        ],
      zip_safe=False)
