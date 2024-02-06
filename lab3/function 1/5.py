from itertools import permutations
def print_permutations():
    user_input = input("Enter a string: ")

    for perm in permutations(user_input):           #runs over all permutations of the entered string
        print(''.join(perm))                        #joins the characters of each permutation and print it

print_permutations()
