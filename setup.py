from setuptools import setup, find_packages

setup(
    name="enigma",
    version="1.0",
    description="3 rotors eniguma machine simulater",
    author="kazumamatsu",
    url = "https://github.com/kazumamatsu/enigma_sim.git",
    packages=setuptools.find_packages("enigma_simulater"),
    requires=["string","random","sys"],
    packages=find_packages(),
)
