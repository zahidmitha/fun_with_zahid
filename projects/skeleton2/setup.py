try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
		'description' : 'My Project',
		'author' : 'Zahid',
		'url' : 'URL to get it at',
		'download_url' : 'Where to download it.',
		'author_email' : 'zahidazimmitha@gmail.com',
		'version' : '0.1',
		'install_requires' : ['nose'],
		'packages' : [],
		'scripts' : ['bin/adi.py'],
		'name' : 'projectname',
		'install_requires' : ["numpy"]
}

setup(**config)

