
phonebook = {
    "Bhasker": "201-620-1115",
    "Geetha": "876-214-2863",
    "Sita": "555-123-4567"
}


while True:
    print("\nPhonebook Lookup")
    name = input("Enter a name : ")

    if name.lower() == 'exit':
        print("Exiting the phonebook. Goodbye!")
        break

    if name in phonebook:
        print(f"{name}'s phone number is {phonebook[name]}")
    else:
        print(f"{name} is not found in the phonebook.")
