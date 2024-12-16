import time


def is_palindrome1(w):
    return w[::-1] == w


def is_palindrome2(w):
    while len(w) > 1:
        if w[0] != w[-1]:
            return False
        w = w[1:-1]
    return True


def is_palindrome3(w):
    if len(w) < 1:
        return True
    if w[0] == w[-1]:
        return is_palindrome3(w[1:-1])
    else:
        return False


text = "Marzena pokazała Zakopane z ram".replace(" ", "").lower()


start_time = time.time()
print(is_palindrome1(text))
end_time = time.time()
print((end_time - start_time) * 1000)

start_time = time.time()
print(is_palindrome2(text))
end_time = time.time()
print((end_time - start_time) * 1000)

start_time = time.time()
print(is_palindrome3(text))
end_time = time.time()
print((end_time - start_time) * 1000)
