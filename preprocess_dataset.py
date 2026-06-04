import os, cv2
from tqdm import tqdm
from preprocess import preprocess_final

DATASET_LOCATION = r"C:\Users\Divya Dharshini K\Desktop\Kinect-Vision-master\dataset\Sign-Language-Digits-Datase\train"
if not os.path.exists(DATASET_LOCATION):
    raise FileNotFoundError(f"Dataset path not found: {DATASET_LOCATION}")

CLASSES = sorted([
    d for d in os.listdir(DATASET_LOCATION)
    if os.path.isdir(os.path.join(DATASET_LOCATION, d))
])

PREPROCESSED_DATASET_LOCATION = r'./Sign-Language-Digits-Dataset/Preprocessed-Dataset/'

def preprocess_dataset():
    try:
        os.makedirs(PREPROCESSED_DATASET_LOCATION, exist_ok=True)
        for _class in CLASSES:
            os.makedirs(os.path.join(PREPROCESSED_DATASET_LOCATION, _class), exist_ok=True)
    except Exception as e:
        print("Directory creation error:", e)
    
    for _class in CLASSES:
        data_loc = os.path.join(DATASET_LOCATION, _class)
        image_files = os.listdir(data_loc)
        c = 1

        for _file in tqdm(image_files, desc=f"Processing {_class}"):
            img_path = os.path.join(data_loc, _file)
            img = cv2.imread(img_path)

            if img is None:
                continue  # skip unreadable files

            image = preprocess_final(img)

            out_path = os.path.join(
                PREPROCESSED_DATASET_LOCATION,
                _class,
                f"{c}.jpg"
            )
            cv2.imwrite(out_path, image)
            c += 1

preprocess_dataset()
