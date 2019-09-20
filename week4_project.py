def main():
    # user_age()
    # student_check()
    # count_down()
    # correct_answer_loop()
    # print_backwards()
    # full_name("Andrew")
    # my_books()
    # print(money_check())
    # num_list()
    my_pets()


def user_age():
    year_born = int(input("Enter your year of birth: "))
    your_age = 2019 - year_born
    print(f"You are {your_age} years old!")


def student_check():
    user_name = input("Enter a string: ")
    teacher_list = ["Kenn", "Kevin", "Erin", "Autumn"]

    if user_name in teacher_list:
        print("Hello teacher!")
    else:
        print("Hello student!")


def count_down():
    user_num = int(input("Enter any negative number: "))
    for x in range(7, user_num - 1, -1):
        print(x)


def correct_answer_loop():
    user_input = int(input("Please enter a number between -10 and -5: "))
    while user_input < -10 or user_input > -5:
        user_input = int(input("Please try again: "))
    print("Good job!")


def print_backwards():
    # commented out material is alternative to print out a list that goes backwards rather than printing each
    # element individually in reverse order. I wasn't sure which one you wanted
    squad = ["One", "Two", "Three", "Four", "Five"]
    # backward = []
    for index in range(-1, -6, -1):
        print(squad[index])
    #     backward.append(squad[index])
    # print(backward)


def full_name(firstName):
    user_lname = input("What is your last name? ")
    print(f"Hello {firstName} {user_lname}!")


def my_books():
    class Books:
        def __init__(self, name, rating, genre, author):
            self.name = name
            self.rating = rating
            self.genre = genre
            self.author = author

        def change_rating(self, new_rating):
            self.rating = new_rating

    my_book1 = Books("A Great Book", 4, "Fiction", "Kevin Yancy")
    my_book2 = Books("A Better Book", 5, "Fiction", "Erin Johnson")
    my_book3 = Books("I Should Really Read More", 2, "Nonfiction", "Andrew Daunais")

    book_list = [my_book1, my_book2, my_book3]

    for eachElement in book_list:
        print(eachElement.name)


def money_check():
    user_money = int(input("Enter how much money is in your account: "))
    if user_money >= -50 and user_money <= 5:
        return "Funds too low."
    elif user_money > 5 and user_money <= 50:
        return "You should add more funds."
    elif user_money > 50:
        return "Just enough."


def num_list():
    user_num = int(input("Enter a positive number: "))
    number_list = []
    for eachNum in range(0, user_num + 1):
        number_list.append(eachNum)
    print("The contents of your array, number_list, are:")
    for eachElement in number_list:
        print(eachElement)


def my_pets():
    pet_list = []

    class Pet:
        def __init__(self, type, breed):
            self.type = type
            self.breed = breed

        def __str__(self):
            return f"Type of pet:   {self.type}\n" \
                   f"Breed of {self.type}:  {self.breed}\n"

    pet1 = Pet("Dog", "Chihuahua")
    pet2 = Pet("Cat", "Siamese")
    pet3 = Pet("Bird", "Parrot")
    pet_list.append(pet1)
    pet_list.append(pet2)
    pet_list.append(pet3)
    for eachElement in pet_list:
        print(eachElement)


main()
