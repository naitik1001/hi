class Car(object):
    #init acts like a constructor
    #slef means this keyword
    def __init__(self,model,color,company):
        self.model=model
        self.color=color
        self.company=company
    def start(self):
        print("car started")
    def stop(self):
        print("car stopped")
    def accelerate(self):
        print("car accelerated")
#this audi is not a variable its a object based on the class
audi=Car("Q7","Black","Audi")
print(audi.start())
print(audi.accelerate())
print(audi.stop())
