def find_pattern_occurrences(txt):
    # Convert the text to lowercase to make the search case-insensitive
    txt = txt.lower()
    count = 0
    pattern_start = 'b'
    pattern_end = 'bob'

    # Iterate over the text to find the pattern
    index = 0
    while index < len(txt):
        start_index = txt.find(pattern_start, index)

        # If 'b' is not found, exit the loop
        if start_index == -1:
            break

        # Try to find 'Bob' starting from the position after 'b'
        end_index = txt.find(pattern_end, start_index)

        # If 'Bob' is found, count it and update the index to search for the next pattern
        if end_index != -1:
            count += 1
            index = end_index + len(pattern_end)
        else:
            # If 'Bob' is not found, move to the next character after 'b' and continue the search
            index = start_index + 1

    return count


# Example usage
text = "The boy named bBob went to the beach with his friend Bob. They built a b123Bob."
print(find_pattern_occurrences(text))
