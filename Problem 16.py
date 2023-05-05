tag = input()
def is_valid_tag():
    # Check if tag has valid format
    if len(tag) != 9 or tag[2] not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        return False

    # Check if tag has valid digits
    for i in range(0, 8, 2):
        if (int(tag[i]) + int(tag[i+1])) % 2 != 0:
            return False

    # Check if tag has valid letter
    vowels = 'AEIOUY'
    if tag[2] in vowels:
        return False

    return True
is_valid_tag()