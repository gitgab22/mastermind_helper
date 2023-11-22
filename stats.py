import matplotlib.pyplot as plt
import time
from main import *

# Function to create a graphical distribution
def distribution_graph(n, duplicates, start_double, optimized_choice):
    if duplicates:
        L = create_array()
    else:
        L = remove_similar_sublists(create_array())
    counter = []
    Sum = 0
    start = time.time()
    Times = []
    Position_Curve = []
    for i in range(n):
        if i % 1000 == 0 and i != 0:
            print("end of calculation ", i)
            end = time.time()
            duration = end - start
            print("time taken ", duration)
            Times.append(duration)
            start = time.time()
            print("start of next calculation ")
        Solution = random.choice(L)
        count, num_positions = random_choice_program_stats(Solution, duplicates, start_double, optimized_choice)
        Sum += count
        counter.append(count)
        Position_Curve.append(num_positions)
    print("Average: ", Sum / n)
    if len(Times) != 0:
        print("Average time per ten: ", sum(Times) / len(Times))
    values, frequencies = [], []
    for value in set(counter):
        values.append(value)
        frequencies.append(counter.count(value))
    plt.subplot(1, 2, 1)
    plt.bar(values, frequencies)
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.title('Distribution for n={}'.format(n))

    plt.subplot(1, 2, 2)
    for i in range(n):
        y = Position_Curve[i]
        plt.plot([j for j in range(len(y))], y)
    plt.xlabel('Number of moves played')
    plt.ylabel('Number of possibilities')
    plt.title('Evolution of the number of possibilities for n={}'.format(n))
    plt.show()

# Function for random choice program with statistics
def random_choice_program_stats(Solution, duplicates, start_double, optimized_choice):
    if duplicates:
        L = create_array()
    else:
        L = remove_similar_sublists(create_array())
    FinalTest = True
    counter = 0
    possibilities = [len(L)]
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
        common_count = total_counter(Current, Solution)
        position_count = position_counter(Current, Solution)
        if duplicates:
            L = keep_common_sublists_duplicates(L, common_count, Current)
        elif not duplicates:
            L = keep_common_sublists(L, common_count, Current)
        L = keep_sublists_positions(L, position_count, Current)
        counter += 1
        if len(L) == 1:
            FinalTest = False
        possibilities.append(len(L))
    return counter, possibilities

# Function to count matching positions
def position_counter(Current, Solution):
    count = 0
    for i in range(4):
        if Current[i] == Solution[i]:
            count += 1
    return count

# Function to count total common elements
def total_counter(Current, Solution):
    common_elements = 0
    for element in set(Solution):
        occurrences_Solution = Solution.count(element)
        occurrences_Current = Current.count(element)
        common_elements += min(occurrences_Solution, occurrences_Current)
    return common_elements
