import pygame
from pygame.locals import *

pygame.init()

joystick = pygame.joystick.Joystick(0)

while True:
    for event in pygame.event.get(): # get the events (update the joystick)
        if event.type == QUIT: # allow to click on the X button
            pygame.quit()
            exit()
    #BUTTON CONTROL
    for button in range(joystick.get_numbuttons()):
        if button == 0 and joystick.get_button(button):
            print(f"Button 0 pressed")
        elif button == 1 and joystick.get_button(button):
            print(f"Button 1 pressed")
        elif button == 2 and joystick.get_button(button):
            print(f"Button 2 pressed")
        elif button == 3 and joystick.get_button(button):
            print(f"Button 3 pressed")            
        elif button == 4 and joystick.get_button(button):
            print(f"Button 4 pressed")
        elif button == 5 and joystick.get_button(button):
            print(f"Button 5 pressed")
        elif button == 6 and joystick.get_button(button):
            print(f"Button 6 pressed")
        elif button == 7 and joystick.get_button(button):
            print(f"Button 7 pressed")
        elif button == 8 and joystick.get_button(button):
            print(f"Button 8 pressed")
        elif button == 9 and joystick.get_button(button):
            print(f"Button 9 pressed")                        

    #AXIS CONTROL
    for axis in range(joystick.get_numaxes()):
        if (axis == 1 or axis == 3) and joystick.get_axis(axis) <= -0.8:
            if axis == 1:
                print(f"Axis 1 motion UP value:",joystick.get_axis(axis))
            else:
                print(f"Axis 3 motion UP value:",joystick.get_axis(axis))            

        elif (axis == 1 or axis == 3) and joystick.get_axis(axis) >= 0.8:
            if axis == 1:
                print(f"Axis 1 motion DOWN value:",joystick.get_axis(axis))
            else:
                print(f"Axis 3 motion DOWN value:",joystick.get_axis(axis))

        if  (axis == 0 or axis == 2) and joystick.get_axis(axis) <= -0.8:
            if axis == 0:
                print(f"Axis 0 motion LEFT value:",joystick.get_axis(axis))
            else:
                print(f"Axis 2 motion LEFT value:",joystick.get_axis(axis))

        elif (axis == 0 or axis == 2) and joystick.get_axis(axis) >= 0.8:
            if axis == 0:
                print(f"Axis 0 motion RIGHT value:",joystick.get_axis(axis))
            else:
                print(f"Axis 2 motion RIGHT value:",joystick.get_axis(axis))


        if  (axis == 4 or axis == 5) and joystick.get_axis(axis) >= 0.8:
            if axis == 4:
                print(f"Axis 4 motion PRESSED value:",joystick.get_axis(axis))
            else:
                print(f"Axis 5 motion PRESSED value:",joystick.get_axis(axis))                

            
         

     # LOOP KILLER
    if joystick.get_button(4) and joystick.get_button(5):
        print("end")
        break