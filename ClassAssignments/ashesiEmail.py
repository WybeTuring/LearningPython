def ashesiEmail():
    from random import randint
    name1 = input("Enter your first name: ")
    name2 = input("Enter your last name: ")
    rank = int(input("Are you a student or a staff member? Enter 1 for student and 2 for staff: "))
    if rank == 1:
        mail = name1.lower() + "." + name2.lower() + "@ashesi.edu.gh"
        gmail1 = name1.lower() + name2.lower() + "@gmail.com"
        gmail2 = name2.lower()+ name1.lower() + "." + "@gmail.com"
        gmail3 = name2.lower()+ name1.lower() + str(randint(0,300)) + "." + "@gmail.com"
        print("Choose from amongst the gmail accounts below;")
        print("\t\t", gmail1)
        print("\t\t", gmail2)
        print("\t\t", gmail3)
    elif rank == 2:
        mail = name1.lower()[0] + name2.lower() + "@ashesi.edu.gh"
    else:
        print("You did not reply correctly")
        return 0
    print("Your Ashesi Email is",mail)
ashesiEmail()
