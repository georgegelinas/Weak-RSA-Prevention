from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256

secparam = 2048

key = RSA.generate(secparam)
public_key = key.publickey()

open('key.pub','w').write(public_key.exportKey())
open('key.priv','w').write(key.exportKey)


def wienerAttack(n,e):
	return True
