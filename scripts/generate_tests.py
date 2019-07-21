import random
import itertools
import sys

names = ['Al', 'Bob', 'Charlie', 'Daniel', 'Ernesto', 'Frank', 'Gary', 'Helena', 'Iana', 'Jeremy', 'Kelly', 'Lewis', 'Manny', 'Nancy', 'Obama', 'Pascal', 'Quentin', 'Ralph', 'Suzie', 'Tracey', 'Ursela', 'Vivian', 'Walter', 'X', 'Yelta', 'Zip']

def generate_test_1(test, output):
    """
    simple case
    """
    k = 5
    print(k, file=test)
    test_1_names = random.sample(names, 5)
    # create scores
    scores = []
    for name in test_1_names:
        num_scores = random.randrange(k,k+6)
        scores.extend([(name, score) for score in random.sample(range(1,900), num_scores)])
    scores.extend([(test_1_names[-1], score) for score in random.sample(range(901,1000),3)])
    random.shuffle(scores)
    for a, b in scores:
        print("{} {}".format(a,b), file=test)
    print(test_1_names[-1], file=output)

def generate_test_2(test, output):
    """
    all but one are skipped
    """
    k = 7
    print(k, file=test)
    test_2_names = random.sample(names, 6)
    scores = []
    for name in test_2_names:
        num_scores = random.randrange(1,k)
        scores.extend([(name, score) for score in random.sample(range(10,900), num_scores)])
    scores.extend([(test_2_names[-1], score) for score in range(1,10)])
    random.shuffle(scores)
    for a, b in scores:
        print("{} {}".format(a,b), file=test)
    print(test_2_names[-1], file=output)

def generate_test_3(test, output):
    """
    odd-length end of input creates winner
    """
    k = 3
    print(k, file=test)
    scores=[
        ("al", 1),
        ("bob", 305),
        ("al", 2),
        ("al", 3),
        ("bob", 306),
        ("bob", 307),
        ("bob", 308),
        ("al", 997),
        ("al", 998),
        ("scoobie", 999)
    ]
    for a, b in scores:
        print("{} {}".format(a,b), file=test)
    print("al", file=output)

def generate_test_4(test, output):
    """
    odd-length end of input creates winner
    """
    k = 3
    print(k, file=test)
    scores=[
        ("carrie", 1),
        ("bob", 305),
        ("carrie", 2),
        ("carrie", 3),
        ("carrie", 4),
        ("scoobie", 999),
        ("bob", 306),
        ("carrie", 997),
        ("bob", 307),
        ("bob", 308),
        ("carrie", 998)
    ]
    for a, b in scores:
        print("{} {}".format(a,b), file=test)
    print("carrie", file=output)

def with_open_call(n, fun):
    with open("test{}.txt".format(n), "w") as t:
        with open("out_test{}.txt".format(n), "w") as o:
            fun(t,o)

if __name__=="__main__":
    with_open_call(1, generate_test_1)
    with_open_call(2, generate_test_2)
    with_open_call(3, generate_test_3)
    with_open_call(4, generate_test_4)
