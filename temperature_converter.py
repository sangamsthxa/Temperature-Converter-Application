import os

# HISTORY_FILE = os.getenv("HISTORY_FILE", "/history.txt")
HISTORY_FILE = "history.txt"

# method to convert into fahrenheit from celsius
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# method to convert into celsius from fahrenheit
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# method to convert into kelvin from celsius
def celsius_to_kelvin(celsius):
    return celsius + 273.15

# method to convert into celsius from kelvin
def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

# method to ask temperature from user
def enterTemperature():
    temp = float(input("Enter temperature: "))
    return temp

# method to save history
def save_to_history(conversion, result):
    # os.makedirs(os.path.dirname(HISTORY_FILE), exist_ok=True)
    with open(HISTORY_FILE, "a") as file:
        file.write(f"{conversion} = {result}\n")

# method to load history in the console
def load_history():
    if not os.path.exists(HISTORY_FILE):
        # returns if history file is not found
        print("No history found.")
        return
    with open(HISTORY_FILE, "r") as file:
        print("Conversion History:")
        print(file.read())

#main method to run the program
def main():
    while True:
        print("\nTemperature Converter")
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        print("3. Celsius to Kelvin")
        print("4. Kelvin to Celsius")
        print("5. View History")
        print("6. Exit")
        
        #ask user to input the choice
        choice = input("Enter choice: ")
        
        if choice == "6":
            print("Exiting converter. Goodbye!")
            break
        
        if choice == "5":
            load_history()
            continue

        # cases to convert into another temperature scale
        if choice == "1":
            temp = enterTemperature()
            result = celsius_to_fahrenheit(temp)
            conversion = f"{temp}°C to {result}°F"
        elif choice == "2":
            temp = enterTemperature()
            result = fahrenheit_to_celsius(temp)
            conversion = f"{temp}°F to {result}°C"
        elif choice == "3":
            temp = enterTemperature()
            result = celsius_to_kelvin(temp)
            conversion = f"{temp}°C to {result}K"
        elif choice == "4":
            temp = enterTemperature()
            result = kelvin_to_celsius(temp)
            conversion = f"{temp}K to {result}°C"
        else:
            print("Invalid choice. Try again.")
            continue
        
        print(f"Result: {conversion}")
        # call save method to save the conversion history
        save_to_history(conversion, result)
        
if __name__ == "__main__":
    main()