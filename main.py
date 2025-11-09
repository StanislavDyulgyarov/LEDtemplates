import csv
import datetime
import cv2
import time
import ctypes


HEAD = "DataExport-"
PLANT = "3500-"
CURRENTDAY = datetime.datetime.now()

FILESTRING = HEAD + PLANT + CURRENTDAY.strftime("%d").rjust(2, '0') + CURRENTDAY.strftime("%m") + CURRENTDAY.strftime("%Y")

y = True
while y == True:
  x = input("Enter a workorder number:")
  if len(x) == 9:
     y=False
  else:
     print("Please give an appropriate WO number.")

print("Thank you!") 

with open(FILESTRING + '.csv', newline='') as csvfile:
    spamreader = csv.DictReader(csvfile)
    for row in spamreader:
        if row['WO'] == x:
           print("Order found: ", row['Z3'])
           imageName = row['Z3']

img = cv2.imread(imageName + ".png", cv2.IMREAD_COLOR)
cv2.namedWindow("window", cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty("window",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
cv2.imshow("window", img)

cv2.waitKey(1) 
time.sleep(0.2)

user32 = ctypes.windll.user32
hwnd = user32.FindWindowW(None, "window")
if hwnd:
    user32.ShowWindow(hwnd, 5)
    user32.SetForegroundWindow(hwnd)

cv2.waitKey(0)
cv2.destroyAllWindows()
