class Shape: 
    def __init__(self, name):
        self.name = name

    def vertax(self):
        pass
    
    def area(self):
        pass
    
    def circum(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
   
        
    def vertax(self,radius):  # 꼭지점 개수
        return 0
    
    def area(self,radius):  # 면적        
        return radius * radius * 3.14
    
    def circum(self,radius):  # 둘레
        return radius * 2 * 3.14

# main
circle = Circle(0,3)

print(f"Circle - Vertax: {circle.vertax()}, Area: {circle.area()}, Circumference: {circle.circum()}")

