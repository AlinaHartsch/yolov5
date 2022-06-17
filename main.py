# open the camera and run the model within the video stream
#logic of the formual below
#!python detect.py --weights runs/train/exp/weights/best.pt --img 416 --conf 0.1 --source {dataset.location}/test/images

from detect import run

run(weights= r'runs\train\exp\weights\final_v.pt', imgsz=(416, 416), conf_thres=0.1, source=0)
