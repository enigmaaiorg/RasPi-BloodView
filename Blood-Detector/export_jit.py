# pip install coremltools==4.0b2
# pip install -r requirements.txt 
# pip install onnx>=1.7.0

import os

def export_JIT():

    # correction in the line 53 in export.py from original repo
    os.system('python ./../YOLOv5/models/export.py --weights ./runs/FINAL/weights/best.pt --img 640 --batch 1')


if __name__ == '__main__':
    export_JIT()