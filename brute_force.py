import binascii
from crypto.cipher import AES

def main():

	with open ('words.txt') as k:
		keys = k.readlines()
	with open ('Plain.txt') as msg:
		plaintext=msg.readline(21)
		plaintext=pkcs5_pad(str(plaintext)).ljust(16, b'\x80)

            for key in keys:
                key=key.strip()
                if len(key)<16:
                    key_padded=key.ljust(16,'#')
                iv=binascii.unhexlify('aabbccddeeff00998877665544332211')
                or_cipher=binascii.unhexlify('764aa26b55a4da654df6b19e4bce00f4ed05e09346fb0e762583cb7da2ac93a2')

                aes_obj = AES.new(key_padded.encode("utf8"), AES.MODE_CBC, iv)
                ciphertext = aes_obj.encrypt(plaintext)

                if (ciphertext == or_cipher):
                    print ("key", (key))

def pkcf5_pad(s, BLOCK_SIZE=16):
    return (s+ (BLOCK_SIZE - len(s) % BLOCK_SIZE) * char(BLOCK_SIZE -len(s) % BLOCK_SIZE)).encode('utf-8')
main()
