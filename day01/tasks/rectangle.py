def rectangle_area_perimeter():
    print("Enter size of rectangle that you want to calculate its area and perimeter\n")
    length = int(input("Length: "))
    width = int(input("Width: "))
    print(f"Rectangle area is {length*width}")
    print(f"Rectangle perimeter is {2*(length+width)}")

rectangle_area_perimeter()