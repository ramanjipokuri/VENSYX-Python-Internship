def stream_browsing_file(path):
    with open(path, "r", encoding="utf-8-sig") as file:
        for line in file:
            yield line.strip()
