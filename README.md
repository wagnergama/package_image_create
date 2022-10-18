# image_create

Description. 
The package image_create is used to:
	- create random images automatically
	- Requirement package Pillow 9.2

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install image_create

```bash
pip install -i https://pypi.org/simple/ image-create, Pillow
```

## Usage

```python
from image_create import create_image
create_image.create_background(target_size_px = int, color_background = tuple(R,G,B), padding = int, path = str )
```

## Author
Wagner Gama

## License
[MIT](https://choosealicense.com/licenses/mit/)