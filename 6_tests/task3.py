def vote(votes):
    n_fix = 0
    counter_fix = 0
    for n in set(votes):
        if votes.count(n) > counter_fix:
            n_fix = n
            counter_fix = votes.count(n)
    return n_fix


if __name__ == '__main__':
    print(vote([1, 1, 1, 2, 3]))
    print(vote([1, 2, 3, 2, 2]))