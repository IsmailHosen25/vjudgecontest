n = int(input().strip())
p = int(input().strip())

page_in_book = p//2
total_pages = n//2

from_front = page_in_book
from_back = total_pages - page_in_book
print(min(from_front,from_back))