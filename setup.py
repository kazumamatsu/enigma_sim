import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="enigma",
    version="1.0",
    author="kazumamatsu",
    author_email,
    description="This is 3rotors enigma sim",
    url="https://github.com/kazumamatsu/enigma_sim",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points = {
        'console_scripts': ['enigma = enigma.Enigma_simulater:main']
    },
    python_requires='>=3.7',
)
