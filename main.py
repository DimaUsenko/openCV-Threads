'''Распознавание объектов (оранжевых котов) + парралельная обработка(по потоку на каждое изображение)'''

import threading
import cv2

def cat(image,t):
    cat_image = cv2.imread(image)
    cat_hsv = cv2.cvtColor(cat_image, cv2.COLOR_BGR2HSV)
    cat_color_low = (7, 40, 60)
    cat_color_high = (18, 255, 200)
    only_cat_hsv = cv2.inRange(cat_hsv, cat_color_low, cat_color_high)

    moments = cv2.moments(only_cat_hsv, 1)  # получим моменты
    x_moment = moments['m01']
    y_moment = moments['m10']
    area = moments['m00']
    x = int(x_moment / area)
    y = int(y_moment / area)
    cv2.putText(cat_image, "Orange Cat!", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    #cv2.imshow('cat_found', cat_image)
    #cv2.waitKey(0)
    cv2.imwrite(f'result{t}.jpg', cat_image)

thread1 = threading.Thread(target=cat, args=(f'im0.jpg',0))
thread2 = threading.Thread(target=cat, args=(f'im1.jpg',1))
thread3 = threading.Thread(target=cat, args=(f'im2.jpg',2))

thread1.start()
thread2.start()
thread3.start()

thread1.join()
thread2.join()
thread3.join()