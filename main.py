import random
import copy

# Function to create a list of all possible combinations
def create_array():
    L = []
    for a in range(8):
        for b in range(8):
            for c in range(8):
                for d in range(8):
                    Q = [a, b, c, d]
                    L.append(Q)
    return L

# Function to remove similar sublists from the list
def remove_similar_sublists(L):
    Q = []
    for sublist in L:
        Lp = [sublist[0]]
        Test = True
        for i in range(1, 4):
            if sublist[i] in Lp:
                Test = False
                break
            Lp.append(sublist[i])
        if Test == True:
            Q.append(sublist)
    return Q

# Array of colors corresponding to numbers
Colors = ["red", "yellow", "blue", "orange", "green", "white", "purple", "pink"]

# Function to convert numbers to colors
def convert_number_to_color(L):
    C = []
    for i in range(4):
        C.append(Colors[L[i]])
    return C

# Main program function
def program(duplicates, start_double, optimized_choice):
    if duplicates:
        L = create_array()
    else:
        L = remove_similar_sublists(create_array())
    FinalTest = True
    counter = 0
    while FinalTest and len(L) > 1:
        if start_double and counter == 0:
            Current = [0, 0, 1, 1]
        else:
            if optimized_choice:
                if counter == 0:
                    Current = random.choice(L)
                else:
                    Current = choice(L)
            else:
                Current = random.choice(L)
        print("There are", len(L), "possibilities left")
        print("To put ", convert_number_to_color(Current))
        b = int(input("How many colors are correct but misplaced? --> "))
        p = int(input("How many colors are correctly placed? --> "))
        if b + p > 4:
            print("ERROR: colors > 4")
            return
        if duplicates:
            L = keep_common_sublists_duplicates(L, b + p, Current)
        elif not duplicates:
            L = keep_common_sublists(L, b + p, Current)
        L = keep_sublists_positions(L, p, Current)
        counter += 1
        if len(L) <= 1:
            FinalTest = False
    if len(L) == 1:
        print("SOLUTION: ", convert_number_to_color(L[0]))
        print(counter, "attempt(s)")
        return counter
    else:
        print("ERROR empty list")
        return

# Function to choose the best guess based on remaining possibilities
def choice(L):
    M = []
    P = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [1, 0], [1, 1], [1, 2], [1, 3], [2, 0], [2, 1], [2, 2], [3, 0], [3, 1], [4, 0]]
    for list in L:
        Sum = 0
        for pair in P:
            Commons = keep_common_sublists_duplicates(L, pair[0], list)
            Positions = keep_sublists_positions(L, pair[1], list)
            Unique_union = set(tuple(x) for x in Commons + Positions)
            Sum += len(L) - len(Unique_union)
        M.append(Sum)
    i = index_max(M)
    return L[i]

# Simplified choice function
def simplified_choice(L, duplicates):
    M = []
    P = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [1, 0], [1, 1], [1, 2], [1, 3], [2, 0], [2, 1], [2, 2], [3, 0], [3, 1], [4, 0]]
    for list in L:
        Sum = 0
        for pair in P:
            if duplicates:
                Commons = counter_common_sublists_duplicates(L, pair[0], list)
            else:
                Commons = counter_common_sublists(L, pair[0], list)
            Positions = counter_sublists_positions(L, pair[1], list)
            Sum += Commons + Positions
        M.append(Sum)
    i = index_max(M)
    return L[i]

# Function to find the index of the maximum value
def index_max(M):
    max_value = M[0]
    L = []
    for i in range(len(M)):
        if M[i] > max_value:
            max_value = M[i]
    for i in range(len(M)):
        if M[i] == max_value:
            L.append(i)
    return random.choice(L)

# Function to keep sublists with common elements
def keep_common_sublists(L, c, sublist):
    new_list = []
    for list in L:
        common_elements = len(set(list) & set(sublist))
        if common_elements == c:
            new_list.append(list)
    return new_list

# Function to keep sublists with common elements including duplicates
def keep_common_sublists_duplicates(L, c, Current):
    new_list = []
    for list in L:
        common_elements = 0
        for element in set(list):
            occurrences_list = list.count(element)
            occurrences_Current = Current.count(element)
            common_elements += min(occurrences_list, occurrences_Current)
        if c == common_elements:
            new_list.append(list)
    return new_list

# Function to keep sublists with correct positions
def keep_sublists_positions(L, p, sublist):
    new_list = []
    for list in L:
        count = 0
        for i in range(4):
            if list[i] == sublist[i]:
                count += 1
        if count == p:
            new_list.append(list)
    return new_list

# Function to count sublists with common elements
def counter_common_sublists(L, c, sublist):
    counter = len(L)
    for list in L:
        common_elements = len(set(list) & set(sublist))
        if common_elements == c:
            counter -= 1
    return counter

# Function to count sublists with common elements including duplicates
def counter_common_sublists_duplicates(L, c, Current):
    counter = len(L)
    for list in L:
        common_elements = 0
        for element in set(list):
            occurrences_list = list.count(element)
            occurrences_Current = Current.count(element)
            common_elements += min(occurrences_list, occurrences_Current)
        if c == common_elements:
            counter -= 1
    return counter

# Function to count sublists with correct positions
def counter_sublists_positions(L, p, sublist):
    counter = len(L)
    for list in L:
        count = 0
        for i in range(4):
            if list[i] == sublist[i]:
                count += 1
        if count == p:
            counter -= 1
    return counter
