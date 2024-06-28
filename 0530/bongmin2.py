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
    def __init__(self, vertaxs,radius): #꼭지점 , 반지름
        super().__init__("Circle")
        self.radius = radius
        self.vertaxs = vertaxs
    
    def vertax(self): #꼭지점개수
            
        return self.vertaxs
        
    def area(self):  #면적        
        self.area = self.radius * self.radius * 3.14 
        return self.area
    
    def circum(self):   #둘레
        self.circum = self.radius * 2 * 3.14
        return self.circum

class Triangle(shape) :         
    def __init__(self, vertaxs, base, height):
        super().__init__("Triangle")
        self.base = base
        self.height = height
        self.vertaxs = vertaxs
    
    def vertax(self): #꼭지점개수
        return self.vertaxs
        
    def area(self):  #면적        
        self.area = self.base * self.height / 2
        return self.area
    
    def circum(self):   #둘레
        self.circum = self.base * 3
        return self.circum

class Rectangle(shape) :
    def __init__(self, vertaxs, base, height):
        super().__init__("Rectangle")
        self.base = base
        self.height = height
        self.vertaxs = vertaxs
    def vertax(self): #꼭지점개수
        return self.vertaxs
        
    def area(self):  #면적        
        self.area = self.base * self.height 
        return self.area
    
    def circum(self):   #둘레
        self.circum = self.base * 4
        return self.circum

# class Poligon(shape) :
#     def __init__(self, vertaxs, base, height):
#         super().__init__("Poligon")
#         self.base = base
#         self.height = height
#         self.vertaxs = vertaxs
    
#     def vertax(self): #꼭지점개수
#         return self.vertaxs
        
#     def area(self):  #면적        
#         self.area = 
#         return self.area
    
#     def circum(self):   #둘레
#         self.circum = self.base * n
#         return self.circum
        
    

    
    
        
circle = Circle(0,3)        #vertaxs, base, height 꼭짓점, 밑변,높이
triangle = Triangle(3, 3, 3) 
rectangle = Rectangle(4, 3, 3)
#poligon = Poligon(n, 3, 3)

print(f"Circle - Vertax: {circle.vertax()}, Area: {circle.area()}, Circumference: {circle.circum()}")
print(f"Triangle - Vertax: {triangle.vertax()}, Area: {triangle.area()}, Circumference: {triangle.circum()}")
print(f"Rectangle - Vertax: {rectangle.vertax()}, Area: {rectangle.area()}, Circumference: {rectangle.circum()}")
#print(f"Poligon - Vertax: {Poligon.vertax()}, Area: {Poligon.area()}, Circumference: {Poligon.circum()}")


# %%
