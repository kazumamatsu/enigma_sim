import setuptools

setuptools.setup(
    name="enigma",
    version="1.1",
    description="3rotors eniguma machine simulater",
    author="kazumamatsu",
    url = "https://github.com/kazumamatsu/enigma_sim.git",
    packages=setuptools.find_packages("enigma_simulater"),
    requires=["string","random","sys"],
    entry_points = {
        'console_scripts': ['enigma = enigma.__init__']
    }
)
