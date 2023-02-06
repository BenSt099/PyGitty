import hashlib

def checkSha256OfFile(fileName):
    hash_sha256 = hashlib.sha256()
    with open(fileName, "rb") as f:
        for part in iter(lambda: f.read(4096), b""):
            hash_sha256.update(part)
    return hash_sha256.hexdigest()