import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="go-analyser", # Replace with your own username
    version="0.0.1",
    author="Katsubo Stas",
    author_email="stasio850@gmail.com",
    description="lab 2, Go analysis",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Windmaiden/Metaprogramming",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            'go-analysis=go.main:main',
        ],
    },
    python_requires='>=3.6',
)