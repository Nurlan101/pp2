def solve(numheads, numlegs):
    c = (numlegs - 2 * numheads) / 2  # number of chicken
    r = numheads - c  #number of rabbits
    return c, r
numheads = int(input())
numlegs = int(input())
c, r = solve(numheads, numlegs)
print(c,r)
