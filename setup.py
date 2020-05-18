from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
	long_description = readme_file.read()

setup(
	name="expofire",
	version="1.0",
	url="https://github.com/nullr3x/ExpoFire",
	description="A simple Python Exploit to Write Data to Insecure/vulnerable firebase databases! ",
	long_description=long_description,
	long_description_content_type="text/markdown",
	author="Sahil Mehra",
	author_email="sahilmehra9896@gmail.com",
	license="MIT",
	keywords="Firebase DB Exploit",
	packages=["firebase", "firebase.modules"],
	install_requires=['requests', 'setuptools'],
	entry_points={
		'console_scripts':[
			'expofire = firebase.__main__:expofire'
		],
	},
)
