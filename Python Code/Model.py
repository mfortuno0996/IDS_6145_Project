import mesa
from Agent import Exhaust
from PIL import Image

def LoadImage(filename):
    try:
        original_image = Image.open(filename)
    except:
        print("Unable to load image")
    L3 = original_image.convert('RGB') #converts image to RGB
    return L3



class ExhaustModel(mesa.Model):

    def __init__(self, width=100, height=100, exhaust_prob = 0.6):

        self.schedule = mesa.time.RandomActivation(self)
        self.grid = mesa.space.Grid(width, height, torus=False)

        for (contents, x, y) in self.grid.coord_iter():
            Hellenic_Trench_Image1 = LoadImage('Hellenic Trench Ships_Shrunk.png')
            r, g, b = Hellenic_Trench_Image1.getpixel((x,y)) #gets the pixel rgb value
            if b > r: #navy color value
                if self.random.random() < exhaust_prob: #checks to see if random value is less than exhaust_prob value
                    new_exhaust = Exhaust((x,y), self) #creates exhaust agent
                    self.grid.place_agent(new_exhaust, (x,y)) #places exhaust agent on grid
                    self.schedule.add(new_exhaust) #adds exhaust agent to scheduler
        self.running = True


    def step(self):
        self.schedule.step()

