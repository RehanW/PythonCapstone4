import datetime # we need to import datetime to be able to see what is overdue
# COMPULSORY TASK 1

# First we need to prompt the user for a username and we will declare a variable that we will use for testing.
login = input("Please enter your username and password in this format: username, password: ")
login_details = ""
nr_users = 0
nr_tasks = 0
vm = ""
logged_in = True

# We will add functions to the program, which we will define below
# First function is for registering a user
def reg_user():
    with open("user.txt", "a+")as uf:                                   # Open user.txt so that we can work in the file
        new_username = input("Please provide a new username: ")
        check_user(new_username)                                        # Calls the function to check if user exists
        username = check_user(new_username)                             # Calls the value of the username that was checked
        new_password = input("Please provide a password: ")
        pass_confirmation = input("Please retype the password: ")
        if new_password == pass_confirmation:                           # Validation before saving the new user
            print("new user saved")
            uf.write("\n" + username + ", " + new_password)             # Write the new user to the file
        else:
            while new_password != pass_confirmation:  # If validation fails we will loop until we can successfully validate new user
                print("The passwords do not match")
                new_username = input("Please provide a new username: ")
                check_user(new_username)                                # Calls the function to check if user exists
                username = check_user(new_username)                     # Calls the value of the username that was checked
                new_password = input("Please provide a password: ")
                pass_confirmation = input("Please retype the password: ")
                if new_password == pass_confirmation:
                    print("new user saved")
                    uf.write("\n" + username + ", " + new_password)     # Write the new user to the file
                    break                                               # Validation is successful and loop is forced to exit
                else:
                    print("The passwords do not match")
                    new_username = input("Please provide a new username: ")
                    new_password = input("Please provide a password: ")
                    pass_confirmation = input("Please retype the password: ")
                    continue                                            # Validation failed and loop is forced to rerun

# We will define a function to see if a user exists
def check_user(username):
    with open("user.txt", "r+", encoding="utf-8")as uf:
        user_exists = False                                             # Set a bool for our while loop
        username_str = ""                                               # Declare a string for testing
        for ele in uf:
            username_str += ele + " "                                   # Add the values read to the string
        if username in username_str:                                    # Test if the username is in the string
            print("This user exists")
            user_exists = True                                          # If it is sets the bool value to True
        while user_exists:
            new_username = input("Please provide a new username: ")
            if new_username in username_str:                            # Check if the new username entered is in the string
                print("This user exists")
                continue                                                # Force repeat of loop if it is in the string
            else:
                user_exists = False                                     # Changes bool value to False
                break                                                   # Force break the loop
    return new_username                                                 # Force return a value that will be used when we call the function

# Next we will define a function to add tasks
def add_task():
    task_assign_user = input("Please provide username to whom the task is assigned: ")
    task_assign_title = input("Please provide the title of the task: ")
    task_assign_desc = input("Please provide the description of the task: ")
    task_assign_due = input("Please provide the due date of the task: ")
    with open("tasks.txt", "a", encoding="utf-8")as tf:                 # Open the file that we want to work in
        tf.write("\n" + task_assign_user + ", " + task_assign_title + ", " +
                 task_assign_desc + ", " + task_assign_due + ", No")    # Write the task to the file

# Next we will define a function to view all tasks
def view_all():
    with open("tasks.txt", "r", encoding='utf_8')as tf:                 # Open the file that we want to retrieve information from
        va = tf.read()
        print(va)

# Next we will define a function to use within our function to view a specific user's tasks
def print_KV(dictionary):
    for key, val in dictionary.items():
        print(key, "=>", val)

# Next we will define a function to use within our function to view a specific user's tasks
def write_where_match(list, i):
    with open("tasks.txt", "r+", encoding="utf-8-sig")as tf:
        data = tf.readlines()
    data[i] = ", ".join(list[i]) + '\n'
    string = data[0] + data[1] + data[2] + data[3]
    with open("tasks.txt", "w+")as ttf:
        ttf.write(string)
    data = []

# Next we will define a function to view a specific user's tasks
def view_mine():
    with open("tasks.txt", "r")as tf:  # Open the file that we want to retrieve information from and it will close after we are done
        i = 0
        y = 1
        vm_lst = []
        login_lst = login.split(",")
        vm_dict = {}
        for line in tf:  # We work line by line to test if the task is assigned to the user and if it is we print it out
            vm = line.strip()
            vm_lst.append(vm.split(","))
        string = ', '.join(vm_lst[0])

    for element in range(len(vm_lst) - 1):
        if vm_lst[i][0] == login_lst[0]:  # User test
            vm_dict.update({y: vm_lst[i][:]})
            y += 1
            i += 1

    print_KV(vm_dict)   # Use a function defined earlier to print the tasks out neatly

# Next we will prompt the user for what they want to do next and test if they want to go back
    user_choice = int(input("Please enter the number of the task you would like to edit or '-1' to go back to main menu: "))
    if user_choice == -1:
        logged_in = True    # Force the program back to the top of the while loop

# Next we will check up the value that the user entered that is not the one made for going back
    elif user_choice > 0:
        if vm_lst[user_choice - 1][5] == ' Yes':        # If they chose to change a task that has been completed they will receive an error message
            print("Sorry you can only edit tasks that hasn't been completed")
        else:
            second_choice = input("Please chose edit or mark as complete: ")    # Prompt user for a second option of what to do next
            if second_choice == "mark as complete":
                if vm_dict[user_choice] in vm_lst:

                    #If the choice was to mark as complete the following code gets executed
                    if vm_lst[0] == vm_dict[user_choice]:
                        vm_lst[0][5] = 'Yes'
                        write_where_match(vm_lst, 0)

                    elif vm_lst[1] == vm_dict[user_choice]:
                        vm_lst[1][5] = 'Yes'
                        write_where_match(vm_lst, 1)

                    elif vm_lst[2] == vm_dict[user_choice]:
                        vm_lst[2][5] = 'Yes'
                        write_where_match(vm_lst, 2)

                    elif vm_lst[3] == vm_dict[user_choice]:
                        vm_lst[3][5] = 'Yes'
                        write_where_match(vm_lst, 3)
                else:                                       # Error message encase of wrong input
                    print("That task is not yours")

            # If the choice was edit the following code gets executed
            if second_choice == "edit":
                # prompt user for a third choice
                third_choice = input("Please specify what you would like to change (user or due date): ")

                # If the choice was user the following code gets executed
                if third_choice == "user":
                    # Prompt for a new user to be assigned to the task
                    new_user = input("Please enter the new user: ")
                    # Write to the task file
                    if vm_lst[user_choice - 1][0] == 'admin':
                        vm_lst[user_choice-1][0] = new_user
                        write_where_match(vm_lst, user_choice - 1)

                # If the choice was due date the following code gets executed
                elif third_choice == "due date":
                    # Prompt for new due date of the task
                    new_dd = input("Please enter the new due date: ")
                    # Write to the task file
                    if vm_lst[user_choice - 1][4]:
                        vm_lst[user_choice - 1][4] = new_dd
                        write_where_match(vm_lst, user_choice - 1)


# Here we will define a function called gen_reports
def gen_reports():
    # First we declare all of the variables that we will need
    t_lst = []
    i = 0
    f = 0
    j = 0
    k = 0
    count_t_complete = 0
    count_t_incomplete = 0
    date_lst = []
    incomplete_overdue = 0
    user_lst = []
    user_registered = []
    tasks_assigned = 0

    # Next we will calculate the datetime
    current_date = datetime.datetime.now()
    current_date_formatted = current_date.strftime("%d %m %Y")
    c_date_lst = current_date_formatted.split(" ")

    # Here we will read a file and save it in a list for later use
    with open("user.txt", "r", encoding="utf-8-sig")as f2in:
        for line in f2in:
            user = line.strip()
            user_lst.append(user.split(","))

        for ele in user_lst:
            user_registered.append(user_lst[j][0])
            j += 1

        for ele in t_lst:
            if user_registered[k] in ele:
                tasks_assigned += 1

    # Here we will again read a file and save it in a list for later use
    with open("tasks.txt", "r", encoding="utf-8-sig")as f1in:
        for line in f1in:
            t = line.strip()
            t_lst.append(t.split(","))

    # Check if tasks are completed or not
    for ele in t_lst:
        if "Yes" in t_lst[i][5]:
            count_t_complete += 1
        elif "No" in t_lst[i][5]:
            count_t_incomplete += 1

        # Check date for the task
        date = t_lst[i][4]
        i += 1
        date = date.strip()
        date_lst.append(date.split(" "))

    # Compare the dates to see if task is overdue
    for ele in range(len(date_lst)):
        if int(date_lst[f][2]) > int(c_date_lst[2]):
            if int(date_lst[f][1]) > int(c_date_lst[1]):
                if "No" in t_lst[f][5]:
                    incomplete_overdue += 1
        f += 1

    # Formulae to calculate the output values in the output files
    percent_incomplete = (count_t_incomplete / (count_t_incomplete + count_t_complete)) * 100
    percent_complete = (count_t_complete / (count_t_incomplete + count_t_complete)) * 100
    percent_overdue = (incomplete_overdue / (count_t_incomplete + count_t_complete)) * 100
    percent_tasks = (tasks_assigned / (count_t_incomplete + count_t_complete)) * 100

    # Write output to the first file
    with open("task_overview.txt", "w", encoding="utf-8-sig")as f1out:
        f1out.write("Amount of task completed: " + str(count_t_complete) + '\n' + "Amount of tasks incomplete: " +
                    str(count_t_incomplete) + '\n' + "Amount of tasks incomplete and overdue: " + str(
            incomplete_overdue)
                    + '\n' + "Percent tasks incomplete: " + str(percent_incomplete) + '\n' + "Percent tasks overdue: "
                    + str(percent_overdue))

    # Write output to the second file
    with open("user_overview.txt", "w", encoding="utf-8-sig")as f2out:
        f2out.write("Total number of users registered: " + str(len(user_registered)) + '\n' + str(user_registered[0])
                    + " has " + str(tasks_assigned) + " tasks assigned to them" + '\n' +
                    "The percentage of tasks assigned to " + str(user_registered[0]) + " is: " + str(percent_tasks) +
                    '\n' + "The percent tasks that have been completed: " + str(percent_complete) + '\n' +
                    "The percent tasks that must still be completed: " + str(percent_incomplete) + '\n' +
                    "The percent tasks that is overdue: " + str(percent_overdue))

# Here we will define the function statistics
def statistics():
    gen_reports()
    #u_over_lst = []
    #t_over_lst = []
    with open("user_overview.txt", "r", encoding="utf-8-sig") as f1in:
        for line in f1in:
            l = line.strip()
            print(l)

    with open("task_overview.txt", "r", encoding="utf-8-sig")as f2in:
        for line in f2in:
            l = line.strip()
            print(l)

# Now we will open the file and run test with the input against the file information.
with open("user.txt", "r+") as f:       # Open user.txt and adds information to a variable that will be used for validation
    for line in f:
        login_details += line
        login_lst = login_details.split("\n")
    if login in login_lst:
        print("You've logged in successfully")
    elif login not in login_lst:
        print("This user does not exist, please try again")
        while login not in login_lst:
            login = input("Please enter your username and password in this format: username, password: ")
            if login in login_lst:
                print("You've logged in successfully")
                break
            elif login not in login_lst:
                print("This user does not exist, please try again")
                continue

while logged_in:
    # Next we need to prompt the user for the selection of what he/she wants to do in the program.
    if login == "admin, adm1n":                                 # Part 2 of the task's implementation
        reason = input("Please select on of the following options:" + "\n" + "s " + "-" + " view statistics" + "\n" +
                       "r " + "-" + " register user" + "\n" + "a " + "-" + " add task" + "\n" + "va " + "-" +
                       " view all tasks" + "\n" + "vm " + "-" + " view my tasks" + "\n" + "gr " + "-" + " generate"
                       " report" + "e " + "-" + " exit" + "\n")
    else:
        reason = input("Please select on of the following options:" + "\n" + "r " + "-" + " register user" + "\n" +
                       "a " + "-" + " add task" + "\n" + "va " + "-" + " view all tasks" + "\n" + "vm " + "-" +
                       " view my tasks" + "\n" + "e " + "-" + " exit" + "\n")

    # Here we will code the behavior if "s" was selected.
    if reason == "s":
        statistics()

    # Here we will code the behavior if "r" was selected.
    if reason == "r":
        if login == "admin, adm1n":                     # Test if user is admin because this function is reserved for admin.
            reg_user()                                  # Here we will call the reg_user function to add a new user
        else:                                           # Message shown if the user is not admin
            print("Sorry this function is reserved for the admin.")

    # Here we will code the behavior if "a" was selected.
    elif reason == "a":
        add_task()                                      # Here we will call the add_task function to add new tasks

    # Here we will code the behavior if "va" was selected.
    elif reason == "va":
        view_all()                                      # Here we will call the view_all function to view all tasks in task file

    # Here we will code the behavior if "vm" was selected.
    elif reason == "vm":
        view_mine()                                     # Here we will call the view_mine function to view a specific user's tasks

    # Here we will code the behavior if "gr" was selected.
    elif reason == "gr":
        gen_reports()


    # Here we will code the behavior if "e" was selected.
    elif reason == "e":
        print("thanks for using task_manager!!")
        exit()                                      # Exit the program