def calculate_velocity(distance, time):
    if time == 0:
        return "Time cannot be zero. Please enter a valid time."
    return distance / time
def calculate_mass(force, acceleration):
    if acceleration == 0:
        return "Acceleration cannot be zero. Please enter a valid acceleration."
    return force / acceleration
def main():
    while True:
        print("\nPhysics Calculator")
        print("1. Calculate Velocity")
        print("2. Calculate Mass")
        print("3. Exit")
        choice = input("Choose an option (1, 2, or 3): ")
        if choice == '1':
            distance = float(input("Enter the distance (in meters): "))
            time = float(input("Enter the time (in seconds): "))
            velocity = calculate_velocity(distance, time)
            print(f"The velocity is: {velocity} meters per second (m/s)")
        elif choice == '2':
            force = float(input("Enter the force (in Newtons): "))
            acceleration = float(input("Enter the acceleration (in meters per second squared): "))
            mass = calculate_mass(force, acceleration)
            print(f"The mass is: {mass} kilograms (kg)")
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
if __name__ == '__main__':
    main()
