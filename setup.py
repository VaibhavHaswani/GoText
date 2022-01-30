import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gotext",
    version="1.0",
    author="Vaibhav Haswani",
    author_email="vaibhavhaswani@gmail.com",
    description="GoText is a universal text extraction and preprocessing tool for python which supportss wide variety of document formats.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/VaibhavHaswani/GoText",
    project_urls={
        "Bug Tracker": "https://github.com/VaibhavHaswani/GoText/issues",
    },
    download_url = 'https://github.com/VaibhavHaswani/GoText/archive/refs/tags/v1.0.tar.gz',    # I explain this later on
    keywords = ['text extraction','text preprocessing','document extraction','text utils'],   # Keywords that define your package best
    install_requires=[            # I get to this in a second
          'textract-plus',
      ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GPL 3.0 License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "gotext"},
    packages=setuptools.find_packages(where="gotext"),
    python_requires=">=3.6",
)