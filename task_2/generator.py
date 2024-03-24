import re                                                       # Import of modules
from typing import Callable


text_1 = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."

def generator_numbers(text: str):                               # Crearion of generator
    match = re.search(r"\d+\.\d+", text)                        # Searching for num in text
    while match:
        yield float(match.group())                              # Returning of float number
        text = re.sub(match.group(), '', text)                  # Deleting of processed num from the text
        match = re.search(r"\d+\.\d+", text)                    # Searching for next num in text

def sum_profit(text: str, func: Callable):                      # Function for calculation of profit
    float_list = []
    for num in func(text):
        float_list.append(num)                                  # Adding to the list of every num from the text
    return sum(float_list)                                      # Returning the sum of nums from the list

total_income = sum_profit(text_1, generator_numbers)
print(f"Загальний дохід: {total_income}")

