import random

# Step 1: Create an empty list with a fixed size (if you know the number of quotes beforehand)
quotes = [None] * 12  # Assuming we have 7 quotes

# Step 2: Manually assign quotes to specific indices
quotes[0] = "The greatest glory in living lies not in never falling, but in rising every time we fall. - Nelson Mandela"
quotes[1] = "The way to get started is to quit talking and begin doing. - Walt Disney"
quotes[2] = "Your time is limited, don't waste it living someone else's life. - Steve Jobs"
quotes[3] = "If life were predictable it would cease to be life, and be without flavor. - Eleanor Roosevelt"
quotes[4] = "If you look at what you have in life, you'll always have more. - Oprah Winfrey"
quotes[5] = "If you set your goals ridiculously high and it's a failure, you will fail above everyone else's success. - James Cameron"
quotes[6] = "Life is what happens when you're busy making other plans. - John Lennon"
quotes[7] = "Time is precious, waste it wisely"
quotes[8] = "Whether you think you can, or you think you can't; you're right -Henry Ford"
quotes[9] = "You can, you should, and if you’re brave enough to start, you will - Stephen King"
quotes[10] = "If I had asked people what they wanted, they would have said faster horses -Henry Ford"
quotes[11] = "Enjoy the pain (a key to not giving up)"

# Step 3: Select a random quote
random_quote = random.choice(quotes)

# Step 4: Print the selected quote
print(random_quote)
