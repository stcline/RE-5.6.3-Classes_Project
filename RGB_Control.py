#Starter code for this assignment.  The comments may be used to guide you but the code is incomplete.

def boardSetup():
  #disable warnings (optional)
  GPIO.setwarnings(False)
  #Select GPIO Mode
  GPIO.setmode(GPIO.BCM)

#Create a class to control the RGB LED
class RGB:
  def __init__(self, red_pin, green_pin, blue_pin):
    #create attributes for the red,green and blue pins
    
    #set all GPIO pins as outputs
    
    #set each pin as a PWM output at 75 Hz
    
    
    #create a method to control the RGB LED by passing arguments for red, green and blue duty cycles as well as duration
    

#Create an RGB object


#Ask the user for the three color values and duration


#Use your custom method from the RGB class to control the object
