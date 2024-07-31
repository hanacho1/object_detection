import json
import os
from PIL import Image

# Update image size 
def update_image_dimensions(json_path, image_dir):
    with open(json_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    for image in data['images']:
        if image['width'] == 0 or image['height'] == 0:
            image_path = os.path.join(image_dir, image['file_name'])
            if os.path.exists(image_path):
                try:
                    with Image.open(image_path) as img:
                        width, height = img.size
                    image['width'] = width
                    image['height'] = height
                    print(f"Updated dimensions for {image['file_name']}: width={width}, height={height}")
                except Exception as e:
                    print(f"Error processing {image['file_name']}: {e}")

    with open(json_path, 'w', encoding='utf-8') as file:
        json.dump(data, file)

# YOLO format conversion function
def convert_to_yolo(json_path, output_dir):
    with open(json_path, 'r', encoding='utf-8') as file:
        data = json.load(file)


    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for image in data['images']:
        image_id = image['id']
        image_width = image['width']
        image_height = image['height']
        image_filename = image['file_name']

        if image_width == 0 or image_height == 0:
            print(f"Skipping {image_filename} due to invalid dimensions.")
            continue

        label_file = os.path.join(output_dir, os.path.splitext(image_filename)[0] + '.txt')
        with open(label_file, 'w') as lf:
            for annotation in data['annotations']:
                if annotation['image_id'] == image_id:
                    class_id = annotation['category_id']
                    bbox = annotation['bbox']

                    x_center = (bbox[0] + bbox[2] / 2) / image_width
                    y_center = (bbox[1] + bbox[3] / 2) / image_height
                    width = bbox[2] / image_width
                    height = bbox[3] / image_height

                    lf.write(f"{class_id} {x_center} {y_center} {width} {height}\n")


def main():
    parser = argparse.ArgumentParser(description="Convert JSON files to YOLO format and update image dimensions.")
    parser.add_argument('--json-folder', type=str, required=True, help='Path to the folder containing JSON files')
    parser.add_argument('--txt-folder', type=str, required=True, help='Path to the folder to save TXT files')
    parser.add_argument('--image-folder', type=str, required=True, help='Path to the folder containing images')

    args = parser.parse_args()

    input_dir = args.json_folder
    output_dir = args.txt_folder
    image_dir = args.image_folder

    for json_filename in os.listdir(input_dir):
        if json_filename.endswith('.json'):
            json_path = os.path.join(input_dir, json_filename)
            update_image_dimensions(json_path, image_dir)
            convert_to_yolo(json_path, output_dir)

if __name__ == "__main__":
    main()
            

 
