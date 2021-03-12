import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="travail_2_-_overwatch",  # Replace with your own username
    version="0.0.1",
    author="Dan Levy",
    author_email="danlevy.ca@icloud.com",
    description="Initiation à bootstrap - Travail 2.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/levydanqc/travail-2-overwatch.git",
    project_urls={
        "Bug Tracker": "https://gitlab.com/levydanqc/travail-2-overwatch/-/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
)
