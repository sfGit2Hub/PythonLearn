import cv2
import dlib
#   返回默认的面部检测器对象
detector = dlib.get_frontal_face_detector()
#   图形预测器对象
#   可以描绘出面部重要的部位坐标
#   使用官方的训练集初始化     http://dlib.net/files/ 下载
landmark_predictor = dlib.shape_predictor('E:\Program Files\sf-demo\shape_predictor_68_face_landmarks.dat')
facerec = dlib.face_recognition_model_v1('E:\Program Files\sf-demo\dlib_face_recognition_resnet_model_v1.dat')
img = cv2.imread('./lena.jpg')
faces = detector(img, 1)
if (len(faces) > 0):
    for k,d in enumerate(faces):
        cv2.rectangle(img, (d.left(), d.top()), (d.right(), d.bottom()), (255,255,255))
        shape = landmark_predictor(img, d)
        face_descriptor = facerec.compute_face_descriptor(img, shape)
        print(face_descriptor)
        for i in range(68):
            cv2.circle(img, (shape.part(i).x, shape.part(i).y), 5, (0,255,0), -1, 8)
            cv2.putText(img, str(i), (shape.part(i).x,shape.part(i).y), cv2.FONT_HERSHEY_SIMPLEX, 0.5 , (255,2555,255))
cv2.imshow('Frame',img)
cv2.waitKey(0)