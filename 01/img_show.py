# 기본 입출력
import cv2

img_file = "img/girl.jpg"
img = cv2.imread(img_file) # image 읽기

if img is not None:
    cv2.imshow('IMG', img) # 읽은 이미지 화면에 표시
    cv2.waitKey() # 키가 입력될 때 까지 대기
    cv2.destroyAllWindows() # 창 모두 닫기
else:
    print("No image file.")