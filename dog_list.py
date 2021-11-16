
import json

# Press Shift+F10 to execute it or replace it with your code.

# Functions
def view_pets(pets):
    # view (aka print) pet names from our "pets" list
    print('Pets in our system:')
    sorted_pets = sorted(pets)
    for pet in sorted_pets:
        print(pet)

#Dictionary usage v
def view_owners(owners):
    print('Owners in our system:')
    sorted_owners = sorted(owners)
    for username in sorted_owners:
        owner = owners[username]
        first_name = owner['first_name']
        last_name = owner['last_name']

        print(f'{username} ({first_name} {last_name}')
        pets = owner['pets']
        for pet_name in pets:
            pet = pets[pet_name]
            pet_age = pet['age']
            print(f'  {pet_name} {pet_age}')


def add_owner(owners):
    first_name = input('Enter first name: ')
    last_name = input('Enter last name: ')
    pets = {}
    owner = {
        'first_name': first_name,
        'last_name': last_name,
        'pets': pets
    }
    username = f'{first_name} {last_name}'
    owners[username] = owner
    save_owners(owners)


def add_pet(owners):
    first_name = input('Enter owner\'s first name: ')
    last_name = input('Enter owner\'s last name: ')
    username = f'{first_name} {last_name}'
    owner = owners[username]
    # add a new pet name from our "pets" list
    pet_name = input('Enter new pet\'s name: ')
    pet_age = input('Enter new pet\'s age: ')
    pet_age = int(pet_age)
    owner_pets = owner['pets']
    owner_pets[pet_name] = {
        'age': pet_age
    }
    save_owners(owners)



def remove_pets(pets):
    # remove an existing pet name from our "pets" list
    remove_pet = input('Enter pet: ')
    pets.remove(remove_pet)
    # save_pet_names(pets)


def load_owners():
    with open('owners.json', 'r') as f:
        owners = json.load(f)
    return owners


def save_owners(owners):
    with open('owners.json', 'w') as f:
        json.dump(owners, f, indent=2)


if __name__ == '__main__':
    owners = load_owners()
    # Infinite Loop
    while True:
        print('Options: [view, add owner, remove owner, add pet, remove pet, exit]')
        # 'view' or 'add' or 'remove' or 'exit'
        request = input('Enter: ')
        if request == 'view':
            view_owners(owners)
        elif request == 'add owner':
            add_owner(owners)
        elif request == 'remove owner':
            pass
        elif request == 'add pet':
            add_pet(owners)
        elif request == 'remove pet':
            pass
        elif request == 'exit':
            # if the user wants to quit then we break out of our infinite while loop and
            # the program will quit
            break
