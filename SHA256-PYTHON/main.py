from hash import *
from Utils.utils import *
from Utils.helper import *
from Utils.constants import *

#example used above
hash_example = sha('hello world')
print('example: ', hash_example)
#bit length: 0
hash_0 = sha('')
vector_hash_0 = 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855'
print('bit size 0: ', hash_0 == vector_hash_0)
#bit length: 24
hash_24 = sha('abc')
vector_hash_24 = 'a7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad'
print('bit size 24: ', hash_24 == vector_hash_24)
#bit length: 448
hash_448 = sha('abcdbcdecdefdefgefghfghighijhijkijkljklmklmnlmnomnopnopq')
vector_hash_448 = '248d6a61d20638b8e5c026930c3e6039a33ce45964ff2167f6ecedd419db06c1'
print('bit size 448: ', hash_448 == vector_hash_448)
#bit length: 896
hash_896 = sha('abcdefghbcdefghicdefghijdefghijkefghijklfghijklmghijklmnhijklmnoijklmnopjklmnopqklmnopqrlmnopqrsmnopqrstnopqrstu')
vector_hash_896 = 'cf5b16a778af8380036ce59e7b0492370b249b11e8f07a51afac45037afee9d1'
print('bit size 896: ', hash_896 == vector_hash_896)