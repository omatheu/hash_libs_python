import hashlib
import time

# List of avaliable algorithms
# sha1, sha224, sha256, sha384, sha512, blake2b, blake2s, md5, sha3_224, sha3_256, sha3_384, sha3_512, shake_128, shake_256
# print(hashlib.algorithms_guaranteed)

def calculate_sha256_hash(data):
    sha256_hash = hashlib.sha256(data.encode()).hexdigest()
    return sha256_hash

list_of_tests = ["Hello, world!", "Hello, world!1", "Hello, world!2", "Hello, world!3", "Hello, world!4", "Hello, world!5", "Hello, world!6", "Hello, world!7", "Hello, world!8", "Hello, world!9"]
results = []

# Teste
# data_string = "Hello, world!"
# hash_result = calculate_sha256_hash(data_string)
# print("SHA-256 hash da string:", hash_result)

for i in list_of_tests:
    results = calculate_sha256_hash(i)
    print(results)
    
print(results)
def calculate_file_sha256_hash(file_path):
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            sha256_hash.update(chunk)
    return sha256_hash.hexdigest()

file_path = "./README.md"
file_hash = calculate_file_sha256_hash(file_path)
# print("SHA-256 hash do arquivo:", file_hash)