def get_unique_destinations(filepath):

    try:
        with open(filepath, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("Error: The file was not found.")
        return

    if len(lines) < 2:
        print("Error: The file is empty or does not have sufficient data.")
        return


    header = [h.strip().strip('"') for h in lines[0].strip().split(',')]

    try:
        origin_city_index = header.index("Origin_city")
        destination_city_index = header.index("Destination_city")
    except ValueError:
        print("Error: Required columns 'Origin_city' and 'Destination_city' are not found in the file.")
        return

    user_origin_city = input("Please enter your origin city: ").strip()

    unique_destinations = set()

    for line in lines[1:]:
        parts = [p.strip().strip('"') for p in line.strip().split(',')]

        if len(parts) > max(origin_city_index, destination_city_index):
            try:
                origin_city = parts[origin_city_index]
                destination_city = parts[destination_city_index]
            except IndexError:
                continue

            if origin_city.lower() == user_origin_city.lower():
                unique_destinations.add(destination_city)

    if unique_destinations:
        print(f"List of unique destinations from {user_origin_city}:")
        for destination in unique_destinations:
            print(destination)
    else:
        print(f"No destinations found for the given origin city: {user_origin_city}")

filepath = "/Users/lucashandlon/Desktop/Information Infrastructure/Airports2.csv"
get_unique_destinations(filepath)
