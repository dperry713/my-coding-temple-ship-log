def get_age_recommendation(rating):
    rating = rating.upper()
    if rating == "G":
        return "General Audience - Suitable for all ages."
    elif rating == "PG":
        return "Parental Guidance Suggested - Some material may not be suitable for children."
    elif rating == "PG-13":
        return "Parents Strongly Cautioned - Some material may be inappropriate for children under 13."
    elif rating == "R":
        return "Restricted - Under 17 requires accompanying parent or adult guardian."
    elif rating == "NC-17":
        return "Adults Only - No one 17 and under admitted."
    else:
        return "Invalid rating. Please enter G, PG, PG-13, R, or NC-17."

# Prompt user for movie rating
movie_rating = input("Enter the movie rating (G, PG, PG-13, R, or NC-17): ")

# Get and display the age recommendation
recommendation = get_age_recommendation(movie_rating)
print(recommendation)