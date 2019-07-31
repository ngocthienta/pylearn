def reformatting_str(s):
    #take only the words in string, then join them together
    #with only a single space between them
    s = s.split()
    news = " ".join(s)
    #print
    print(news.title())
s = input('Please type a random string: ')
n = 0
for e in s:
    if e != " ":
        n += 1
        break
if n == 1 :
    print('Your string is valid.')
    reformatting_str(s)
else :
    print("Your string is invalid.")
