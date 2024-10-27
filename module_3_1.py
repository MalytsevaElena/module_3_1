calls = 0
def count_calls():
    global calls
    calls = calls + 1
    return calls
def string_info(string):
    tuple_ = (len(string), string.upper(), string.lower())
    count_calls()
    print(tuple_)
def is_contains(string, list_to_search):
    result = False
    count_calls()
    for name in list_to_search:
        if name.lower() == string.lower():
           result = True
    print(result)

string_info('Capybara')
string_info('Armageddon')
is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])
is_contains('cycle', ['recycling', 'cyclic'])
is_contains('Man', ['girl', 'man', 'woman'])
print(calls)






