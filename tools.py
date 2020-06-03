from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, serialization

from cryptography.hazmat.primitives.asymmetric import dsa, utils
SER_ENCODING = serialization.Encoding.PEM
SER_FORMAT = serialization.PublicFormat.SubjectPublicKeyInfo
HASHING = hashes.SHA256()
OUTPUT_PATH = "./output/log.txt"

# Method responsible for both `private_key` and `public_key` generation. `key_size` was declared 1024 for basic key strength.
def gen_keys():
    private_key = dsa.generate_private_key(
        key_size=1024,
        backend=default_backend()
    )
    public_key = private_key.public_key()
    return private_key, public_key  

# Method responsible for signing a certain content with the private key according to the declared hashing_method.
def sign(private_key, digest):
    return private_key.sign(digest, utils.Prehashed(HASHING))

# Method responsible for verifying a certain received content with a public key to be able to tell if the public key generated that content via the declared hashing_method.
def verify(public_key, signature, data):
    try:
        public_key.verify(signature, data, utils.Prehashed(HASHING))
        return True
    except:
        return False

# Method responsible for hashing the stringified object.
def get_hash(obj):
    HASH_METHOD = hashes.Hash(HASHING, default_backend())
    HASH_METHOD.update(str(obj).encode('utf-8'))
    return HASH_METHOD.finalize()


def logger(*value):
    print(*value, sep="")
    with open(OUTPUT_PATH, 'a') as f:
        print(*value, file=f)


