from PIL import Image


def resize_image(size1, size2):

    image = Image.open('mypicture.png')

    print(f"Current size : {image.size}")
    resized_image = image.resize((size1, size2))

    resized_image.save('mypicture-'+str(size1)+'.png')


size1 = int(input('Enter width: '))
size2 = int(input('Enter length: '))
resize_image(size1, size2)