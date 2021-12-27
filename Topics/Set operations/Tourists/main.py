# work with these variables
eugene = set(input().split())
rose = set(input().split())
country = (eugene | rose) - (eugene & rose)
print(country)
