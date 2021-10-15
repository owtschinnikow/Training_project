def string_equality_check(A, B):
    if len(A) != len(B):
        return False
    for i in range(len(A)):
        if A[i] != B[i]:
            return False
    return True


def search_substring(s, sub):
    for i in range(0, len(s)-len(sub)):
        if string_equality_check(s[i:i+len(sub)]):
            print(i)