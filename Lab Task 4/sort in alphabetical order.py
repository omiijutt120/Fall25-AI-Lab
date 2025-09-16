def bubble_sort(t):
    a = list(t.replace(" ", ""))
    n = len(a)
    for i in range(n - 1):
        for j in range(n-1-i):
            if ord(a[j]) > ord(a[j+1]):
                a[j], a[j+1] = a[j+1], a[j]
    return "".join(a)

def bubble_words(sentence):
    words = sentence.split()
    n = len(words)
    for i in range(n - 1):
        for j in range(n-1-i):
            if words[j] > words[j+1]:
                words[j], words[j+1] = words[j+1], words[j]
    return " ".join(words)

s_c = bubble_sort("I am Raiskh")
print("Characters sorted:", s_c)

s_w = bubble_words("I am Raiskh")
print("Words sorted:",s_w)
