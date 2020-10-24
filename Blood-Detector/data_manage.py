import pandas as pd
from sklearn import model_selection
import numpy as np
import os

def create_txts(df, path):

    filenames = []
    for filename in df.file_name:
        filenames.append(filename)
    unique_files = set(filenames)
    
    for unique in unique_files:
        yolo_input = []
        for _, row in df[df.file_name == unique].iterrows():
            yolo_input.append([row.label, row.x_center_norm, row.y_center_norm, row.width_norm, row.height_norm])
            yolo_input_to_txt = np.array(yolo_input)
            
            name_txt = os.path.join(path, str(row.file_name.split('.')[0] + ".txt"))

            np.savetxt(name_txt, yolo_input_to_txt, fmt=["%d", "%f", "%f", "%f", "%f"])


def preprocessing():

    dframe = pd.read_csv('./../Dataset/annotations_blood_cells.csv')
    df_train, df_valid = model_selection.train_test_split(dframe, test_size=0.1, random_state=13, shuffle=True)
    print('Shape train: {}'.format(df_train.shape))
    print('Shape valid: {}'.format(df_valid.shape))

    path_train = './../Dataset/BCCD/test/train'
    path_valid = './../Dataset/BCCD/test/valid'

    create_txts(df_train, path_train)
    create_txts(df_valid, path_valid)

    


if __name__ == '__main__':
    preprocessing()