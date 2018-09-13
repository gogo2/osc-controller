import setuptools

with open("README.md", "r") as rdme:
    long_description = rdme.read()

setuptools.setup(
    name="osc-controller",
    version="0.3.0",
    author="Bartosz Sobol",
    author_email="bartoszmsobol@gmail.com",
    description="Simple library for creating osc software in python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gogo2/osc-controller",
    packages=setuptools.find_packages(),
    platforms='any',
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
