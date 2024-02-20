import os
import cv2

path = 'D:/Coding/Class/Projects/117/Images'

Images = []

for file in os.listdir(path):
    file_name, file_extension = os.path.splitext(file)

    if file_extension.lower() in ['.jpg', '.jpeg', '.png', '.gif']:
        file_name = os.path.join(path, file)

        print(file_name)

        Images.append(file_name)

count = len(Images)

frame = cv2.imread(Images[0])

width, height, channels = frame.shape

size = (width, height)

print(size)

out = cv2.VideoWriter('Project.avi', cv2.VideoWriter_fourcc(*'DIVX'), 0.8, size)

for i in range(0, count-1):
    img = cv2.imread(Images[i])

    cv2.imshow('Friendship Day', img)
    cv2.waitKey(1000)

    out.write(img)

print("Done")

cv2.destroyAllWindows()

out.release()