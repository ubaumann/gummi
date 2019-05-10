import setuptools
import gummi.constants

with open("README.md", "r") as rea:
    long_description = rea.read()

with open('requirements.txt', 'r') as req:
    lines = req.readlines()
    requirements = [l.strip().strip('\n')
                    for l in lines if l.strip() and not l.strip().startswith('#')]

setuptools.setup(
    name=gummi.constants.BINARY_NAME,
    version=gummi.constants.PROGRAM_VERSION,
    author="sebastian",
    author_email="sebastian.hug@outlook.com",
    description="Manage your LaTeX templates with ease.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/seboschtion/gummi",
    packages=setuptools.find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            '%s = gummi.main:main' % gummi.constants.BINARY_NAME
        ]
    },
)
