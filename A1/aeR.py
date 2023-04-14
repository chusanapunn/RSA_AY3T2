from Crypto.Cipher import AES				# AES (all modes)

from Crypto.Util import Counter				# AES CTR
from os import urandom						# AES CBC or CTR
#from Crypto import Random					# AES CBC or CTR
#Random.get_random_bytes(16)				# AES CBC or CTR

from Crypto.Cipher import PKCS1_OAEP		# RSA
from Crypto.PublicKey import RSA			# RSA


#module 'time' has no attribute 'clock?					

def pad16(string):
	BLOCK_SIZE = 16
	PADDING = '#'

	if (len(string) % 16) > 0:
		out = string + (BLOCK_SIZE - len(string) % BLOCK_SIZE) * PADDING
		return out
	else:
		return string

	#ALTERNATIVE PADDING    out = '{s:{c}^{n}}'.format(s=string,n=BLOCK_SIZE,c='#')


def unpad16 (string):
	BLOCK_SIZE = 16
	PADDING = '#'
	out = string.strip(PADDING)
	return out




class RSA_cipher (object):
	def __init__(self, k):
		self.KEY_LENGTH = k	
		
	#	self.KEY_LENGTH = 1024	# Minimum value, better use method set_key_length()
	#def set_key_length (self, k):
	#	self.KEY_LENGTH = k

	def generate_keypair (self):
		key = RSA.generate(self.KEY_LENGTH)
		pubkey = key.publickey().exportKey("DER")
		privkey = key.exportKey("DER")
		return (pubkey,privkey)


	def encrypt (self, pub, message):
		key = RSA.importKey(pub)
		cipher = PKCS1_OAEP.new(key)
		ciphertext = cipher.encrypt(message)
		return ciphertext


	def decrypt (self, priv, ciphertext):
		key = RSA.importKey(priv)
		cipher = PKCS1_OAEP.new(key)
		message = cipher.decrypt(ciphertext)
		return message






class AES_ECB (object):														# USER FOR host_decrypt AND host_encrypt
	def __init__(self, k):
		self.KEY = pad16(k)
		self.cipher = AES.new(self.KEY, AES.MODE_ECB)

	def encrypt(self, s):
		s = pad16(s)
		return self.cipher.encrypt(s)

	def decrypt(self, s):
		t = self.cipher.decrypt(s)
		return unpad16(t)




class AES_CBC (object):
	def __init__(self, k):
		self.KEY = pad16(k)

	def encrypt(self, s):
		iv = urandom(16)
		s = pad16(s)
		enc_cipher = AES.new(self.KEY, AES.MODE_CBC, iv)
		return iv + enc_cipher.encrypt(s)

	def decrypt(self, s):
		iv = s[:16]
		dec_cipher = AES.new(self.KEY, AES.MODE_CBC, iv)
		t = dec_cipher.decrypt(s[16:])
		return unpad16(t)




class AES_CTR (object):			# KEY = 128 or 256 bit		IV = 128 bit		# BLOCK SIZE = 128 bit
	def __init__(self, k):
		self.KEY = pad16(k)													# KEY 128 or 256 bit (padded)

	def encrypt(self, s):
		iv = urandom(16)													# generate random IV (128 bit) - for every encryption
		ctr = Counter.new(128, initial_value=long(iv.encode('hex'), 16))	# init counter
		enc_cipher = AES.new(self.KEY, AES.MODE_CTR, counter=ctr)			# init cipher
		s = pad16(s)														# message padding (multiple of 128 bit)
		return iv + enc_cipher.encrypt(s)									# minimum output 32 byte: IV (128 bit) + ENC_MESSAGE (128 bit)

	def decrypt(self, s):
		iv = s[:16]															# get IV (first 128 bit)
		ctr = Counter.new(128, initial_value=long(iv.encode('hex'), 16))	# init counter
		dec_cipher = AES.new(self.KEY, AES.MODE_CTR, counter=ctr)			# init cipher
		t = dec_cipher.decrypt(s[16:])										# decrypt (IV is excluded)
		return unpad16(t)													# return unpadded message






# GOOD TEST OF RSA
####################################################################################
print ("-------------------\nRSA:\n\n")

r = RSA_cipher(4096)
pub, priv = r.generate_keypair()

#print pub
#print priv

enc = r.encrypt(pub, "test_string")
dec = r.decrypt(priv, enc)

print ("ENC: " + str(enc)	)			#.encode('hex')
print ("DEC: " + str(dec))



# GOOD TEST OF AES-ECB
####################################################################################
print ("\n\n-------------------\nAES ECB:\n\n")

KEY = "AAAAABBBBBCCCCCDDDDDEEEEEFFFFFGG"

c = AES_ECB (KEY)

enc = c.encrypt("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA  " * 2)
dec = c.decrypt(enc)

print ("ENC: " + str(enc))					#.encode('hex')
print ("DEC: " + str(dec))



# GOOD TEST OF AES-CBC
####################################################################################
print ("\n\n-------------------\nAES CBC:\n\n")

KEY = "AAAAABBBBBCCCCCDDDDDEEEEEFFFFFGG"

c = AES_CBC (KEY)

enc = c.encrypt("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA  " * 2)
dec = c.decrypt(enc)

print ("ENC: " + str(enc))					#.encode('hex')
print ("DEC: " + str(dec))



# GOOD TEST OF AES-CTR		<-- Suggested
####################################################################################
print ("\n\n-------------------\nAES CTR:\n\n")

KEY = "AAAAABBBBBCCCCCDDDDDEEEEEFFFFFGG"

c = AES_CTR (KEY)

enc = c.encrypt("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA  " * 2)
dec = c.decrypt(enc)

print ("ENC: " + str(enc))					#.encode('hex')
print ("DEC: " + str(dec))

print ("DEC2: " +  str(  c.decrypt(enc)  ))	#.encode('hex')