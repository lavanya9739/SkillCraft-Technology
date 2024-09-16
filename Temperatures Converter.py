def fahrenheit_to_celsius(f):
    return (f - 32) * 5.0 / 9.0

def celsius_to_fahrenheit(c):
    return (c * 9.0 / 5.0) + 32

def celsius_to_kelvin(c):
    return c + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def fahrenheit_to_kelvin(f):
    c = fahrenheit_to_celsius(f)
    return celsius_to_kelvin(c)

def kelvin_to_fahrenheit(k):
    c = kelvin_to_celsius(k)
    return celsius_to_fahrenheit(c)

def temperature_converter():
    print("Temperature Conversion Tool")
    print("1. Fahrenheit to Celsius")
    print("2. Celsius to Fahrenheit")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Fahrenheit to Kelvin")
    print("6. Kelvin to Fahrenheit")

    choice = int(input("\nEnter the number of your conversion choice: "))

    if choice == 1:
        f = float(input("Enter temperature in Fahrenheit: "))
        print(f"{f} Fahrenheit is {fahrenheit_to_celsius(f)} Celsius.")
    elif choice == 2:
        c = float(input("Enter temperature in Celsius: "))
        print(f"{c} Celsius is {celsius_to_fahrenheit(c)} Fahrenheit.")
    elif choice == 3:
        c = float(input("Enter temperature in Celsius: "))
        print(f"{c} Celsius is {celsius_to_kelvin(c)} Kelvin.")
    elif choice == 4:
        k = float(input("Enter temperature in Kelvin: "))
        print(f"{k} Kelvin is {kelvin_to_celsius(k)} Celsius.")
    elif choice == 5:
        f = float(input("Enter temperature in Fahrenheit: "))
        print(f"{f} Fahrenheit is {fahrenheit_to_kelvin(f)} Kelvin.")
    elif choice == 6:
        k = float(input("Enter temperature in Kelvin: "))
        print(f"{k} Kelvin is {kelvin_to_fahrenheit(k)} Fahrenheit.")
    else:
        print("Invalid choice! Please select a valid option.")

temperature_converter()
