import cv2
import numpy as np
import time

# Camera start
cap = cv2.VideoCapture(0)

# Camera warm-up
time.sleep(2)

# Capture background frame
background = None
for i in range(30):
    ret, background = cap.read()

background = np.flip(background, axis=1)

print("Background captured successfully")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Flip frame (mirror effect)
    frame = np.flip(frame, axis=1)

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define RED color range (cloak)
    lower_red1 = np.array([0, 120, 70])
    upper_red1 = np.array([10, 255, 255])

    lower_red2 = np.array([170, 120, 70])
    upper_red2 = np.array([180, 255, 255])

    # Create masks
    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    
    mask = mask1 + mask2

    # Remove noise
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((5, 5), np.uint8))
    mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE, np.ones((5, 5), np.uint8))

    # Inverse mask
    mask_inv = cv2.bitwise_not(mask)

    # Extract background where cloak is
    cloak_area = cv2.bitwise_and(background, background, mask=mask)

    # Extract normal frame
    normal_area = cv2.bitwise_and(frame, frame, mask=mask_inv)

    # Combine both
    final_output = cv2.addWeighted(cloak_area, 1, normal_area, 1, 0)

    # Show output
    cv2.imshow("Invisible Cloak", final_output)

    # Press ESC to exit
    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()