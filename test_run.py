import cv2, requests
url = "https://localhost:8000/face_detection/detect/"
image_to_read = cv2.imread("C://Users/VRS/Downloads/pho/workpic.jpg")
tracker = {"url":"https://i.ibb.co/Ydpjhy1/workpic.jpg"}
req = requests.post(url, data=tracker).json()
print("image3.png : {}".format(req))


for (w,x,y,z) in req["faces"]:
    cv2.rectangle(image_to_read, (w,x), (y,z), (0,255,0), 2)

cv2.imshow("image1.jpg",image_to_read)
cv2.waitKey(0)
