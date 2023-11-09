import subprocess
def rgb_to_yuv(R, G, B): #exercise 1.1
    Y = R *  .257 + G *  .0504 + B *  .098 + 16
    U = R * -.148 + G * -.291 + B *  .439 + 128
    V = R *  .439 + G * -.368 + B * -.071 + 128
    return Y, U, V

def yuv_to_rgb(Y, U, V): #exercise 1.2
    R = 1.164 * (Y - 16) + 1.596 * (V - 128)
    G = 1.164 * (Y - 16) - 0.813 * (V - 128) - 0.391 * (U - 128)
    B = 1.164 * (Y - 16) + 2.018 * (U - 128)
    return R, G, B

# Example usage:
R, G, B = 255, 0, 0  # Replace these values with your RGB values
Y, U, V = rgb_to_yuv(R, G, B)
print(f"RGB to YUV: Y={Y}, U={U}, V={V}")

# Example usage for YUV to RGB:
y, u, v = 76, 84, 255  # Replace these values with your YUV values
r, g, b = yuv_to_rgb(y, u, v)
print(f"YUV to RGB: R={R}, G={G}, B={B}")

def resize_image(input_image,output_image,width,height,quality): #exercise 2
    # Run the ffmpeg command
    subprocess.run(f"ffmpeg -i {input_image} -vf scale={width}:{height} -q:v {quality} {output_image}", shell=True, check=True)
#Example usage
input_image = 'dog.jpg'
output_image = 'dog_resized.jpg'
width = 800
height = 600
quality = 5 #Desired quality (1-31, where 1 is the highest quality)
resize_image(input_image,output_image,width,height,quality)
def serpentine(file_path): #exercise3
    with open(file_path, 'rb') as file:
        # Read the entire file into a bytes object
        jpeg_bytes = file.read()

    # Extract the image data
    image_data = jpeg_bytes[2:]

    # Initialize variables for zigzag pattern
    rows, cols = 0, 0
    width = 0
    height = 0

    while len(image_data) > 0:
        # Read and process the byte at the current position
        current_byte = image_data[:1]

        # Do something with the current_byte, for example, print it
        print(current_byte[0], end=' ')

        # Move to the next position in zigzag pattern
        if (rows + cols) % 2 == 0:
            if cols < width - 1:
                cols += 1
            else:
                rows += 1
            if rows > height - 1:
                rows = height - 1
                cols += 2
            if cols > width - 1:
                cols = width - 1
        else:
            if rows < height - 1:
                rows += 1
            else:
                cols += 1
            if cols > width - 1:
                cols = width - 1
            if rows > height - 1:
                rows = height - 1
                cols += 2

        # Remove the processed byte from the image data
        image_data = image_data[1:]

# Usage example
serpentine("dog.jpg")

def resize_image(input_image,output_image,width,height,quality): #exercise 4
    # Run the ffmpeg command
    subprocess.run(f"ffmpeg -i {input_image} -vf format=gray -c:v mjpeg -q:v 1 {output_image}", shell=True, check=True)

#Example usage
input_image = 'dog.jpg'
output_image = 'dog_bw.jpg'

resize_image(input_image,output_image,width,height,quality)
#here we see that using the lowest quality setting will result in a highly compressed image with significant loss of image quality.

def run_length_encode(data): #exercise 5
    encoded_data = bytearray()
    i = 0

    while i < len(data):
        count = 1
        while i + 1 < len(data) and data[i] == data[i + 1]:
            count += 1
            i += 1
        encoded_data.append(count)
        encoded_data.append(data[i])
        i += 1

    return encoded_data

def run_length_decode(encoded_data):
    decoded_data = bytearray()
    i = 0

    while i < len(encoded_data):
        count = encoded_data[i]
        value = encoded_data[i + 1]
        decoded_data.extend([value] * count)
        i += 2

    return decoded_data

# Example usage:
original_data = bytearray([1, 1, 1, 2, 2, 3, 3, 3, 3, 4])
encoded_data = run_length_encode(original_data)
print("Encoded data:", encoded_data)
decoded_data = run_length_decode(encoded_data)
print("Decoded data:", decoded_data)


#exercise 6
import numpy as np
from scipy.fftpack import dct, idct


class DCTConverter:
    def __init__(self):
        pass

    def dct(self, data):
        return dct(data, type=2, norm='ortho')

    def idct(self, data):
        return idct(data, type=2, norm='ortho')


# Example usage:
if __name__ == "__main__":
    dct_converter = DCTConverter()

    # Sample input data
    input_data = np.array([1, 2, 3, 4, 5, 6, 7, 8])

    # Perform DCT on the input data
    dct_result = dct_converter.dct(input_data)
    print("DCT result:", dct_result)

    # Perform IDCT on the DCT result to reconstruct the original data
    reconstructed_data = dct_converter.idct(dct_result)
    print("Reconstructed data:", reconstructed_data)
