# Your code here

class MathOperations():
    pi=3.1416
    @classmethod
    def calculate_circle_area(cls, radius):
        return cls.pi * radius * radius
    
area = MathOperations.calculate_circle_area(5)
print(area)  # Output: 78.54