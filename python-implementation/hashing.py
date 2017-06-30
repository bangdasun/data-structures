### Hash table: based on dictionary
"""
    Dictionaries in Python are implemented using hash tables,
    where the indexes are obtained using a hash function on key
    
    reference:
        http://www.bogotobogo.com/python/python_hash_tables_hashing_dictionary_associated_arrays.php
"""
myhashtable = {}

# insert: key - value
myhashtable['Monday'] = 626
myhashtable['Tuesday'] = 627
myhashtable['Wednesday'] = 628
myhashtable['Thursday'] = 629
myhashtable['Friday'] = 630

myhashtable.keys()
myhashtable.values()
myhashtable.items()

# delete
del myhashtable['Monday']
myhashtable.pop('Tuesday')

### Hash table: using built-in hash function
map(hash, [0, 1, 2, 3])
hash(2)
map(hash, ['0', '1', '2', '3'])
hash('2')


from hashlib import md5, sha512
md5('a').digest()
md5('a').hexdigest()
sha512('a')
sha512('a').digest()
sha512('a').digest()
