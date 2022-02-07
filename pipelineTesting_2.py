from ast import List
from logging import Filter


listings = [2, 8, 9, 12, 56, 34]

filterList = filter(lambda x: x * 2 != 0, listings)
print("Listings: ", list(listings))
print("Filtered list", list(filterList))

