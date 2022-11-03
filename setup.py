import setuptools

setuptools.setup(
    name="enigma",
    version="1.0",
    author="kazumamatsu",
    entry_points = {
        'console_scripts': ['enigma = enigma.enigma_simulater:enigma']
    }
)
