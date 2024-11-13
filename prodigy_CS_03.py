from PIL import Image
import numpy as np

# Function to encrypt an image using XOR operation
def encrypt_image(input_image_path, output_image_path, key):
    # Open the image and convert to numpy array
    img = Image.open(input_image_path)
    img_array = np.array(img)
    
    # Encrypt the image using XOR with the key
    encrypted_array = img_array ^ key
    
    # Convert back to Image object
    encrypted_img = Image.fromarray(encrypted_array)
    
    # Save the encrypted image
    encrypted_img.save(output_image_path)
    print(f"Image encrypted and saved as {output_image_path}")

# Function to decrypt an image using XOR operation
def decrypt_image(input_image_path, output_image_path, key):
    # Open the image and convert to numpy array
    img = Image.open(input_image_path)
    img_array = np.array(img)
    
    # Decrypt the image using XOR with the same key
    decrypted_array = img_array ^ key
    
    # Convert back to Image object
    decrypted_img = Image.fromarray(decrypted_array)
    
    # Save the decrypted image
    decrypted_img.save(output_image_path)
    print(f"Image decrypted and saved as {output_image_path}")

# Generate a random key for encryption (the key should be the same size as the image)
def generate_random_key(image_width, image_height):
    # Generate a random key of the same size as the image (3 channels for RGB)
    return np.random.randint(0, 256, (image_height, image_width, 3), dtype=np.uint8)

# Test the encryption and decryption functions
if __name__ == "__main__":
    input_image_path = "input_image.jpg"  # Path to the input image
    encrypted_image_path = "encrypted_image.jpg"  # Path to save the encrypted image
    decrypted_image_path = "decrypted_image.jpg"  # Path to save the decrypted image
    
    # Open the input image and get its dimensions
    img = Image.open(input_image_path)
    img_width, img_height = img.size
    
    # Generate a random key for encryption
    key = generate_random_key(img_width, img_height)
    
    # Encrypt the image
    encrypt_image(input_image_path, encrypted_image_path, key)
    
    # Decrypt the image back
    decrypt_image(encrypted_image_path, decrypted_image_path, key)
