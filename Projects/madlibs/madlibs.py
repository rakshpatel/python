# String concatination
# We are creating a string that says "subscribe to ________"

# youtuber = "Rakshit"

# Multiple ways to concatenate
# message = "Subscribe to"
# print(message +" "+ youtuber)
# print("{} {}".format(message, youtuber))
# print(f"{message} {youtuber}")

adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous person: ")
madlib = "Computer programming is so {}! It makes me so excited all the time because \
I love to {}. Stay hydrated and {} like you are {}!".format(adj, verb1, verb2, famous_person)

print(madlib)