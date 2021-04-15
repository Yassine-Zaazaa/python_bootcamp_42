import sys

class Vector:
    def __init__(self, values):
        if type(values) == list:
            if len(values) > 0:
                for i in values:
                    if type(i) != float and type(i) != int:
                        raise TypeError
                    i = float(i)
                self.values = values
            self.size = len(values)
        elif type(values) == int and values > 0:
            self.size = values
            self.values = [float(i) for i in range(values)]
        elif type(values) == tuple:
            if len(values) != 2:
               raise ValueError
            elif values[0] != min(values) or values[1] != max(values):
                raise ValueError
            self.size = values[1] - values[0]
            self.values = [float(i) for i in range(values[0], values[1])]
        else:
            raise TypeError
        
    def __add__(self, second):
        if isinstance(second , Vector):
            if second.size == self.size:
                result = Vector(second.size)
                for i in range(self.size):
                    result.values[i] = self.values[i] + second.values[i]
            else:
                sys.exit("Addition of vectors of different size isn't possible.")
        
        if isinstance(second, int) or isinstance(second, float):
            result = Vector(self.size)
            for i in range(self.size):
                result.values[i] = self.values[i] + second
        return result
    
    def __radd__(self, second):
        return Vector.__add__(self, second)
    
    def __sub__(self, second):
        if isinstance(second , Vector):
            if second.size == self.size:
                result = Vector(second.size)
                for i in range(self.size):
                    result.values[i] = self.values[i] - second.values[i]
            else:
                sys.exit("Substraction of vectors of different size isn't possible.")
        if isinstance(second, int) or isinstance(second, float):
            result = Vector(self.size)
            for i in range(self.size):
                result.values[i] = self.values[i] - second
        return result
    
    def __rsub__(self, second):
        if isinstance(second , Vector):
            return Vector.__sub__(self, second)
        if isinstance(second, int) or isinstance(second, float):
            sys.exit("Subtracting a vector from an integer isn't possible.")
        sys.exit("Substraction from something oter than a Vector or an integer with a vector isn't possible.")
        
    def __truediv__(self, second):
        if isinstance(second, int) or isinstance(second, float):
            result = Vector(self.size)
            for i in range(self.size):
                result.values[i] = self.values[i] / second
            return result
        elif isinstance(second, Vector):
            result = Vector(self.size)
            for i in range(self.size):
                result.values[i] = self.values[i] / second.values[i]
        else:
            sys.exit("Division of something instead a Vector or an integer with a vector isn't possible.")
    
    def __rtruediv__(self, second):
        if isinstance(second, Vector):
            return Vector.__truediv__(self, second)
        if isinstance(second, int) or isinstance(second, float):
            sys.exit("Division of a vector from an integer isn't possible.")
        sys.exit("Division from something instead a Vector or an integer with a vector isn't possible.")
    
    def __mul__(self, second):
        if isinstance(second, int) or isinstance(second, float):
            result = Vector(self.size)
            for i in range(self.size):
                result.values[i] = self.values[i] * second
            return result
        elif isinstance(second, Vector):
            if len(self.values) == len(second.values):
                result = 0
                for i in range(self.size):
                    result = result + (self.values[i] * second.values[i])
            return result
        else:
            sys.exit("Multiplication between a vector on something other than an integer or a vector isn't possible.")
            
    def __rmul__(self, second):
        return Vector.__mul__(self, second)
    
    def __str__(self):
        print("|", end="")
        for i in range(self.size - 1):
            print(f" {self.values[i]}", end=", ")
        print(f"{self.values[self.size - 1]} |")
        return ""
        
    def __repr__(self):
        print("|", end="")
        for i in range(self.size - 1):
            print(f" {self.values[i]}", end=", ")
        print(f"{self.values[self.size - 1]} |")
        return ""