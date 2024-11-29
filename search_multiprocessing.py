import multiprocessing

def search_in_file(file_path, keywords, result_queue):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            result = {keyword: [] for keyword in keywords}
            for keyword in keywords:
                if keyword in content:
                    result[keyword].append(file_path)
            result_queue.put(result)
    except Exception as e:
        print(f"Error reading {file_path}: {e}")

def search_files_multiprocessing(files, keywords):
    result_queue = multiprocessing.Queue()
    processes = []

    for file in files:
        process = multiprocessing.Process(target=search_in_file, args=(file, keywords, result_queue))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    final_results = {keyword: [] for keyword in keywords}
    while not result_queue.empty():
        result = result_queue.get()
        for keyword, files in result.items():
            final_results[keyword].extend(files)

    return final_results
