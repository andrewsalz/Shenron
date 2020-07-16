def letters(user_input):
    
    result = ""
    num_count = 0
    empt_str = ""
    joint = ""
    s = 0

    while s < len(user_input):
        if user_input[s].isnumeric() == True:
            empt_str += user_input[s]
            s += 1
            while user_input[s].isnumeric() == True:
                empt_str += user_input[s]
                s += 1
            joint = int(empt_str)
            empt_str = ""
            result += (joint * user_input[s])
            s += 1

        else:
            empt_str = user_input[s]
            num_count += 1
            s += 1
            while s < len (user_input) and empt_str == user_input[s]:
                num_count += 1
                s += 1
            result += str(num_count) + user_input[s-1]
            num_count = 0
            empt_str = ""

    print(result)


user_input = input("Enter your string of numbers and letters: ")

letters(user_input)