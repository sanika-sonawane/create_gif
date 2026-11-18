print("  Area Calculator ")
print("--------------------")
print("1] Triangle")
print("2] Rectangle")
print("3] Square")
print("4] Circle")
print("5] Quit")

ques = int(input("Which Shape: "))
if ques == 1:
    base = int(input("Enter the base Triangle: "))
    height = int(input("Enter the height of Triangle: "))
    area = (base * height) / 2
    print("The area of Triangle is: ", area)
elif ques == 2:
    length1 = int(input("Enter the lenth of rectangle: "))
    breadth1 = int(input("Enter the breadth of the rectangle: "))
    area1 = length1 * breadth1
    print("The area of the Rectangle is: ", area1)
elif ques == 3:
    side = int(input("Enter the side length of square: "))
    area2 = side ** 2
    print("The area of Square is: ", area2)
elif ques == 4:
    radius = int(input("Enter the radius of circle"))
    area3 = 3.14 * (radius ** 2)
    print("The area of circle is: ", area3)
else:
    print("Quit")
