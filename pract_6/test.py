# Practical part: dictionaries, exception handling, function with docstring

dict1 = {1: '123', 2: 'sfsdf'}
try:
    val = dict1[12]
except KeyError as e:
    print("KeyError")


def person_processing(person1, person2):
    """
    Adds balance of people.
    person1 and person2 are dicts with name (str) and balance (int).
    Returns int: sum of person1.balance and person2.balance.
    Raises ValueError if sum of balances < 0.
    """
    balance1 = person1.balance
    balance2 = person2.balance
    sum = balance1 + balance2
    if sum < 0:
        raise ValueError('sum < 0!')
    return sum
