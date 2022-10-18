# 동영상 파일 재생
import cv2

video_file = "img/big_buck.avi"

cap = cv2.VideoCapture(video_file) # 동영상 캡쳐 객체 생성

if cap.isOpened(): # 캡쳐 객체 초기화 확인
    while True:
        ret, img = cap.read()   # 다음 프레임 읽기
        if ret:                 # 프레임 읽기 정상
            cv2.imshow(video_file, img) # 화면에 표시
            cv2.waitKey(25)     # 25ms 지연
        else:                   # 다음 프레임을 읽을 수 없음
            break               # 재생 완료
else:
    print("can't open video")   # 캡쳐 객체 초기화 실패

cap.release()                   # 캡쳐 자원 반납
cv2.destroyAllWindows()