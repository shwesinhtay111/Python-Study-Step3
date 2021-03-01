s = set()
s.add(1)
s.add(2)
print(s)
s.clear()
print(s)
s = {1,2,3}
sc = s.copy()
print(sc)
print(s)
s.add(4)
print(s)
print(s.difference(sc))

s1 = {1,2,3}
s2 = {1,4,5}
s1.difference_update(s2)
print(s1)
print(s)
s.discard(2)
print(s)
s1.intersection(s2)
print(s1)
s1.intersection_update(s2)
print(s1)

s3 = {1,2}
s4 = {1,2,4}
s5 = {5}

# isdisjoint - return True if two sets have a null intersection
print(s3.isdisjoint(s4))
print(s3.isdisjoint(s5))

# issubset - reports whether another set contains this set
print(s3.issubset(s4))

# issuperset - report whether this set contains another set
print(s4.issuperset(s3))
print(s3.issuperset(s4))
# Return the symmetric difference of two sets as a new set.(i.e. all elements that are in exactly one of the sets.)
print(s3.symmetric_difference(s4))

# Returns the union of two sets (i.e. all elements that are in either set.)
print(s3.union(s4))

# Update a set with the union of itself and others.
print(s3.update(s4))

