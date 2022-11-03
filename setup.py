import setuptools

setuptools.setup(
    name="enigma",
    version="1.0",
    entry_points = {
        'console_scripts': ['enigma = enigma.Enigma_simulater:enigma']
    }
)
