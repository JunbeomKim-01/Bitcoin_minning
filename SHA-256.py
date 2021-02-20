import hashlib

string = input()
sha = hashlib.new('sha256')

sha.update(string)
print(sha.hexdigest())
