from setuptools import setup
from setuptools import find_packages

with open("README.md", "r") as f:
    page_description = f.read()

setup(
    name='image_create',
    version='0.0.1',
    author="wagner_gama",
    author_email="wagner@dealinformatica.info",
    description="pacote para criação de imagens",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/wagnergama/package_image_create",
    packages=find_packages(include=['image_create']),
    python_requires= '>=3.10'
)