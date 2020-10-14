import math

def f(n):
    fact = 1

    for i in range(1, n + 1):
        fact = fact * i

    return fact


def com(n, k):
    return f(n)//(f(k)*f(n - k))


def bri(n, k, p):
    assert n >= k, "n most be bigger"
    return com(n, k)*(p**k)*((1-p)**(n-k))


def cul(n, m, p):
    total = 0
    for x in range(m, n + 1):
        total += bri(n, x, p)
    return total


def change_to_win_one(a, r):
    print("Needed computers for fake vote:", math.ceil(r / 2))
    min_control_number = math.ceil(r / 2)
    return cul(r, min_control_number, a)

def main():
    try:
        number_of_computers = int(input("Number of needed computers per vote: "))
        present_bad_computers = float(input("Present of malicious computers in the net: ")) / 100
    except ValueError:
        print("enter a number")
        return

    chose_to_take = change_to_win_one(present_bad_computers, number_of_computers)
    print(f"Present of compromise votes: {chose_to_take * 100}%")

if __name__ == '__main__':
    main()

