# TASK 1

def reverse_string(n):

    if len(n) == 0:
        return ""
    else:
        return reverse_string(n[1::]) + n[0]

strings = "i like cocomelon"
print(reverse_string(strings))

