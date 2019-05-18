import cryptography
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa

# Gera um par de chaves pública-privada
def gera_chaves():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    public_key = private_key.public_key()
    return private_key, public_key


# Adiciona as chaves públicas e privadas à lista de eleitores
def gera_carteiras(eleitores):
    for e in eleitores:
        e['private_key'], e['public_hey'] = gera_chaves()        

    return eleitores

# Assina uma informação
def sign():
    pass

# Verifica a assinatura
def verify_sign():
    pass