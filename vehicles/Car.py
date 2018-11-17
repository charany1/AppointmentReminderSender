import fire
class Car:

    def __init__(self, speed=10, colour="R"):
        self.speed = speed
        self.colour = colour

    def change_colour(self,colour):
        self.colour = colour
        return colour

    def change_speed(self,speed):
        self.speed = speed

    def get_current_state(self):
        print("Color : {} , Speed : {}".format(self.colour,self.speed))



def main():
    car_1 = Car()
    car_1.get_current_state()

if __name__=="__main__":
    fire.Fire(Car)