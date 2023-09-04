#import module
from googlesearch import search

print("Welcome to Google Search Tool")

#Taking Query
query = input("What do you want to search on google? : ")

for i in search(query, start=0, stop=10):
    print(i)