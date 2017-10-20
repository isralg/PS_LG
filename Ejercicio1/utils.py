def is_perfect(num):
    own_dividers = get_own_dividers(num)
    sum = 0

    for divider in own_dividers:
        sum += divider

    if sum == num:
        return True
    else:
        return False

def is_defective(num):
    own_dividers = get_own_dividers(num)
    sum = 0

    for divider in own_dividers:
        sum += divider

    if sum < num:
        return True
    else:
        return False

def is_abundant(num):
    own_dividers = get_own_dividers(num)
    sum = 0

    for divider in own_dividers:
        sum += divider

    if sum > num:
        return True
    else:
        return False

def get_own_dividers(num):
    own_dividers = []
    for x in range(1, num-1):
        if num % x == 0:
            own_dividers.append(x)

    return own_dividers
