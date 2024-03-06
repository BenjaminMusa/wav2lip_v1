import os
import cv2
from tqdm import tqdm

paths = os.listdir("data/gt")

for img_path in tqdm(paths):
    img = cv2.imread("data/gt/" + img_path)
    img = cv2.resize(img, (384, 384))
    cv2.imwrite("data/hq/" + img_path, img)