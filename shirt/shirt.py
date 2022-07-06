from PIL import Image, ImageOps
import sys
import os

def main():

    if len(sys.argv) != 3:
        sys.exit("Wrong number of arguments.")

    put_shirt(sys.argv[1], sys.argv[2])

   

def put_shirt(original_picture_path, result_picture_path):
    supported_extensions = [".jpg", ".jpeg", ".png"]
    _, input_ext = os.path.splitext(original_picture_path)
    _, output_ext = os.path.splitext(result_picture_path)
   
    if input_ext.lower() != output_ext.lower():
        raise ValueError("Input and output files doesn`t have the same extensions.")

    if input_ext.lower() not in supported_extensions:
        raise ValueError("Wrong file extension.")

    original_picture = Image.open(original_picture_path)

    shirt_picture = Image.open("shirt.png")
    shirt_size = shirt_picture.size
    
    result_picture = ImageOps.fit(original_picture, shirt_size)
    
    result_picture.paste(shirt_picture, shirt_picture)
    result_picture.save(result_picture_path)


if __name__ == "__main__":
    main()