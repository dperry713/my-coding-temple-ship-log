def suggest_outfit(temperature):
    if temperature < 0:
        return "It's freezing! Time for your penguin cosplay: a puffy white parka, black leggings, and webbed mittens. Don't forget your beak-shaped face mask!"

    elif 0 <= temperature < 10:
        return "Brrr! Layer up with a thermal onesie, topped with a colorful ski suit. Add moon boots and a hat with ear flaps. You'll look like a fashionable yeti!"

    elif 10 <= temperature < 20:
        return "Chilly day! Go for the 'lumberjack chic' look: plaid flannel shirt, warm jeans, a beanie, and boots. Bonus points for a fake beard!"

    elif 20 <= temperature < 25:
        return "Perfect weather for your superhero alter ego: wear a tight-fitting long-sleeve shirt and leggings in your signature colors. Add a cape for dramatic effect!"

    elif 25 <= temperature < 30:
        return "Time for 'business casual meets beach bum': khaki shorts, a Hawaiian shirt, and flip-flops. Don't forget your briefcase-shaped cooler!"

    elif 30 <= temperature < 35:
        return "Hot day! Channel your inner fruit salad: wear a yellow shirt (banana), green shorts (kiwi), and a red hat (strawberry). Stay cool and delicious!"

    else:
        return "It's scorching! Embrace your inner desert nomad: loose, flowy clothes in light colors, a turban-style head wrap, and sandals. Carry a personal misting fan for that oasis effect!"

# Get temperature input from the user
try:
    temp = float(input("Enter the temperature in Celsius: "))
    outfit = suggest_outfit(temp)
    print(outfit)
except ValueError:
    print("Please enter a valid number for the temperature.")