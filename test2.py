def reformatting_text(test_str):
    test_str = test_str.strip()
    count = test_str.count(" ")
    n = 0
    while count != 0 :
        count = count//2
        n = n + 1
    for i in range(n) :
        test_str = test_str.replace("  "," ")
    print(' '.join(word[0].upper() + word[1:] for word in test_str.split()))
    return;
print('Please type a random string: ')
txt = input()
print(txt)
reformatting_text(test_str = txt)
