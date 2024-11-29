import sys
import time
from tabulate import tabulate
from colorama import Fore, Style
from search_threaded import search_files_threaded
from search_multiprocessing import search_files_multiprocessing

# Функція для форматованого виводу результатів
def print_results(results, execution_time, approach):
    print("\n" + "=" * 50)
    print(Fore.CYAN + f"🔍 {approach.capitalize()} Results:" + Style.RESET_ALL)

    # Форматування результатів у таблицю
    table = []
    for keyword, files in results.items():
        table.append([keyword, ", ".join(files) if files else "Not found"])
    print(tabulate(table, headers=["Keyword", "Files"], tablefmt="grid"))

    print(Fore.GREEN + f"\n⏱️ Execution Time: {execution_time:.6f} seconds" + Style.RESET_ALL)
    print("=" * 50 + "\n")

# Основна функція
def main():
    if len(sys.argv) < 4:
        print(Fore.RED + "Usage: python main.py <approach> <files> <keywords>" + Style.RESET_ALL)
        sys.exit(1)

    approach = sys.argv[1].lower()  # threaded або multiprocessing
    files = sys.argv[2].split(',')  # файли, розділені комами
    keywords = sys.argv[3].split(',')  # ключові слова, розділені комами

    start_time = time.time()

    if approach == "threaded":
        results = search_files_threaded(files, keywords)
        end_time = time.time()
        print_results(results, end_time - start_time, "Multithreading")
    elif approach == "multiprocessing":
        results = search_files_multiprocessing(files, keywords)
        end_time = time.time()
        print_results(results, end_time - start_time, "Multiprocessing")
    else:
        print(Fore.RED + "Invalid approach. Please use 'threaded' or 'multiprocessing'." + Style.RESET_ALL)
        sys.exit(1)

if __name__ == "__main__":
    main()
