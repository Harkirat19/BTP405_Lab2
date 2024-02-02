def stats_decorator(func):
    def wrapper(line):
        numbers = list(map(int, line.strip().split()))
        print("Numbers read:", numbers)
        print("Count of numbers:", len(numbers))
        print("Average of numbers:", sum(numbers) / len(numbers))
        print("Maximum of numbers:", max(numbers))
        func(line)
    return wrapper

@stats_decorator
def print_stats(line):
    pass

def printStats(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            print_stats(line)

file_path = 'q4.txt'  
printStats(file_path)
