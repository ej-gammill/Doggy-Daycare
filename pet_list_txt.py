# Press Shift+F10 to execute it or replace it with your code.

# Functions
def view_pets(pets):
    # view (aka print) pet names from our "pets" list
    print('Pets in our system:')
    sorted_pets = sorted(pets)
    for pet in sorted_pets:
        print(pet)


def add_pets(pets):
    # add a new pet name from our "pets" list
    new_pet = input('Enter new pet: ')
    pets.append(new_pet)
    save_pet_names(pets)


def remove_pets(pets):
    # remove an existing pet name from our "pets" list
    remove_pet = input('Enter pet: ')
    pets.remove(remove_pet)
    save_pet_names(pets)


def load_pet_names():
    pet_list = []
    with open('pet_list.txt', 'r') as f:
        for pet_name in f:
            pet_list.append(pet_name.rstrip())
    return pet_list


def save_pet_names(pets):
    with open('pet_list.txt', 'w') as f:
        for pet in pets:
            f.write(pet + '\n')


if __name__ == '__main__':
    pets = load_pet_names()
    # Infinite Loop
    while True:
        print('Options: [view, add, remove, exit]')
        # 'view' or 'add' or 'remove' or 'exit'
        request = input('Enter: ')
        if request == 'view':
            view_pets(pets)
        elif request == 'add':
            add_pets(pets)
        elif request == 'remove':
            remove_pets(pets)
        elif request == 'exit':
            # if the user wants to quit then we break out of our infinite while loop and
            # the program will quit
            break
