from setuptools import setup, find_packages

setup(
    name="enigma",
    version="1.0",
    description="3 rotors eniguma machine simulater",
    author="kazumamatsu",
    url = "https://github.com/kazumamatsu/enigma_sim.git",
    packages=find_packages(),
    requires=["string","random","sys"],
)
