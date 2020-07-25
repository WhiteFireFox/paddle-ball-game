#将视频逐帧保存为图片
import math
import cv2

def GetPicture(path):
    video = cv2.VideoCapture(path)
    # 获取视频帧率
    fps = video.get(cv2.CAP_PROP_FPS)
    print(fps)
    # 获取画面大小
    width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    size = (width, height)
    # 获取帧数   
    frame_num = str(video.get(7))
    ret, frame = video.read()
    i = 0
    while ret:
        cv2.imwrite('/home/aistudio/picture/' + str(i) + '.jpg', frame)   #保存图片到/home/aistudio/pic/目录下
        ret, frame = video.read()
        i += 1
    video.release()

#调用GetPicture
GetPicture('/home/aistudio/work/test.mp4')
