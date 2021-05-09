from distutils.core import setup


with open("README.md") as f:
    long_description = f.read()


setup(
    name="bug-free-game",
    version="0.0.0",
    description="A game which is totally free of bugs",
    long_description=long_description,
    packages=["bug-free-game"],
    install_requires=["pyglet"],
)
