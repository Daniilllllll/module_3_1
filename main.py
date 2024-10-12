calls = 0

def count_calls ():
    global calls
    calls += 1

def string_info(string):
    strok = str(string)
    itog = len(strok), strok.upper(), strok.lower()
    count_calls()
    return itog

def is_contains(string, list_to_search):
    string = str(string).lower()
    list_to_search = list(list_to_search)
    count_calls()
    for i in range(len(list_to_search)):
        if str(list_to_search[i]).lower() == string:
            itog = True
            break
        else:
            itog = False
            continue
    return itog

print(string_info('Govovrun'))
print(string_info('Paprika'))
print(is_contains('Golova', ['kom', 'PaPaRam', 'prIME'])) # Urban ~ urBAN
print(is_contains('krovo', ['rekrovo', 'krovo'])) # No matches
print(calls)


