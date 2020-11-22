import hashlib


class User:
    def __init__(self):
        self.user_name = user_name


def make_hash_pw(password):
    p = hashlib.sha256(password)
    p = p.hexdigest()
    return p


def check_hash_pw(pw, hash_val):
    p = make_hash_pw(str.encode(pw))
    if p == hash_val:
        return True
    else:
        return False


while True:

    print("1. Login")
    print("2. Create account")
    print("3. Exit Program")
    print("")
    input_int = input("Enter 1, 2 or 3 accordingly: ")

    try:
        input_int = int(input_int)
    except ValueError:
        print("Invalid Input...Please Try Again")
        print()
        continue

    ''' # To reset the file:
    write_file = open("login_users.txt", "w")
    write_file.write("")
    write_file.close()
    '''

    # Following 2 lines print the file with all usernames and passwords
    read_file = open("login_users.txt", 'r')
    # print(read_file.read())  # print the file & has to be b4 the following line(cuz same var getting changed)!
    read_file = read_file.read()

    read_file_list = read_file.split('\n')

    user_name_dict = {}  # dict with all usernames as keys and their index in user_name_list as values
    # Fill the dict:
    for i in range(len(read_file_list)):
        if i % 3 == 0:
            user_name_dict[read_file_list[i]] = i

    # read_file = read_file.readlines()

    # -----FIRST CASE-----
    if input_int == 1:
        first_case_exit = False
        while True:
            if not first_case_exit:
                existing_username = input("Username: ")
            else:
                existing_username = input("\nEnter 'b' to go back OR \nEnter Username: ")

            if existing_username == 'b':
                break
            if existing_username in user_name_dict:
                for i in range(3):
                    existing_password = input("Password: ")
                    if check_hash_pw(existing_password, read_file_list[user_name_dict[existing_username]+1]):
                        print("***LOGIN SUCCESSFUL***")
                        break
                    else:
                        print("Incorrect! ", 2-i, " attempts left")
                # print("3 attempts failed! ")
                break
            else:
                print("Username doesn't exist. Please try again! ")
                first_case_exit = True
    # -----SECOND CASE-----
    elif input_int == 2:
        write_file = open("login_users.txt", "a")  # open file to write the new username and password to it

        # user = User()
        while True:
            new_username = input("Enter Username: ")
            if new_username in user_name_dict:
                print("Username is taken, please try another one! ")
            else:
                break
        new_password = input("Enter password: ")
        write_file.write(new_username)
        write_file.write("\n")
        write_file.write(make_hash_pw(str.encode(new_password)))
        write_file.write("\n\n")
        # write_file.write("\n")
        write_file.close()

        print("***Account Created and saved :)")
        # user.name= user_name

    # -----THIRD CASE-----
    elif input_int == 3:
        print("Goodbye :)")
        break




