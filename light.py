color = input("Enter a color (red, yellow, or green): ").lower()

if color == "red":
    print("Stop!")
elif color == "yellow":
    print("Slow down and prepare to stop.")
elif color == "green":
    print("Go!")
else:
    print("Invalid color. Please enter red, yellow, or green.")