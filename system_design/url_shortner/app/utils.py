import hashlib

def generate_hash(url):
    return hashlib.md5(url.encode()).hexdigest()[:10]
