# Your code here

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        

    def __str__(self):
        return f"{self.title}, {self.author} , {self.year}"

# Create an instance of the Person class
libro1 = Book("terapeuta", "jose emilio", "1925")

# Print the information of the person using the __str__ method
print(libro1)  # Output: Juan, 25 years old, Male