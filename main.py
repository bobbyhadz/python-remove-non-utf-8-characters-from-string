# Remove the non utf-8 characters from a String in Python

my_str = '\x86bobbyhadz.com\x86'

result = my_str.encode(
    'utf-8', errors='ignore'
).decode('utf-8')

print(result)  # 👉️ 'bobbyhadz.com'