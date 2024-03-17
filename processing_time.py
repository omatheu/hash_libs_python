import pandas as pd
import hashlib
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import time

# Função para calcular o tempo de execução do algoritmo SHA-256
def sha256_time():
    start_time = time.time()
    data = b"Hello, world!"  # Dados de exemplo
    hashlib.sha256(data).hexdigest()
    end_time = time.time()
    return end_time - start_time

# Função para calcular o tempo de execução do algoritmo AES-256
def aes256_time():
    start_time = time.time()
    data = b"Hello, world!"  # Dados de exemplo
    key = b"ThisIsASecretKey"  # Chave secreta de exemplo
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())
    encryptor = cipher.encryptor()
    encryptor.update(data)
    #encryptor.finalize()
    end_time = time.time()
    return end_time - start_time

# Número de iterações para obter uma média de tempo mais precisa
num_iterations = 1000

# Executar as funções e calcular o tempo médio
sha256_avg_time = sum(sha256_time() for _ in range(num_iterations)) / num_iterations
aes256_avg_time = sum(aes256_time() for _ in range(num_iterations)) / num_iterations

# Criar o DataFrame
data = {
    "Algoritmo": ["SHA-256", "AES-256"],
    "Tempo Médio (s)": [sha256_avg_time, aes256_avg_time]
}

df = pd.DataFrame(data)

print(df)