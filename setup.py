from setuptools import setup, find_packages

setup(
    name='documentation',
    author='insurgency.gg',
    packages=find_packages(),
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Framework :: Sphinx',
        'Topic :: Documentation',
        'Topic :: Documentation :: Sphinx',
    ],
    install_requires=[
        'Sphinx',
        'git+https://github.com/agronholm/sphinx-autodoc-typehints.git@2dae2d685a5edf82c1ee3d919ff9434c2a1622f8#egg'
        '=sphinx-autodoc-typehints',
    ],
)
