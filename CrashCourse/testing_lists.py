# This is from exercise 3-10

programming_languages = ['java', 'c', 'c++', 'javascript', 'react', 'html', 'python', 'ada']
print("My list of programming_languages: ")
print(programming_languages)

programming_languages.append('pascal')
print("\nMy list of programming_languages after appending: ")
print(programming_languages)

programming_languages.insert(3, 'basic')
print("\nMy list of programming_languages after inserting: ")
print(programming_languages)

del programming_languages[1]
print("\nMy list of programming_languages after del call: ")
print(programming_languages)

language = programming_languages.pop()
print(f"\nMy list of programming languages after popping off {language} at the end")
print(programming_languages)
programming_languages.append(language)

language = programming_languages.pop(4)
print(f"\nMy list of programming languages after popping the 4th item: ")
print(programming_languages)

programming_languages.insert(4, language) # put it back
print(f"\nInserting it back: ")
print(programming_languages)

programming_languages.remove('html')
print(f"\nHTML isn't really a programming language, so I removed it: ")
print(programming_languages)

print("\nSorting temporarily: ")
print(sorted(programming_languages))

print("\nReverse sorting temporarily: ")
print(sorted(programming_languages, reverse=True))

programming_languages.sort()
print("\nSorting permanently: ")
print(programming_languages)

programming_languages.sort(reverse=True)
print("\nSorting permanently, reversed: ")
print(programming_languages)

programming_languages.reverse()
print("\nReversed it back: ")
print(programming_languages)

print(f"The length of programming_languages is: {len(programming_languages)}.")
