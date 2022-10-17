from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()
    
print(requirements)

setup(
        name="image_create",
        version="0.0.2",
        author="wagner_gama",
        author_email="wagner@dealinformatica.info",
        description="pacote para criação de imagens",
        long_description=page_description,
        long_description_content_type="text/markdown",
        url="https://github.com/wagnergama/package_image_create",
        packages = find_packages,
        install_requires=requirements,
        python_requires='>=3.8',
    )
