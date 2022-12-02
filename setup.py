from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in demoapp/__init__.py
from demoapp import __version__ as version

setup(
	name="demoapp",
	version=version,
	description="It is a Demo app",
	author="Rohith",
	author_email="rohith@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
