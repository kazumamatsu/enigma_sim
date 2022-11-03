import setuptools

setuptools.setup(
    name="enigma",
    version="1.0",
    description="3rotors eniguma machine simulater",
    author="kazumamatsu",
    url = "https://github.com/kazumamatsu/enigma_sim.git",
    entry_points = {
        'console_scripts': ['enigma = enigma.enigma_simulater:enigma']
    }
)
