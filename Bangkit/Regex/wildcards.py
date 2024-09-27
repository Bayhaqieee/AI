import re
print(re.search(r"[Pp]ython", "Python"))

print(re.search(r"[a-z]way", "The end of the highway"))
print(re.search(r"[a-z]way", "What a way to go"))
print(re.search("cloud[a-zA-Z0-9]", "cloudy"))
print(re.search("cloud[a-zA-Z0-9]", "cloud9"))

print(re.search(r"[^a-zA-Z]", "This is a sentence with spaces."))
print(re.search(r"[^a-zA-Z ]", "This is a sentence with spaces."))

print(re.search(r"cat|dog", "I like cats."))
print(re.search(r"cat|dog", "I love dogs!"))
print(re.search(r"cat|dog", "I like both dogs and cats."))

print(re.search(r"cat|dog", "I like cats."))
print(re.search(r"cat|dog", "I love dogs!"))
print(re.search(r"cat|dog", "I like both dogs and cats."))
print(re.findall(r"cat|dog", "I like both dogs and cats."))

print(re.search(r"Py.*n", "Pygmalion"))
print(re.search(r"Py.*n", "Python Programming"))
print(re.search(r"Py[a-z]*n", "Python Programming"))
print(re.search(r"Py[a-z]*n", "Pyn"))

print(re.search(r"o+l+", "goldfish"))
print(re.search(r"o+l+", "woolly"))
print(re.search(r"o+l+", "boil"))

print(re.search(r"p?each", "To each their own"))
print(re.search(r"p?each", "I like peaches"))

print(re.search(r".com", "welcome"))
print(re.search(r"\.com", "welcome"))
print(re.search(r"\.com", "mydomain.com"))

print(re.search(r"\w*", "This is an example"))
print(re.search(r"\w*", "And_this_is_another"))