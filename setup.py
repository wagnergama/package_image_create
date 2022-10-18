from setuptools import setup

setup(
    name='image_create',
    version='0.0.3',
    author="wagner_gama",
    author_email="wagner@dealinformatica.info",
    description="pacote para criação de imagens",
    install_requires=[
        'Pillow==9.2.0',
        'importlib-metadata; python_version == "3.10"',
    ],
)
