import hashlib

def generate_short_url(original_url):
    return hashlib.sha256(original_url.encode()).hexdigest()[:10]
