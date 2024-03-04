## Operator Overloading:
## More Use of Dunder Method:
# __add__ = 
# 

class Vector:
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k

    def __str__(self): # Dunder method
        return f'{self.i}i + {self.j}j + {self.k}k'
   
    def __add__(self, x): # By writing this: Now our result type is vector
        return Vector(self.i + x.i , self.j + x.j , self.k + x.k)
    
v1 = Vector(3, 5, 6)
print(v1)
v2 = Vector(1, 2, 9)
print(v2)

print(v1 + v2) # This can be performed by add method in the class, if the method is not present then it will gives an error
print(type(v1 + v2)) 

