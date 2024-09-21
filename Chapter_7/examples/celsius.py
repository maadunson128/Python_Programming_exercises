###Program : Simple decision structures

temp_cel = eval(input("What's the temperature in degree celsius: "))
temp_far = 9/5 * temp_cel + 32
print(f"Temperature in farenheit: {temp_far} degree Farenheit.")

if temp_far > 90:
    print("Very hot temperature")

if temp_far < 30:
    print("Very low temperature")
