import os

def detection(file_name):

    # correction in the line 53 in export.py from original repo

    return os.system('python ./../../YOLOv5/detect.py --source ./static/inference/input/{} --output \
                   ./static/inference/output/ --weights \
                   ./../runs/FINAL/weights/best.pt --device  cpu'.format(file_name))

if __name__ == '__main__':
    detection()
    




