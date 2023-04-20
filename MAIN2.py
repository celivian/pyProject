def bracket_check(test_string):
    if test_string:
        if test_string[0] == '(' and test_string[-1] == ')' and test_string.count('(') == test_string.count(')'):
            while test_string:
                for i in range(len(test_string)):
                    if test_string[i] == '(':
                        for j in range(len(test_string[i:])):
                            if test_string[i:][j] == ')':
                                test = test_string
                                test_string = test_string[i + 1:j]
                                test_string += test[j + 1:]
                                break

                    else:
                        if len(test_string) <= 2:
                            break
                        continue
    if test_string == '()' or test_string == '':
        print('YES')
    else:
        print('NO')


bracket_check("())(()")
