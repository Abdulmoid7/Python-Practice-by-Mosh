    # Prompt the user to enter planet names
    num_planets = int(input("Enter the number of planets: "))
    for i in range(num_planets):
        planet_name = input(f"Enter name of planet {i+1}: ")
        planets.append(planet_name)

    # Display the entered planet names
    print("\nList of planets:")
    for planet in planets:
        print(planet)

if __name__ == "__main__":
    main()
