# peak finder

# One dimensional version of peak finding
# a b c d e f g h i
# 1 2 3 4 5 6 7 8 9

# we want to find a peak 
# position is 2 is a peak if b >= a and b >= c
# position 9 is a peak if i >= h

# PROMPT:
# find a peak if it exists

# straightforward approach but we intend to build something more complicated
# worse case complexity is theta(n) - we would need to loop over n number of elements
# asymptotic complexity is linear

# You can use a divide and conquer strategy to decrease the complexity
# we can use binary search - a recursive algorithm 

# array of length n, we look at n/2 position

# if a[n/2] < a[n/2 - 1] then look left half 1..n/2 - 1 to find peak
# else if a[n/2] < a[n/2 + 1] then look at right a[n/2 + 1]..a[n]
# else n/2 is a peak




