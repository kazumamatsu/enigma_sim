import setuptools

setuptools.setup(
    name="enigma",
    version="1.0",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points = {
        'console_scripts': ['enigma = enigma.Enigma_simulater:main']
    }
)
