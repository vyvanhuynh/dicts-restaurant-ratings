"""Restaurant rating lister."""
import sys

# put your code here
def restaurant_rating_dict(file):
    text = open(sys.argv[1])
    scores_dict = {}

    for line in text:
        restaurant_strip = line.rstrip()
        restaurant = restaurant_strip.split(":")
        place = restaurant[0]
        rating = restaurant[1]
        scores_dict[place] = rating
        #scores_dict.append(restaurant) # does not work for dictionaries

    for place,rating in sorted(scores_dict.items()):
        print(f"{place} is rated at {rating}.")


    #return scores_list
        # # place = restaurant[0]
        # # rating = restaurant[1]
        # # scores[place] = rating
        # for place in restaurant:
        #     scores[place] = scores.get(place,0)

        # for place,rating in scores.items():
        #     return print(f"{place} is rated at {rating}.")
        
restaurant_rating_dict("scores.txt")

