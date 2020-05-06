import random

if __name__ == '__main__':
    list_a = [x for x in range(10)]
    print(list_a)
    random.shuffle(list_a)
    print(random.sample(list_a, len(list_a)))
    print(list_a)
