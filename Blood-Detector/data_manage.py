import pandas as pd
from sklearn import model_selection
import numpy as np
import os
import shutil

def create_txts(df, image_original_path, image_train_path, label_path):

    filenames = []
    for filename in df.file_name:
        filenames.append(filename)
    unique_files = set(filenames)
    
    for unique in unique_files:
        yolo_input = []
        for _, row in df[df.file_name == unique].iterrows():
            yolo_input.append([row.label, row.x_center_norm, row.y_center_norm, row.width_norm, row.height_norm])
            yolo_input_to_txt = np.array(yolo_input)
            name_txt = os.path.join(label_path, str(row.file_name.split('.')[0] + ".txt"))

            np.savetxt(name_txt, yolo_input_to_txt, fmt=["%d", "%f", "%f", "%f", "%f"])
            shutil.copyfile(os.path.join(image_original_path, row.file_name), os.path.join(image_train_path, row.file_name))


def preprocessing():

    dframe = pd.read_csv('./../Dataset/annotations_blood_cells.csv')
    df_train, df_valid = model_selection.train_test_split(dframe, test_size=0.1, random_state=13, shuffle=True)
    print('Shape train: {}'.format(df_train.shape))
    print('Shape valid: {}'.format(df_valid.shape))

    image_original_path = './../Dataset/BCCD/JPEGImages'

    image_train_path = './../Dataset/BCCD/ModelData/images/train'
    image_val_path = './../Dataset/BCCD/ModelData/images/val'

    labels_train_path = './../Dataset/BCCD/ModelData/labels/train'
    labels_val_path = './../Dataset/BCCD/ModelData/labels/val'
    

    create_txts(df_train, image_original_path, image_train_path, labels_train_path)
    create_txts(df_valid, image_original_path, image_val_path, labels_val_path)

    


if __name__ == '__main__':
    preprocessing()