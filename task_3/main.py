from pathlib import Path
import sys



def parse_log_line(line: str) -> dict:                                      # Function for parsing lines
    try:
        log_dict = {"date": "", "time": "", "level": "", "message": ""}
        items = line.split()
        log_dict["date"] = items.pop(0)
        log_dict["time"] = items.pop(0)
        log_dict["level"] = items.pop(0)
        rest = " ".join(items)
        log_dict["message"] = rest
        return log_dict
    except IndexError:
        return "The line in file is empty"


def load_logs(file_path: str) -> list:                                      # Function for opening log file
    logs = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                logs.append(parse_log_line(line))
            return logs
    except FileNotFoundError:
        return "File was not found"


def filter_logs_by_level(logs: list, level: str) -> list:                   # Function for filtering levels
    try:
        return [log for log in logs if log['level'] == level]
    except TypeError:
        return "Wrong input data"

def count_logs_by_level(logs: list) -> dict:                                # Function for counting levels
    counts = {"INFO": 0, "DEBUG": 0, "ERROR": 0, "WARNING": 0}
    try:
        for dict in logs:
            counts[dict["level"]] += 1
        return counts
    except TypeError:
        return "Missing data"


def display_log_counts(counts: dict):                                       # Function for displaying result
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    try:
        for key, value in counts.items():
           print(f"{key:<16} | {value:<9}")
        return " "
    except AttributeError:
        return "Wrong input data"


def display_argument_info(logs: list) -> str:                               # Function for displaying information for level
    for dict in logs:
        if sys.argv[2].upper() == dict["level"]:
            print(f"{dict["date"]} {dict["time"]} - {dict["message"]}")
        

if __name__ == "__main__":                                                  # Conditions for script "If script is main file, do conditions bellow"
    file_path = Path('log_file.log')
    logs = load_logs(file_path)
    counts = count_logs_by_level(logs)
    # print(filter_logs_by_level(logs, "INFO"))
    # print(count_logs_by_level(logs))
    print(display_log_counts(counts))
    if len(sys.argv) <2:
        print("No path to file.")
        sys.exit(1)
    try:                                                                    # additional unneccessary argument for command line
        if sys.argv[2]:
            print(f"Деталі логів для рівня '{sys.argv[2].upper()}': ")
            display_argument_info(logs)
    except IndexError:
        pass
