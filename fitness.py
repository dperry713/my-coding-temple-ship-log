def get_health_advice(minutes):
    if minutes < 10:
        return "You might want to start considering those 10-minute exercise videos as a major life improvement. Remember, every little bit helps, and so does that extra slice of pizza if you’re exercising too little!"
    elif 10 <= minutes < 30:
        return "Good job! You're in the 'I exercise, but I still binge-watch Netflix' zone. Keep it up, and soon you’ll be able to lift those remote controls with ease and maybe even do a few push-ups in between episodes."
    elif 30 <= minutes < 60:
        return "Fantastic! You’re in the 'I exercise regularly, but my couch misses me' category. Keep it up, and you might just find yourself running away from zombies in your dreams. Or at least your jeans will fit better!"
    elif 60 <= minutes < 90:
        return "Wow, you’re practically a fitness guru! Just remember, even the most dedicated athletes need a day off to eat nachos and contemplate life’s mysteries. You’re balancing both brilliantly!"
    else:
        return "You are a fitness legend! Your dedication is so high that even superheroes might need to take notes. Just make sure to mix in some rest days, or you might start developing superpowers like 'endless endurance' or 'superhuman hunger.'"

def main():
    while True:
        try:
            user_input = input("How many minutes per day do you exercise? ")
            minutes = float(user_input)
            if minutes < 0:
                print("Negative minutes? Are you a time traveler from the future? Try again with a positive number!")
                continue
            
            advice = get_health_advice(minutes)
            print(advice)
            break  # Exit the loop after providing advice
        except ValueError:
            print("Oops! That doesn't look like a valid number. Try again, and this time, maybe leave out the letters!")

if __name__ == "__main__":
    main()
