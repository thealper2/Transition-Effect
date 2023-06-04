import cv2

def nothing(x):
    pass

image1 = cv2.imread("image1.jpg")
image2 = cv2.imread("image2.jpg")

size = (640, 480)

image1 = cv2.resize(image1, size)
image2 = cv2.resize(image2, size)

window_name = "Transition Effect"

out = cv2.addWeighted(image1, 0.5, image2, 0.5, 0)
cv2.namedWindow(window_name)

cv2.createTrackbar("Alpha/Beta", window_name, 0, 1000, nothing)

while True:
    cv2.imshow(window_name, out)
    alpha = cv2.getTrackbarPos("Alpha/Beta", window_name) / 1000
    beta = 1 - alpha
    out = cv2.addWeighted(image1, alpha, image2, beta, 0)

    if cv2.waitKey(0) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()
