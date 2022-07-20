import pygame
import time
import random
import numpy as np
import easyocr

#storing the coordinates of cars getting parked
x_score = np.zeros(10)
y_score = np.zeros(10)

#selects empty parking slot
def select(slots):
    for i in range(10):
        if slots[i] == 0:
            return i
    return 10

#display the cars alredy parked
def move_bilt(carlist,slots):
    for j in range(10):
            if x_score[j] != 0:
                display_surface.blit(carlist[j].image, (x_score[j], y_score[j]))
    free = slots.shape[0] - np.count_nonzero(slots, axis=0)
    Occupied = 10 - free
    textsurface = myfont.render('Free Space : '+str(free), False, (0, 0, 0))
    textsurface1 = myfont.render('Occupied Space : '+str(Occupied), False, (0, 0, 0))
    display_surface.blit(textsurface,(685,20))
    display_surface.blit(textsurface1,(685,50))
    
    pygame.display.update()

#display the car taken away with charges
def take_bilt(carlist,slots,takecar,tot):
    for j in range(10):
        if (x_score[j] != 0) and (j != takecar):
            display_surface.blit(carlist[j].image, (x_score[j], y_score[j]))
    free = slots.shape[0] - np.count_nonzero(slots, axis=0)
    Occupied = 10 - free
    textsurface = myfont.render('Free Space : '+str(free), False, (0, 0, 0))
    textsurface1 = myfont.render('Occupied Space : '+str(Occupied), False, (0, 0, 0))
    textsurface2 = myfont.render('Charges : '+str(tot), False, (0, 0, 0))
    display_surface.blit(textsurface,(685,20))
    display_surface.blit(textsurface1,(685,50))
    display_surface.blit(textsurface2,(685,80))
    pygame.display.update()

#Main Class Car
class Cars():
    def __init__(self):
        r = str(random.randint(1, 3))
        carst = "C:\\Users\\mihir\\Desktop\\Python Innovative\\Cars\\" + "NCAR" + str(r) + ".png"
        self.image = pygame.image.load(carst)

    #animation of car being parked
    def move(self, count, slots, s, numplate,carlist):

        if select(slots) == 10:
            print("Parking Full!!!")
        else:
            count = select(slots)
            timestrt[count] = time.time()
            numplate[count] = s
            slots[count] = 1

        x = 0
        if count % 2 == 0:
            temp = count
        else:
            temp = count - 1
        while True:
            if x < 80 + temp * 57:
                display_surface.fill(white)
                display_surface.blit(image, (0, 0))
                display_surface.blit(self.image, (x, 190))
                x += 0.2   
            else:
                break
            move_bilt(carlist,slots)
            pygame.display.update()

        if count % 2 == 0:
            self.image = pygame.transform.rotate(self.image, 90)
            y = 190
            while True:
                if y > 50:
                    display_surface.fill(white)
                    display_surface.blit(image, (0, 0))
                    display_surface.blit(self.image, (x, y))
                    y -= 0.2   
                else:
                    x_score[count] = x
                    y_score[count] = y
                    break
                move_bilt(carlist,slots)
                pygame.display.update()

        else:
            self.image = pygame.transform.rotate(self.image, -90)
            y = 190
            while True:
                if y < 310:
                    display_surface.fill(white)
                    display_surface.blit(image, (0, 0))
                    display_surface.blit(self.image, (x, y))
                    y += 0.2
                else:
                    x_score[count] = x
                    y_score[count] = y
                    break
                move_bilt(carlist,slots)
                pygame.display.update()

    #animation of car going out of parking
    def takeback(self, count, slots, s, numplate, x, y,carlist):
        takecar = numplate.index(s)
        timeend[takecar] = time.time()
        tot = timeend[takecar] - timestrt[takecar]
        tot = "%.2f" % tot
        print("Time in Park :", tot)
        numplate[takecar] = ""
        slots[takecar] = 0
        if count % 2 == 0:
            while True:
                if y < 190:
                    display_surface.fill(white)
                    display_surface.blit(image, (0, 0))
                    display_surface.blit(self.image, (x, y))
                    y += 0.2
                    
                else:
                    self.image = pygame.transform.rotate(self.image, -90)
                    break
                take_bilt(carlist,slots,takecar,tot)
                


        else:
            while True:
                if y > 190:
                    display_surface.fill(white)
                    display_surface.blit(image, (0, 0))
                    display_surface.blit(self.image, (x, y))
                    y -= 0.2
                    
                else:
                    self.image = pygame.transform.rotate(self.image, 90)
                    break
                take_bilt(carlist,slots,takecar,tot)

        while True:
            if x < 560:
                display_surface.fill(white)
                display_surface.blit(image, (0, 0))
                display_surface.blit(self.image, (x, 190))
                x += 0.2
            else:
                x_score[takecar] = 0
                y_score[takecar] = 0
                break
            take_bilt(carlist,slots,takecar,tot)


pygame.init()
pygame.font.init()
slots = np.zeros(10)
numplate = ["", "", "", "", "", "", "", "", "", ""]
timestrt = ["", "", "", "", "", "", "", "", "", ""]
timeend = ["", "", "", "", "", "", "", "", "", ""]
myfont = pygame.font.Font(r'C:\Users\mihir\Desktop\Python Innovative\Ranille.ttf',16)
white = (255, 255, 255)


free = slots.shape[0] - np.count_nonzero(slots, axis=0)
Occupied = 10 - free
textsurface = myfont.render('Free Space : '+str(free), False, (0, 0, 0))
textsurface1 = myfont.render('Occupied Space : '+str(Occupied), False, (0, 0, 0))


X = 860
Y = 440

display_surface = pygame.display.set_mode((X, Y))

pygame.display.set_caption('Parking')

image = pygame.image.load(r'C:\Users\mihir\Desktop\Python Innovative\parking1.jpg')

i = 0
d = 0
k = 1
h = 1
carlist = [Cars() for i in range(10)]



#infinite loop
#This loop will always run and display the backgroud
while True:
    display_surface.fill(white)
    display_surface.blit(image, (0, 0))
    pygame.draw.rect(display_surface, (110,141,61), (680, 300, 70, 35), border_radius = 15)
    pygame.draw.rect(display_surface, (110,141,61), (770, 300, 70, 35), border_radius = 15)
    free = slots.shape[0] - np.count_nonzero(slots, axis=0)
    Occupied = 10 - free
    textsurface = myfont.render('Free Space : '+str(free), False, (0, 0, 0))
    textsurface1 = myfont.render('Occupied Space : '+str(Occupied), False, (0, 0, 0))
    textsurface3 =  myfont.render('  Park             Take', False, (255,255,255))
    display_surface.blit(textsurface,(685,20))
    display_surface.blit(textsurface1,(685,50))
    display_surface.blit(textsurface3,(687,310))
    
    #Clicking logic of buttons
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 680 <= mouse[0] <= 750 and 300 <= mouse[1] <= 335:
                path = "C:\\Users\\mihir\\Desktop\\Python Innovative\\Numberplates\\no" + str(k) + ".jpg"
                reader = easyocr.Reader(['en'], gpu = False)
                s = reader.readtext(path,detail = 0,paragraph = True)
                print(s)
                i = select(slots)
                if i == 10:
                    print("Parking Full")
                    break
                carlist[i].move(i, slots, s, numplate,carlist)
                k = (k + 1)%10
            if 770 <= mouse[0] <= 840 and 300 <= mouse[1] <= 335:
                path1 =  "C:\\Users\\mihir\\Desktop\\Python Innovative\\Numberplates\\no" + str(h) + ".jpg"
                reader = easyocr.Reader(['en'], gpu = False)
                s = reader.readtext(path1,detail = 0,paragraph = True)
                print(s)
                h += 1
                if s not in numplate:
                    print("Parking Empty")
                    break
                i = numplate.index(s)
               
                carlist[i].takeback(i, slots, s, numplate, x_score[i], y_score[i],carlist)
                

        if event.type == pygame.QUIT:
          
            pygame.quit()
         
            quit()
    mouse = pygame.mouse.get_pos()
    
    #displaying the cars already parked
    for i in range(10):
        if x_score[i] != 0:
            display_surface.blit(carlist[i].image, (x_score[i], y_score[i]))

    pygame.display.update()