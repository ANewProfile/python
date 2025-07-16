gravity = 9.8
density = float(
    input("What is the density of the displaced liquid(kg/cubic meters)? "))
volume = float(
    input("What is the volume of the displaced liquid(cubic meters)? "))

print(f"The buoyant force is {round(density * volume * gravity, 2)}!")
