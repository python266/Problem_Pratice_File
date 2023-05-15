#FUllY MODIFY
from collections import Counter
def count_highest_occurrence():
    n = int(input("Enter the number of elements: "))  # Take user input for the number of elements
    playlist = input("Enter the elements separated by spaces: ")  # Take user input for the playlist

    split_playlist = playlist.split(' ')  # Split the input playlist into a list of elements
    playlist_counts = Counter([int(x) for x in split_playlist])  # Count the occurrences of each element

    max_occurrence = max(playlist_counts.values())  # Find the maximum occurrence in the playlist

    # Find the numbers with the highest occurrence in the playlist
    highest_occurrence_numbers = [num for num, count in playlist_counts.items() if count == max_occurrence]

    print("Numbers with the highest occurrence:", highest_occurrence_numbers)

count_highest_occurrence()


#Without modify
from collections import Counter
def counter():
    int(input("Enter the number: "))
    playlsit = input("Playlist ---> ")
    split_of_playlist = playlsit.split(' ')
    p = Counter([int(x) for x in split_of_playlist])
    print(p)
counter()
