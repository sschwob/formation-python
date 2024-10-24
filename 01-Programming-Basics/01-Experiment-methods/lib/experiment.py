import random # DO NOT REMOVE THIS LINE

# Warning:
# - One line of code for each method
# - Just look in the doc for the right method of the String class!

def say_hello(name):
  # TODO: return a String to say 'Hello' to the given name
  # example: say_hello('Paul') => "Hello Paul!"
  return

def uppercase_a_string(a_string):
  # TODO: return an uppercase String
  # example: uppercase_a_string("Hello World") => "HELLOW WORLD"
  return

def concatenated_strings(string_1, string_2, string_3):
  # TODO: return a concatenated string in this order : string_3, string_1, string_2.
  # example: concatenated_strings('mange', 'le chien', le lapin) => "le lapin mange le chien"
  return

def replace_str(initial_string, old_letter, new_lettre):
  # TODO: return a copy of the string with the new letter replacing the old one
  # example: replace_str("casanova", "a", "o") => "cosonovo"
  return

def get_rid_of_surrounding_whitespaces(a_string):
  # TODO: return a copy of the string with leading and trailing whitespaces removed
  # example: get_rid_of_surrounding_whitespaces("  hey yo  ") => "hey yo"
  return

def it_starts_with(a_string, a_begining):
  # TODO: return True if the string starts with the begining
  # example: it_starts_with("hello", "he") => True
  return

# Warning:
# - Now two lines of code are allowed but not all the time needed
# - Just look in the doc for the right method of the List class!

def add_an_element(a_list, an_element):
  # TODO: return a list with the new element inside
  # example: add_an_element([1, 2, 3], 4) => [1, 2, 3, 4]
  a_list.append(an_element)
  return

def join_two_lists(list_1, list_2):
  # TODO: return a list composed by two lists
  # example: join_two_lists(['a', 'b', 'c'], ['d', 'e']) => ['a', 'b', 'c', 'd', 'e']
  list_1.extend(list_2)
  return

def count_number_of(a_list, an_item):
  # TODO: return the number of occurrences of an item in the list.
  # example: count_number_of([1, 2, 3, 2, 5, 2, 3], 3) => 2
  return

def choose_a_random_number(a_list):
  # TODO: return a random item from the list
  # example: choose_a_random_number([2, 4, 8, 10]) => 4
  return
