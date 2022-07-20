Title : Parking Management using Image Processing 

PythonPackages used in this project:
1)easyocr
2)pygame
3)numpy
4)random
5)time

Here, time and random are inbuilt packages of Python Language whereas installation of other three packages are shown below:

1)easyocr
This package can be install using pip install easyocr
Note : There might be issue using this package in PyCharm as well as Jupyter Notebook (As we have tried using both of them).
So we recommend to use Visual Studio Code as we have executed the same in it.

2)pygame
This package can be install using pip install pygame

3)numpy
This package can be install using pip install numpy



After Installition of all the required packages there is one more thing you need to do before execution i.e., you have to change the path of all the images we have used in our GUI. The line numbers where you have to change the path of image are 51,169,186,216,227.

After changing the paths as per your device you are all set to execute the code.

NOTE : After pressing the Park/Take Button in GUI you need to wait for some seconds for cars to come in/go out because pygame and easyocr are very slow libraries and it takes time to execute




FEATURES OF THE PROGRAM

This project is based on real life Parking Management System. The ideology behind this project is when driver reaches the parking, the numberplate of the car gets captured in the camera and stored in the system. Using easyocr, the image (.jpg) file gets extracted to text and stored in the list. Then the animation of the car getting parked will be shown. Maximum 10 cars can be parked after that the error message of the parking full will be shown in the terminal.

The GUI consists of two buttons namely Park and Take for parking and taking away of the car. There are 3 cars (different colors) used in the GUI, the color of the car will be selected randomly by the computer. The allocation space for parking will be selected according to the first empty space found.

For reducing the complexity of the program we already have 10 images of the number plates starting from no0 to no9. When you press Park automatically image no0 will be extracted to text and car is parked and it will run sequentially no1, no2, ...

In real life scenario when the car moves out of the parking space its numberplate will be scanned and car moves out in GUI also but in this project for ease whem you press Take button the first car came will be takenaway. Also when animation of car going out is shown, you can see the Charges of the car on the right panel which is nothing but the time for which the car was being parked.
  

TEAM DETAILS:
19BCE006 - HET AGHERA
19BCE023 - MIHIR BHANDERI
19BCE026 - KUSH BHATT

 

