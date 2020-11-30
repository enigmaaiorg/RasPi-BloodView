#exec(open("test.py --name prueba").read())
import os

def trainModel():

    os.system('python ./../YOLOv5/train.py --img 640 --batch 16 --epochs 100 --hyp ./../YOLOv5/data/hyp.scratch.yaml --data ./../Dataset/bloodData.yaml --cfg ./../YOLOv5/models/yolov5s.yaml --weights ./../YOLOv5/models/yolov5s.pt --cache-images --name FINAL')

if __name__ == '__main__':
    trainModel()

# 100 epochs completed in 0.876 hours.