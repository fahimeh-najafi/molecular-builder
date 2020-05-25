import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="molecular_builder",
    version="0.1.0",
    author="Henrik Andersen Sveinsson",
    author_email="henriasv@fys.uio.no",
    description="Package for building moleular systems",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/henriasv/molecular-builder",
    include_package_data=True,
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=["ase", "requests", "requests-cache", "clint", "werkzeug","cython", "recommonmark"],
    python_requires='>=3.6',
)
