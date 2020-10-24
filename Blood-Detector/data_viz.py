""" Ploter images with bounding boxes """
# python data_viz.py --file_image BloodImage_00073.jpg

import cv2
import matplotlib.pyplot as plt 
import sys
import pandas as pd
import argparse

def visualization(image_name):

    dframe = pd.read_csv('./../Dataset/annotations_blood_cells.csv')
    image = cv2.imread('./../Dataset/BCCD/JPEGImages/{}'.format(image_name))
    image = cv2.cvtColor(image ,cv2.COLOR_BGR2RGB)

    for _, row in dframe[dframe.file_name == '{}'.format(image_name)].iterrows():
        
        xmin = row.xmin
        xmax = row.xmax
        ymin = row.ymin
        ymax = row.ymax

        width = xmax - xmin
        height = ymax - ymin

        if row.label == 0: # glob. rojos
            cv2.rectangle(image, (xmin, ymin),(xmin + width, ymin + height), (216, 65, 38), 2) 

        if row.label == 1: # glob. blanco
            cv2.rectangle(image, (xmin, ymin),(xmin + width, ymin + height), (219, 223, 198), 2) 

        if row.label == 2: # plaquetas
            cv2.rectangle(image, (xmin, ymin),(xmin + width, ymin + height), (203, 203, 53), 2) 
        
        cv2.putText(image, row.name_cell, (xmin, ymin + height + 20), cv2.FONT_HERSHEY_SIMPLEX , 0.5, (0, 0, 0), 1, cv2.LINE_AA)   

    return image

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Plot image select")
    parser.add_argument('--file_image', type=str, default='BloodImage_00031.jpg', required=False,
                        help='image to plot with bounding boxes')

    args = parser.parse_args()

    frame_image = visualization(args.file_image)   
    plt.imshow(frame_image)
    plt.show()
