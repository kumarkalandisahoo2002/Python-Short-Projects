#finding area of "Square"
arm = int(input("Enter the length of the side:\n"))
print(f"Area of the square having side length {arm} is: ", arm**2)
print("\n")


#finding area of "Rectangle"
length = int(input("Enter the length of rectangle:\n"))
breadth = int(input("Enter the breadth of rectangle:\n"))
print(f"Area of the rectangle having length {length} & breadth {breadth} is: ", length * breadth)
print("\n")


#finding area of "Circle"
PI = 3.1415926535897
radius = int(input("Enter the radius of circle:\n"))
print(f"Area of the circle having radius {radius} is", PI*(radius**2))
print("\n")


#finding area of "Triangle"
base = int(input("Enter the base of triangle:\n"))
height = int(input("Enter the height of triangle:\n"))
print(f"Area of the triangle having base {base} & height {height} is: ", 0.5*base*height)