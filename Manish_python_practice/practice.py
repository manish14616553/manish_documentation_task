'''a=5
b=6
c=3
# print(a>b)
# print(a<b)
# print(a==b)
# print(a!=b)


print(a>=b and b and c)
# print(a>b and b>c )
# print(a<b and a>c)

print(a>c or b>c)
print(a<c or b<c)

m=10
m+=5
m*=4
m//=2
print(m)
k=20
k=k+1
print(k)

# membership operator
a='hello my name is manish'
d='my' in a
k='rao ' in a

print(k)
print(d)

# identity operator

a=10
b=10
print(a is b)
print(a is not b)

import matplotlib.pyplot as plt

# Manish's scores
attempts = ['First Attempt', 'Second Attempt', 'Third Attempt']
scores = [3, 3.5, 5]

# Visualizing the scores using a bar chart
plt.bar(attempts, scores, color='skyblue')
plt.xlabel('Attempts')
plt.ylabel('Scores')
plt.title('Manish\'s Scores in Attempts')
plt.ylim(0, 5)  # Set the y-axis limit to better visualize the scores
plt.show()'''

'''import statistics

def calculate_mean(numbers):
    return sum(numbers) / len(numbers)

def calculate_median(numbers):
    return statistics.median(numbers)

def calculate_mode(numbers):
    return statistics.mode(numbers)

def calculate_standard_deviation(numbers):
    return statistics.stdev(numbers)

if __name__ == "__main__":
    try:
        num_list = []
        n = int(input("Enter the number of elements in the list: "))
        for i in range(n):
            num = float(input(f"Enter element {i+1}: "))
            num_list.append(num)

        mean = calculate_mean(num_list)
        median = calculate_median(num_list)
        mode = calculate_mode(num_list)
        std_dev = calculate_standard_deviation(num_list)

        print(f"Mean: {mean}")
        print(f"Median: {median}")
        print(f"Mode: {mode}")
        print(f"Standard Deviation: {std_dev}")

    except ValueError:
        print("Invalid input. Please enter valid numbers.")'''

'''import statistics
import matplotlib.pyplot as plt

def calculate_mean(numbers):
    return sum(numbers) / len(numbers)

def calculate_median(numbers):
    return statistics.median(numbers)

def calculate_mode(numbers):
    return statistics.mode(numbers)

def calculate_standard_deviation(numbers):
    return statistics.stdev(numbers)

def visualize_marks(marks):
    plt.bar(range(len(marks)), marks, tick_label=[f"Student {i+1}" for i in range(len(marks))])
    plt.xlabel('Students')
    plt.ylabel('Marks')
    plt.title('Student Marks')
    plt.show()

if __name__ == "__main__":
    try:
        num_students = int(input("Enter the number of students: "))
        marks_list = []
        for i in range(num_students):
            marks = float(input(f"Enter marks for Student {i+1}: "))
            marks_list.append(marks)

        mean = calculate_mean(marks_list)
        median = calculate_median(marks_list)
        mode = calculate_mode(marks_list)
        std_dev = calculate_standard_deviation(marks_list)

        print(f"\nMean: {mean}")
        print(f"Median: {median}")
        print(f"Mode: {mode}")
        print(f"Standard Deviation: {std_dev}")

        visualize_marks(marks_list)

    except ValueError:
        print("Invalid input. Please enter valid numbers.")'''



'''import statistics

def get_user_input():
    user_input = input("Enter a list of numbers separated by spaces: ")
    numbers = [int(num) for num in user_input.split()]
    return numbers

def calculate_mean(numbers):
    return sum(numbers) / len(numbers)

def calculate_median(numbers):
    return statistics.median(numbers)

def calculate_mode(numbers):
    return statistics.mode(numbers)

def calculate_standard_deviation(numbers):
    return statistics.stdev(numbers)

if __name__ == "__main__":
    numbers_list = get_user_input()

    mean = calculate_mean(numbers_list)
    median = calculate_median(numbers_list)
    mode = calculate_mode(numbers_list)
    standard_deviation = calculate_standard_deviation(numbers_list)

    print(f"Mean: {mean}")
    print(f"Median: {median}")
    print(f"Mode: {mode}")
    print(f"Standard Deviation: {standard_deviation}")'''


'''def get_user_input():
    user_input = input("Enter a list of numbers separated by spaces: ")
    numbers = [float(num) for num in user_input.split()]
    return numbers

def calculate_mean(numbers):
    return sum(numbers) / len(numbers)

def calculate_median(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    if n % 2 == 0:
        return (sorted_numbers[n//2 - 1] + sorted_numbers[n//2]) / 2
    else:
        return sorted_numbers[n//2]

def calculate_mode(numbers):
    counts = {}
    for num in numbers:
        counts[num] = counts.get(num, 0) + 1

    max_count = max(counts.values())
    mode = [num for num, count in counts.items() if count == max_count]
    return mode

def calculate_standard_deviation(numbers):
    mean = calculate_mean(numbers)
    squared_diff = [(num - mean) ** 2 for num in numbers]
    variance = sum(squared_diff) / len(numbers)
    return variance ** 0.5

if __name__ == "__main__":
    numbers_list = get_user_input()

    mean = calculate_mean(numbers_list)
    median = calculate_median(numbers_list)
    mode = calculate_mode(numbers_list)
    standard_deviation = calculate_standard_deviation(numbers_list)

    print(f"Mean: {mean}")
    print(f"Median: {median}")
    print(f"Mode: {mode}")
    print(f"Standard Deviation: {standard_deviation}")'''


'''import matplotlib.pyplot as plt

dates = ["26th", "Same Day", "After 10 Days"]
manish_scores = [3, 5, 5]
amit_scores = [3, 5, 5]

plt.plot(dates, manish_scores, marker='o', label='Manish')
plt.plot(dates, amit_scores, marker='o', label='Amit')

plt.xlabel('Dates')
plt.ylabel('Scores')
plt.title('Manish and Amit Scores')
plt.legend()
plt.grid(True)

plt.show()

import matplotlib.pyplot as plt

def visualize_scores():
    dates = ['26th', 'Same Day', '10th Day']
    manish_scores = [3, 5, 5]
    amit_scores = [3, 5, 5]

    bar_width = 0.35
    index = range(len(dates))

    plt.bar(index, manish_scores, bar_width, label='Manish')
    plt.bar([i + bar_width for i in index], amit_scores, bar_width, label='Amit')

    plt.xlabel('Dates')
    plt.ylabel('Scores')
    plt.title('Boat Race Task Scores')
    plt.xticks([i + bar_width / 2 for i in index], dates)
    plt.legend()

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    visualize_scores()

import statistics

def mean_median_mode_std_dev(numbers):
    mean_value = statistics.mean(numbers)
    median_value = statistics.median(numbers)
    mode_value = statistics.mode(numbers)
    std_dev_value = statistics.stdev(numbers)
    return mean_value, median_value, mode_value, std_dev_value

if __name__ == "__main__":
    try:
        # Get the input list of numbers from the user
        num_list = [float(x) for x in input("Enter a list of numbers separated by spaces: ").split()]

        mean, median, mode, std_dev = mean_median_mode_std_dev(num_list)

        # Print the calculated values
        print("Mean:", mean)
        print("Median:", median)
        print("Mode:", mode)
        print("Standard Deviation:", std_dev)

    except ValueError:
        print("Invalid input. Please enter a valid list of numbers separated by spaces.")

import statistics

def get_student_scores():
    scores = []
    for i in range(10):
        while True:
            try:
                score = float(input(f"Enter the score of student {i + 1}: "))
                if 0 <= score <= 100:
                    scores.append(score)
                    break
                else:
                    print("Score must be between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
    return scores

def calculate_mean(scores):
    return statistics.mean(scores)

def calculate_median(scores):
    return statistics.median(scores)

def calculate_mode(scores):
    return statistics.mode(scores)

def calculate_standard_deviation(scores):
    return statistics.stdev(scores)

def main():
    print("Enter the scores of 5 students:")
    student_scores = get_student_scores()

    mean = calculate_mean(student_scores)
    median = calculate_median(student_scores)
    mode = calculate_mode(student_scores)
    standard_deviation = calculate_standard_deviation(student_scores)

    print("\nResults:")
    print(f"Mean: {mean}")
    print(f"Median: {median}")
    print(f"Mode: {mode}")
    print(f"Standard Deviation: {standard_deviation}")

if __name__ == "__main__":
    main()'''

# a=int(input('enter the data'))
# i=0
# while a>i:
#     print()

import statistics

def get_intern_scores():
    scores = []
    for i in range(5):
        while True:
            try:
                score = float(input(f"Enter the score of intern {i + 1}: "))
                scores.append(score)
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
    return scores

def calculate_mean(scores):
    return statistics.mean(scores)

def calculate_median(scores):
    return statistics.median(scores)

def calculate_mode(scores):
    return statistics.mode(scores)

def calculate_standard_deviation(scores):
    return statistics.stdev(scores)

def main():
    print("Enter the scores of 5 interns:")
    intern_scores = get_intern_scores()

    mean = calculate_mean(intern_scores)
    median = calculate_median(intern_scores)
    mode = calculate_mode(intern_scores)
    standard_deviation = calculate_standard_deviation(intern_scores)

#     print("\nResults:")
    print(f"Mean: {mean}")
    print(f"Median: {median}")
    print(f"Mode: {mode}")
    print(f"Standard Deviation: {standard_deviation}")

if __name__ == "__main__":
    main()
