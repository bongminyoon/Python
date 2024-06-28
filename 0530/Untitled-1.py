#%%
class shape: 
    def __init__(self, name):
        self.name = name
    def vertax(self):
        pass
    
    def area(self):
        pass
    
    def circum(self):
        pass

class Circle(shape) :
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius
        
    def vertax(self): #꼭지점개수
        return self
        
    def area(self):  #면적        
        return self.radius * self.radius * 3.14
    def circum(self):   #둘레
        return self.radius * 2 * 3.14

class Triangle(shape) :         
    def __init__(self, radius, height):
        super().__init__("Triangle")
        self.radius = radius
    def vertax(self): #꼭지점개수
        self.vertax = self
        
    def area(self, radius):  #면적        
        self.area = radius * self * 3.14
    def circum(self):   #둘레
        self.circum = self * 2 * 3.14   

class Rectangle(shape) :
    ef __init__(self, radius, height):
        super().__init__("Rectangle")
        self.radius = radius
        self.height = heighr
    def vertax(self): #꼭지점개수
        self.vertax = self
        
    def area(self, radius):  #면적        
        return self.radius * self.height
    def circum(self):   #둘레
        self.circum = self * 2 * 3.14   

class Polygon(shape) :
    ef __init__(self, radius):
        super().__init__("Polygon")
        self.radius = radius
    def vertax(self): #꼭지점개수
        self.vertax = self
        
    def area(self, radius):  #면적        
        self.area = radius * self * 3.14
    def circum(self):   #둘레
        self.circum = self * 2 * 3.14   
    
#main


#circle = Circle(0,3) #꼭지점, 지름
triangle = Circle(3,3) #꼭지점, 지름
rectangle = Rectangle(4,3) #꼭지점, 지름
polygon = Polygon(5,3) #꼭지점, 지름

triangle