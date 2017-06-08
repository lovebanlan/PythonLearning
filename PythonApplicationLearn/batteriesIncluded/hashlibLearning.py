import hashlib
md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())
#摘要算法不是加密算法，不能用于加密（因为无法通过摘要反推明文），只能用于防篡改，
#但是它的单项计算特性决定了可以在不存储明文口令的情况下验证用户口令。