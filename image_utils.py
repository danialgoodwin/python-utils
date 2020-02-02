#!/usr/bin/env python

from pathlib import Path
# Source: `pip install Wand`
from wand.image import Image


def resize_image(
        input_image_path: Path,
        output_image_path: Path,
        new_width: int = 1920,
        new_height: int = 1080,
        is_add_size_to_image_name: bool = True
):
    with Image(filename=str(input_image_path)) as input_image:
        # print(img.size)
        with input_image.clone() as output_image:
            output_image.resize(new_width, new_height)
            if is_add_size_to_image_name:
                output_image.save(filename=f'{output_image_path.parent}/{output_image_path.stem}_{new_width}x{new_height}{output_image_path.suffix}')
            else:
                output_image.save(filename=output_image_path)


def resize_images(input_path: Path, output_path: Path, file_glob: str = '*.jpg', new_width: int = 1920, new_height: int = 1080):
    print(f'resize_images(), input_path={input_path}, output_path={output_path}')
    output_path.mkdir(parents=True, exist_ok=True)
    for image in input_path.glob(file_glob):
        print(f'    image={image}')
        resize_image(image, Path(f'{output_path}/{image.name}'), new_width, new_height)


def main():
    print('main()')
    # resize_images(Path('~/Desktop/roku-vintage-dogs-original'))
    # resize_images('C:\\Users\\goodwin\\Desktop\\roku-vintage-dogs-original', '.', )


if __name__ == '__main__':
    main()
