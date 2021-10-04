"""Restaurant rating lister."""
import sys

# put your code here
def restaurant_rating_dict(file):
    text = open(sys.argv[1])
    scores_dict = {}
    quit = True

    while quit == True:
        restaurant_input = input("What restaurant would you like to add?: ")
        rating_input = input("What would you rate the place (0-5): ")
        if int(rating_input) > 5:
            print("Please enter a number between 0 and 5")
        else:
            scores_dict[restaurant_input] = rating_input #creates a dictionary with line 9 and 10
            for line in text:
                restaurant_strip = line.rstrip()
                restaurant = restaurant_strip.split(":")
                place = restaurant[0]
                rating = restaurant[1]
                scores_dict[place] = rating

            for place,rating in sorted(scores_dict.items()):
                print(f"{place} is rated at {rating}.")
            
            print("Did you want to add more restaurants?")
            print("1. Add more restaurants")
            print("2. Do not add anymore restaurants")
            user_choice = int(input("Please enter 1. to add more retaurants or 2. to stop adding more restaurants: "))
            if user_choice == 1:
                continue
            if user_choice == 2:
                print("Ok, thank you for your restaurants and ratings")
                break
    

restaurant_rating_dict("scores.txt")

# def restaurant_rating_input(input):
#     restaurant_input = input("What restaurant would you like to add?: ")
#     rating_input = input("What would you rate the place (0-5): ")

#     user_dict = {}
#     place = restaurant_input
#     rating = rating_input
#     user_dict[place] = rating


# def give_rating(scores_dict):
#     for place,rating in sorted(scores_dict.items()):
#         print(f"{place} is rated at {rating}.")

        
# places_visited = restaurant_rating_dict("scores.txt")
# give_rating(places_visited)
# # give_rating(places_visited)