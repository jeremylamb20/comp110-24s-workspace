"""Dictionary Utils Exercise."""
__author__ = "730461078"


def invert(first: dict[str, str]) -> dict[str, str]:
    """Function that inverts keys and values in a dictionary."""
    output = {}  
    for key in first:
        value = first[key]
        if value in output:
            raise KeyError("Duplicate value found when inverting dictionary.")
        output[value] = key   
    return output


def favorite_color(color_dict: dict[str, str]) -> str:
    """Function to determine the favorite color in a dictionary."""
    most_popular: dict[str, int] = {}  
    for key in color_dict:  
        color = color_dict[key]
        if color in most_popular: 
            most_popular[color] += 1  
        else:
            most_popular[color] = 1  
    most_pop_color = ''
    max_count = 0
    for color in most_popular:
        count = most_popular[color]
        if count > max_count:
            most_pop_color = color
            max_count = count
    return most_pop_color


def count(freq_list: list[str]) -> dict[str, int]:
    """Function to count number a specific value is present."""
    counts: dict[str, int] = {}
    for item in freq_list:
        if item in counts:
            counts[item] += 1  
        else:
            counts[item] = 1  
    return counts


def alphabetizer(words: list[str]) -> dict[str, list[str]]:
    """Function that alphabetizes items."""
    alphabet: dict[str, list[str]] = {}
    for word in words: 
        first_letter = word[0].lower()  
        if first_letter in alphabet:  
            alphabet[first_letter].append(word)
        else:  
            alphabet[first_letter] = [word]
    return alphabet


def update_attendance(attendance: dict[str, list[str]], day: str, person: str) -> None:
    """Function to update attendance."""
    if day in attendance:
        attendance[day].append(person)
    else:
        attendance[day] = [person]