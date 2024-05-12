from PIL import Image
import io
import base64
import numpy as np
from pydantic import BaseModel
class ORC_Check(BaseModel):
    image:str
def encode_numpy_array_to_base64(image_np):
    # Convert the NumPy array to PIL Image
    image_pil = Image.fromarray(image_np)

    # Create an in-memory stream to hold the image data
    img_byte_array = io.BytesIO()

    # Save the image to the in-memory stream in PNG format
    image_pil.save(img_byte_array, format='PNG')

    # Encode the image data to Base64
    base64_encoded = base64.b64encode(img_byte_array.getvalue())

    # Decode bytes to string
    base64_string = base64_encoded.decode('utf-8')

    return base64_string

def decode_base64_to_numpy(base64_string):
    # Decode the Base64 string into bytes
    image_bytes = base64.b64decode(base64_string)

    # Create a BytesIO object to wrap the decoded bytes
    image_stream = io.BytesIO(image_bytes)

    # Open the image using PIL
    img_pil = Image.open(image_stream)

    # Convert PIL Image to NumPy array
    image_np = np.array(img_pil)

    return image_np


if __name__ == '__main__':
    image_path = r"main\WIN_20240404_07_18_34_Pro.jpg"
    pil_image = Image.open(image_path)
    pil_image  = Image.fromarray(decode_base64_to_numpy(encode_numpy_array_to_base64(np.asarray(pil_image,np.uint8))))
    pil_image.show()