from setuptools import setup, find_packages, Extension

with open("README.md","r", encoding = 'utf-8') as fp:
	readme = fp.read()

setup(
	name="separability-index",
	version="0.1.0",
	description="An index to assess how separable two two-component datasets are.",
	author="A. Renmin Pretell Ductram, Scott J. Brandenberg",
	author_email="rpretell@unr.edu, sjbrandenberg@g.ucla.edu",
	url="https://github.com/RPretellD/separability-index",
    long_description=readme,
    
    packages=find_packages(),
	include_package_data=True,
	
    install_requires=["numpy"],

	license="MIT",
	keywords="separability",
	classifiers=[
        "Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
	]
)