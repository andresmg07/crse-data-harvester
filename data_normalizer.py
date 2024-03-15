def normalize_headers(file):
    accent_removed_headers = file.columns.str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode(
        'utf-8')
    normalized_headers = [header.lower() for header in accent_removed_headers]
    file.columns = normalized_headers
