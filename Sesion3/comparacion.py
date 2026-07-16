while True:
    food = input("What's the best food? (type 'exit' to stop): ").lower()
    if food == "rice":
        print("Yes, rice is the best.")
    elif food == "apple":
        print("Apples aren't my cup of rice.")
    elif food == "Mote de queso":
        print("Great election!")
    elif food == "exit":
        break
    else:
        print("Never heard of it!")

# your first while loop: can you guess what it does?
'''limit = 12

counter = 1
while counter < limit + 1:    print(counter)
    #counter = counter + 1
    counter += 2
'''