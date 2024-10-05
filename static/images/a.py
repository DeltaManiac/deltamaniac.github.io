import os
import shutil

# Directory containing the segment folders and images
base_directory = '.'  # Update this to your actual path

# Target root directory for hierarchical organization
target_root = os.path.join(base_directory, 'games', 'tis-100', 'segment')

# Create the target root directory if it doesn't exist
os.makedirs(target_root, exist_ok=True)

# Iterate through all directories in the base directory
for foldername in os.listdir(base_directory):
    folder_path = os.path.join(base_directory, foldername)
    
    # Check if it's a directory and matches the segment naming pattern
    if os.path.isdir(folder_path) and foldername.startswith('games.tis-100.segment.'):
        # Extract the segment number
        segment_number = foldername.split('.')[-1]
        
        # Create a directory for the segment number
        segment_directory = os.path.join(target_root, segment_number)
        
        # Create the segment directory if it doesn't exist
        os.makedirs(segment_directory, exist_ok=True)

        # Initialize a counter for renaming files
        file_count = 1

        # Move and rename PNG files associated with this segment to the new segment directory
        for file in os.listdir(base_directory):
            if file.endswith('.png'):
                original_image_path = os.path.join(base_directory, file)
                
                # Create new file name
                new_image_name = f"{file_count}.png"
                new_image_path = os.path.join(segment_directory, new_image_name)
                
                # Move and rename the image
                shutil.move(original_image_path, new_image_path)
                print(f'Moved and renamed image: {file} to {new_image_path}')
                
                # Increment the file counter
                file_count += 1

print("Folder restructuring complete.")