import os

def detection(path_file):

    # correction in the line 53 in export.py from original repo
    #path_file = './inference/input/test.py'

    #os.system('python ./../yolov5/detect.py --source ./inference/input/{} --weights ./runs/FINAL/weights/jit_512_640.pt --device cpu'.format(path_file))
    print("ha llegado a blood_detection")

if __name__ == '__main__':
    detection()
    




