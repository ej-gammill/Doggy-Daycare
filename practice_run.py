import json


# Press Shift+F10 to execute it or replace it with your code.
def view_pets(pets):
    for pet_name in pets:
        pet = pets[pet_name]
        pet_age = pet['age']
        pet_breed = pet['breed']
        pet_size = pet['size']
        print(f'      {pet_name}')
        print(f'       pet\'s breed: {pet_breed}')
        print(f'       pet\'s size: {pet_size}')
        print(f'       pet\'s age: {pet_age}')




# Functions
# Dictionary usage v
def view_owners(owners):
    print('Owners in our system:')
    sorted_owners = sorted(owners)
    for username in sorted_owners:
        owner = owners[username]
        print_owner(owner)

def print_owner(owner):
    first_name = owner['first_name']
    last_name = owner['last_name']
    phone_number = owner['phone_number']
    print(f'{first_name} {last_name}')
    print(f'  Phone Number: {phone_number}')
    print(f'  Pets:')
    pets = owner['pets']
    view_pets(pets)
    print()

def add_owner(owners):
    first_name = input('Enter first name: ')
    last_name = input('Enter last name: ')
    phone_number = input('Enter phone number: ')
    pets = {}
    owner = {
        'first_name': first_name,
        'last_name': last_name,
        'phone_number': phone_number,
        'pets': pets
    }
    username = f'{first_name} {last_name}'
    owners[username] = owner
    save_owners(owners)


# worked on & a little confused for how to enter owner's name in code for system to remove#
def remove_owner(owners):
    remove_owner = input('Enter owner: ')
    if remove_owner in owners:
        print('Are you sure?')
    else:
        print('Owner not found')
        return
    owner = owners[remove_owner]
    print_owner(owner)
    user_reply = input('Yes or no: ')
    user_reply = user_reply.lower()
    if user_reply == 'no':
        print('Owner deletion cancelled')
    elif user_reply == 'yes':
        del owners[remove_owner]
        save_owners(owners)
        print('Owner deletion confirmed.')
    else:
        print('Error: Unexpected input, owner deletion is cancelled')


def add_pet(owners):
    username = input('Enter owner\'s name: ')
    owner = owners[username]
    # add a new pet name from our "pets" list
    pet_name = input('Enter new pet\'s name: ')
    pet_age = input('Enter new pet\'s age: ')
    pet_age = int(pet_age)
    pet_breed = input('Enter new pet\'s breed: ')
    pet_size = input('Enter new pet\'s size: ')
    owner_pets = owner['pets']
    owner_pets[pet_name] = {
        'age': pet_age,
        'breed': pet_breed,
        'size': pet_size,
    }
    save_owners(owners)


def remove_pets(owners):
    # remove an existing pet name from our "pets" list
    username = input('Enter Owner: ')
    if username not in owners:
        print('Owner not found')
        return
    remove_pet = input('Enter pet: ')
    # del owners[remove_owner]
    owner = owners[username]
    print_owner(owner)
    pets = owner['pets']
    if remove_pet not in pets:
        print('Pet not found')
        return
    pet = pets[remove_pet]
    # TODO we left off here
    del pets[remove_pet]
    # save_pet_names(pets)
    print_owner(owner)
    user_reply = input('Yes or no: ')
    user_reply = user_reply.lower()
    if user_reply == 'no':
        print('Owner deletion cancelled')
    elif user_reply == 'yes':
        del owners[remove_owner]
        save_owners(owners)
        print('Owner deletion confirmed.')
    else:
        print('Error: Unexpected input, owner deletion is cancelled')

def load_owners() -> dict:
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
            # worked on
            remove_owner(owners)
        elif request == 'add pet':
            add_pet(owners)
        elif request == 'remove pet':
            # worked on
            remove_pets(owners)
        elif request == 'exit':
            # if the user wants to quit then we break out of our infinite while loop and
            # the program will quit
            break