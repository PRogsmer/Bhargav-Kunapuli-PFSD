#The count() method returns the number of times a specified value appears in the string.
#(2110030156 - Bhargav Kunapuli)
#example 1:
import time
import requests

message = 'python is popular programming language'

print('Number of occurrence of p:', message.count('p'))

#example 2:
# define string
string = "Python is awesome, isn't it?"
substring = "is"

count = string.count(substring)

# print count
print("The count is:", count)

#example 3:
# define string
string = "Python is awesome, isn't it?"
substring = "i"

# count after first 'i' and before the last 'i'
count = string.count(substring, 8, 25)

# print count
print("The count is:", count)

#example 4:
str1 = 'John has 1 apple, Sarah has 2 apples, Mike has 5 apples.'
substr = 'apples'

# Occurences of substring 'apples' in the string
result = str1.count(substr)
print("Number of substring occurrences:", result)

# Occurences of substring 'apples' from index 0 to index 40
start, end = 0, 40
result2 = str1.count(substr, start, end)
print("Number of substring occurrences:", result2)

#example 5:
txt = requests.get('https://www.gutenberg.org/cache/epub/1513/pg1513.txt').text
print(f"Downloaded {len(txt)} bytes of text...")

start_time = time.time()
count = txt.count('Romeo')
end_time = time.time()

print(f"Time to find all occurences of 'Romeo': {end_time - start_time}s with {count} results")