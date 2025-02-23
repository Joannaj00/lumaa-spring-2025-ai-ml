from setuptools import setup, find_packages

setup(
    name="perfume_recommender",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "numpy>=1.24.3",
        "pandas>=2.0.3",
        "scikit-learn>=1.3.0",
        "nltk>=3.8.1",
    ],
)
