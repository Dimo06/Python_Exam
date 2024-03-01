def is_valid_url(url):
    # Check if the URL starts with "http://" or "https://"
    if not (url.startswith('http://') or url.startswith('https://')):
        return False

    # Check if there is a "." in the URL, indicating a domain name
    if '.' not in url:
        return False

    # Split the URL by ".", and check if there are at least two parts (domain name and TLD)
    parts = url.split('.')
    if len(parts) < 2:
        return False

    # Additional checks can be added here (e.g., checking for a path, query parameters)

    return True


# Example usage
print(is_valid_url("https://www.example.com"))  # Expected: True
print(is_valid_url("not-a-url"))  # Expected: False
