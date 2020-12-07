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
        'sphinx-autodoc-typehints @ git+https://github.com/tillhainbach/sphinx-autodoc-typehints.git@master#egg'
        '=sphinx-autodoc-typehints',
        'sphinx-autobuild',
    ],
)
