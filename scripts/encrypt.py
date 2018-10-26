from config.encrypt import source_dir, dest_archive, encrypt_password
from src.packages.security.crypto import encrypt_file, , decrypt_file, tardir
import hashlib


tardir(source_dir, dest_archive)
encoded = dest_archive + '.enc'
decoded = dest_archive + '.dec'
key = hashlib.sha256(encrypt_password.encode('utf8')).digest()

encrypt_file(key, dest_archive, out_filename=encoded)
decrypt_file(key, dest_archive, out_filename=decoded)

