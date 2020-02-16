import setuptools

with open("README.rst", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="lieutenant-commander-melnaquib", # Replace with your own username
    version="0.0.1",
    author="Mustafa Elnaquib",
    author_email="melnaquib@gmail.com",
    description="help talk to Linux for BioInformatics",
    long_description=long_description,
    url="https://github.com/melnaquib/ltcmdr",
    packages=setuptools.find_packages(),
    entry_points={
          'console_scripts': [
              'lcdr = lcdr.__main__:main'
          ]
      },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: AGPLv3 License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)