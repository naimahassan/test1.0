class Circle:
    
    def __init__(self,radius):
        self.radius=radius


    def get_area(self):
        area=2*3.14*self.radius
        return area

    def circumfrence(self):
        return 2*3.14*self.radius
    


class square:
    def __init__(self,side):
        self.side=side

    def area(self):
        return self.side*self.side

    def perimeter(self):
        return 4*self.side
        



class rectangle:
    def __init__(self,l,w):
        self.l=l
        self.w=w
        
    def perimeter(self):
       return 2 * (self.l + self.w)
   
    def get_area(self):
       return self.l * self.w



class sphere:
    def __init__(self,r):
        self.r=r
        

    def area(self):
        return (4*3.14*self.r)*2

    def volume(self):
        return 4/3*3.14*self.r*2