hour = int(input("Enter the current hour (1-12): "))
hours_ahead = int(input("How many hours ahead? "))
new_hour = (hour + hours_ahead) % 12

print(f"New hour: {new_hour} o'clock")
