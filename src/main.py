import math
import requests
import sys

def load_coffee_shops(url):
    linesFromFile = requests.get(url).text.splitlines()
    coffeeShopsList = []

    for line in linesFromFile:
        element_din_fisier = line.split(",")

        if len(element_din_fisier) != 3:
            print(f"Entry at {line} is invalid.")
            sys.exit(1)

        shopName = element_din_fisier[0].strip()

        # In the doc provided to me, the data may be wrong for example : Name, Y, X => Starbucks1, "100", 43 => y != float => execution ends.
        try: 
            y = float(element_din_fisier[1].strip())
            x = float(element_din_fisier[2].strip())
        except ValueError:
            print(f"Line at: {line} is not numeric....")
            sys.exit(1)

        coffeeShopsList.append((shopName, y, x))

    return coffeeShopsList


# From the problem description it is specified that the coordinates are on a plane. (2D)
# => the Euclidean distance formula is the best/standard method to calculate the distance from 2 points (client and coffee shop)
#the same approach I used in some of my previous projects, one example would be the Village Simulator, where I calculated the distance from the NPC Agent to the Checkpoints (placed on the virtual 3d environment)
def calculate_distance(user_y, user_x, shop_y, shop_x):
    return math.sqrt((shop_x - user_x)**2 + (shop_y - user_y)**2)


def main():

    if len(sys.argv) != 4:
        print("Please enter: <user_y> <user_x> <coffee_shops.csv>")
        sys.exit(1)

    #=>From the problem description, the solution is meant to run from CLI => so I choose to use sys.argv to read the INPUT arg.
    # ! Using Input() will pause the execution for manual input
   

    user_y = float(sys.argv[1]) 
    user_x = float(sys.argv[2])
    url = sys.argv[3]

    coffee_shop_list = load_coffee_shops(url)

    distances = []
    for shop_name, shop_y, shop_x in coffee_shop_list:
        dist = calculate_distance(user_y, user_x, shop_y, shop_x)
        distances.append((shop_name, dist)) 

    distances.sort(key=lambda dist: dist[1])
    
    for shop_name, dist in distances[:3]:
        print(f"{shop_name}, {dist:.4f}")    

if __name__ == "__main__":
    main()