# Define functions for equations in each unit
import math 

# Unit 1: Kinematics
def kinematics():
    print("\nKinematics Equations:")
    print("1. v = u + at")
    print("2. s = ut + 0.5at^2")
    print("3. v^2 = u^2 + 2as")
    
    choice = input("Choose an equation (1, 2, 3): ")
    
    if choice == "1":
        u = float(input("Enter initial velocity (u) in m/s: "))
        a = float(input("Enter acceleration (a) in m/s^2: "))
        t = float(input("Enter time (t) in seconds: "))
        v = u + a * t
        print(f"The final velocity (v) is: {v} m/s")
    
    elif choice == "2":
        u = float(input("Enter initial velocity (u) in m/s: "))
        a = float(input("Enter acceleration (a) in m/s^2: "))
        t = float(input("Enter time (t) in seconds: "))
        s = u * t + 0.5 * a * t ** 2
        print(f"The displacement (s) is: {s} meters")
    
    elif choice == "3":
        u = float(input("Enter initial velocity (u) in m/s: "))
        a = float(input("Enter acceleration (a) in m/s^2: "))
        s = float(input("Enter displacement (s) in meters: "))
        v = (u ** 2 + 2 * a * s) ** 0.5
        print(f"The final velocity (v) is: {v} m/s")
    
    else:
        print("Invalid choice, try again.")
        kinematics()

# Unit 2: Dynamics
def dynamics():
    print("\nDynamics Equations:")
    print("1. F = ma")
    print("2. W = Fd cos(θ)")
    print("3. F_gravity = mg")
    
    choice = input("Choose an equation (1, 2, 3): ")
    
    if choice == "1":
        m = float(input("Enter mass (m) in kg: "))
        a = float(input("Enter acceleration (a) in m/s^2: "))
        F = m * a
        print(f"The force (F) is: {F} N")
    
    elif choice == "2":
        F = float(input("Enter force (F) in N: "))
        d = float(input("Enter displacement (d) in meters: "))
        theta = float(input("Enter angle (θ) in degrees: "))
        W = F * d * (math.cos(math.radians(theta)))
        print(f"The work (W) is: {W} Joules")
    
    elif choice == "3":
        m = float(input("Enter mass (m) in kg: "))
        g = 9.8  # gravitational acceleration in m/s^2
        F_gravity = m * g
        print(f"The gravitational force (F_gravity) is: {F_gravity} N")
    
    else:
        print("Invalid choice, try again.")
        dynamics()

# Unit 3: Circular Motion
def circular_motion():
    print("\nCircular Motion Equations:")
    print("1. F_c = mv^2 / r")
    print("2. T = 2πr / v")
    
    choice = input("Choose an equation (1, 2): ")
    
    if choice == "1":
        m = float(input("Enter mass (m) in kg: "))
        v = float(input("Enter velocity (v) in m/s: "))
        r = float(input("Enter radius (r) in meters: "))
        F_c = (m * v ** 2) / r
        print(f"The centripetal force (F_c) is: {F_c} N")
    
    elif choice == "2":
        r = float(input("Enter radius (r) in meters: "))
        v = float(input("Enter velocity (v) in m/s: "))
        T = (2 * math.pi * r) / v
        print(f"The period (T) is: {T} seconds")
    
    else:
        print("Invalid choice, try again.")
        circular_motion()

# Main Menu
def main_menu():
    import math
    
    print("\nWelcome to the AP Physics 1 Calculator")
    print("Select a unit:")
    print("1. Kinematics")
    print("2. Dynamics")
    print("3. Circular Motion")
    print("4. Exit")
    
    choice = input("Enter the number corresponding to the unit: ")
    
    if choice == "1":
        kinematics()
    elif choice == "2":
        dynamics()
    elif choice == "3":
        circular_motion()
    elif choice == "4":
        print("Goodbye!")
        exit()
    else:
        print("Invalid choice, try again.")
        main_menu()

# Run the program
if __name__ == "__main__":
    main_menu()
