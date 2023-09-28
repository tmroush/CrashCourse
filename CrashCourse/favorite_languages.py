favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

pollers = ['erin', 'chuck', 'sarah', 'edward']

for poller in pollers:
    if poller in favorite_languages.keys():
        print(f"{poller.title()}, thank you for taking our poll!")
    else:
        print(f"{poller.title()}, you need to take our favorite languages poll.")
