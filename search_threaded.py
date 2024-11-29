import threading

def search_in_file(file_path, keywords, results):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            for keyword in keywords:
                if keyword in content:
                    results[keyword].append(file_path)
    except Exception as e:
        print(f"Error reading {file_path}: {e}")

def search_files_threaded(files, keywords):
    results = {keyword: [] for keyword in keywords}
    threads = []

    for file in files:
        thread = threading.Thread(target=search_in_file, args=(file, keywords, results))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return results
