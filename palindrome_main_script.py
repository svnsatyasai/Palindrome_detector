
def palindrome_check(list1):
    final_list = []
    try:
        for x in list1:
            if x.replace(" ", "").upper() == x[::-1].replace(" ", "").upper():
                final_list.append(x)
    except Exception as e:
        print(e)
    print ("The following are the palindromes : " + " Total - " + str(len(final_list)))
    print (final_list)
    return final_list


def read_file():
    whole_list = []
    try:
        file_path = 'English.txt'  # mention file full path here
        with open(file_path, 'r') as f_read:
            whole_data = f_read.read()
            whole_data = whole_data.strip()
            whole_list = whole_data.split('\n')
    except Exception as e:
        print (e)
    return whole_list


data_list = read_file()
data_list = list(set(data_list))

Palindromes_result = palindrome_check(data_list)
