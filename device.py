class device:
    def __init__(self,name,height,width, power_on):
        self.name = name
        self.height = height
        self.width = width
        power_on = input("would you like to turn the computer on? yes/ no")
        if power_on.lower() =="yes":
            print ("turning", self.name, "on...")
            self.power_on = True
        else:
            print ("turning", self.name,"off...")
            self.power_on = False
        


class computer(device):
    def __init__(self):
        power_on = input("would you like to turn the computer on? yes/ no")
        if power_on.lower() =="yes":
            print ("turning computer on...")
            self.power_on = True
        else:
            print ("turning computer off...")
            self.power_on = False
        
        def netflix(self):
            print ("watching netflix...")
        
        def google_word(self):
            print ("using google word")



        