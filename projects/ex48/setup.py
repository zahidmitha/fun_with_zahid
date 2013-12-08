try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
		'description' : 'ex48v2',
		'author' : 'Zahid',
		'url' : 'URL to get it at',
		'download_url' : 'Where to download it.',
		'author_email' : 'zahidazimmitha@gmail.com',
		'version' : '0.1',
		'install_requires' : ['nose'],
		'packages' : [],
		'scripts' : [],
		'name' : 'ex48v2',
}

setup(**config)

