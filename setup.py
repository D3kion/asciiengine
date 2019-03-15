from setuptools import setup

setup(
    name='asciiengine',
    version='0.0.1',
    description='ASCII game engine based on Pygame',
    keywords='ascii game engine pygame roguelike text adventures',
    url='https://github.com/D3kion/asciiengine',
    author='D3kion',
    author_email='dekion@protonmail.com',
    license='MIT',
    packages=['asciiengine'],
    install_requires=[
        'pygame',
    ],
    zip_safe=False,
)
