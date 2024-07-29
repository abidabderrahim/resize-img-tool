from PIL import Image
import os

# Get user input for the directory path, new dimensions, and extension
directory = input("Enter the full path of the directory containing the images: ").strip()

# Check if the path is a valid directory
if not os.path.isdir(directory):
    print(f"The path provided is not a valid directory: {directory}")
else:
    try:
        # Get new dimensions from the user
        x = int(input("Enter new width (X): "))
        y = int(input("Enter new height (Y): "))

        # Get the desired extension from the user
        extension = input("Enter the desired extension (e.g., png, jpg): ").strip().lower()

        # Check for valid extensions
        valid_extensions = {'png', 'jpg', 'jpeg', 'bmp', 'gif', 'tiff'}
        if extension not in valid_extensions:
            print(f"Invalid extension: {extension}. Please choose from {valid_extensions}")
        else:
            # Create the new directory for resized images
            new_directory = os.path.join(directory, 'new-img')
            os.makedirs(new_directory, exist_ok=True)

            # Iterate over all files in the directory
            for filename in os.listdir(directory):
                file_path = os.path.join(directory, filename)

                # Check if the file is an image
                if os.path.isfile(file_path) and filename.lower().endswith(tuple(valid_extensions)):
                    try:
                        # Open the image file
                        image = Image.open(file_path)
                        print(f"Resizing image: {filename}, Current size: {image.size}")

                        # Resize the image
                        resize_image = image.resize((x, y))

                        # Save the resized image in the new directory with the new extension
                        base_filename, _ = os.path.splitext(filename)
                        new_file_name = os.path.join(new_directory, f'{base_filename}_resized.{extension}')
                        resize_image.save(new_file_name)

                        print(f"Resized image saved as {new_file_name} with dimensions ({x}, {y})")
                    except Exception as e:
                        print(f"An error occurred while processing {filename}: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
