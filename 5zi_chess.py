import random

arr = [['-' for i in range(0, 10)] for j in range(0, 10)]
user_name1 = None
user_name2 = None
space = "  "
state = True
tempo = ""
index = 0
usernametemp = ""
# this part is checked and OK
def play_again():
    for i in range(0, 10):
        for j in range(0, 10):
            arr[i][j] = '-'
    how_to_name = input("Would you like to play again?(y/n)")
    if how_to_name == 'y' or how_to_name == 'Y':
        index = 0
    else:
        exit()


def check(user):  # check if the conditions satisfy the win_condition
    if user == 1:
        t = 'o'
        usernametemp = user_name2
    else:
        t = 'x'
        usernametemp = user_name1
    for i in range(0, 10):
        # check if horizontal x-axis has 5 of the same character
        for j in range(0, 6):
            horizontal = [arr[i][j], arr[i][j + 1], arr[i][j + 2], arr[i][j + 3], arr[i][j + 4], t]
            horizontal_b = list(set(horizontal))
            if len(horizontal_b) == 1:
                print(usernametemp, " wins!")
                play_again()

    for i in range(0, 6):
        for j in range(0, 10):
            vertical = [arr[i][j], arr[i + 1][j], arr[i + 2][j], arr[i + 3][j], arr[i + 4][j], t]
            vertical_b = list(set(vertical))
            if len(vertical_b) == 1:
                print(usernametemp, " wins!")
                play_again()
    for i in range(0, 6):
        for j in range(0, 6):
            slope = [arr[i][j], arr[i + 1][j + 1], arr[i + 2][j + 2], arr[i + 3][j + 3], arr[i + 4][j + 4], t]
            slope_b = list(set(slope))
            if len(slope_b) == 1:
                print(usernametemp, " wins!")
                play_again()
    for i in range(4, 10):
        for j in range(4, 10):
            slope2 = [arr[i][j], arr[i - 1][j - 1], arr[i - 2][j - 2], arr[i - 3][j - 3], arr[i - 4][j - 4], t]
            slope2_b = list(set(slope2))
            if len(slope2_b) == 1:
                print(usernametemp, " wins!")
                play_again()


# change the value of the variable
Terry = ""

booooool = 0


# this part is the function used to check the input and write the User input into the array
def insert_char(temp, boo):
    # cut invalid inputs
    if not (2 <= len(temp) <= 3):
        Terry = input("The location you want to go has already been occupied or invalid! REENTER please: ")
        insert_char(Terry, booooool)
    else:
        if len(temp) == 3:
            if temp[2] != 0:
                Terry = input("The location you want to go has already been occupied or invalid! REENTER please: ")
                insert_char(Terry, booooool)
        if not (65 <= ord(temp[0]) <= 74 and 48 <= ord(temp[1]) <= 57):
            Terry = input("The location you want to go has already been occupied or invalid! REENTER please: ")
            insert_char(Terry, booooool)


    for i in range(0, 10):
        for j in range(0, 10):
            # tempo = chr(i+65), str(j)
            if str(temp) == chr(i + 65) + str(j) or str(temp) == chr(i + 65) + str(10):
                if boo == 0:
                    if arr[i][j - 1] == '-':
                        arr[i][j - 1] = 'o'
                        break
                    else:
                        temp = input(
                            "The location you want to go has already been occupied or invalid! REENTER please: ")
                        insert_char(Terry, booooool)
                        print("Warning2")
                        break
                    break
                elif boo == 1:
                    if arr[i][j - 1] == "-":
                        arr[i][j - 1] = 'x'
                        break
                    else:
                        temp = input(
                            "The location you want to go has already been occupied or invalid! REENTER please: ")
                        insert_char(Terry, booooool)
                        break
                        # j = 0
                        # i = 0
                break


# this part is checked and OK
def chess_base():
    space = '  '
    for i in range(0, 10):
        a = 2
        if i == 0:
            a = 6
        print(" " * a, i + 1, end="")
        if i == 9:
            print("")
    for i in range(65, 75):
        print(space, chr(i), space, end="")
        for j in range(0, 10):
            print(arr[i - 65][j], space, end="")
            if j == 9:
                print("")


ran = random.randint(0, 1)

# main iteration:
while 1 == 1:
    if index == 0:
        arr = [['-' for i in range(0, 10)] for j in range(0, 10)]
        print("Welcome to Bob's Chess Game!")
        print("-----simple gobang game <console version>-----")
        print("----------------------------------------------")
        chess_base()
        user_name1 = input("Input the first user's name: ")
        user_name2 = input("Input the second user's name: ")
        print("___________________________________________________________________")
        print(" NOTE!!!!!!!!!The input should be like 'E1' or something like that")
        print("___________________________________________________________________")
        if ran == 1:
            print("According to our random number system,", user_name1, "go first!")
        else:
            print("According to our random number system,", user_name2, "go first!")
        chess_base()
    if index % 2 == 0:
        user1 = input("Hi! What's the next step?")
        Terry = user1
        booooool = 1
        insert_char(Terry, booooool)
        check(0)
        chess_base()

    if index % 2 == 1:
        user2 = input("Hi! What's the next step?")
        Terry = user2
        booooool = 0
        insert_char(Terry, booooool)
        check(1)
        chess_base()

    index += 1
    if index == -1:
        exit()

# TODO: Extra function: you could Enter: back to go back to the last step!
# TODO: Delete from the Dictionary is also one method
