from setuptools import setup, find_packages

setup(
    name="ml_config",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["omegaconf"],
    author="Ruslan Mamedov",
    description="Reusable YAML + CLI config loader for ML projects",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    python_requires='>=3.7',
)
