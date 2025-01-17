#Program: To find the distance of lightning strike

def distance(seconds):
    feet_distance = 1100 * seconds
    miles_distance = feet_distance / 5280
    print(f"The distance b/w you and lightning strike: {round(miles_distance, 4)} miles")

time = float(input("Enter the time taken to hear the sound of lightning after you saw it (in seconds): "))
distance(time)
