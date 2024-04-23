"""Functions that implement sorting algorithms."""

__author__ = "730482646"

def insertion_sort(x: list[int]) -> None:
    """Basic insertion sort algorithm.
    Insert into an already sorted list."""
    track_index = 0
    while track_index < len(x) - 1:
        unsorted_track_index = track_index + 1
        element = x[unsorted_track_index]

        while unsorted_track_index > 0 and x[unsorted_track_index - 1] > element:
            temp_index = x[unsorted_track_index]
            x[unsorted_track_index] = x[unsorted_track_index -1]
            x[unsorted_track_index - 1] = temp_index
            unsorted_track_index -= 1
        
        x[unsorted_track_index] = element
        track_index += 1
    return None


def selection_sort(x: list[int]) -> None:
    """Basic selection sort algorithm. 
    Repeatedly find the minimum and swap it."""
    count = 0
    while count < len(x):
        min_elem_index = count
        count_two = count + 1
        while count_two < len(x):
            if x[count_two] < x[min_elem_index]:
                min_elem_index = count_two
            count_two += 1
        if min_elem_index != count:
            temp_int = x[min_elem_index]
            x[min_elem_index] = x[count]
            x[count] = temp_int
        count += 1
    return None
    