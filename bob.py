known_users = ["Alice", "Bob", "Claire", "Dan", "Emma", "Fred", "Georgie", "Harry"]
print (len(known_users))

while True:
    print("Hi! My name is Bob")
    name = input("What is your name?: ").strip().capitalize()

    if name in known_users:
        print("Hello {}".format(name))
        remove = input("Would you like to be removed from the system (y/n)?:").lower()

        if remove == "y":
            known_users.remove(name)
        elif remove == "n":
            print("Okay you are sitll in the system.")
            
    else:
        print("You are not in the system.")
        add_me = input("Would you like to be added to the system? (y/n): ").strip().lower()
        if add_me == "y":
            known_users.append(name)
        elif add_me =="n":
            print("Okay you have not been added.")
