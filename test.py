import string, random


def get_clice():
    tmp = string.ascii_letters  # py3 这个函数把大小写都包括进去了
    return (''.join(random.sample(tmp, random.randint(15, 20))))


print(get_clice())
