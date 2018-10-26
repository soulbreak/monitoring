from Crypto.Cipher import AES
import struct
import os
import tarfile


def encrypt(key, data, outfile='encrypted.enc'):
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(data.encode('utf8'))
    file_out = open(outfile, "wb")
    [ file_out.write(x) for x in (cipher.nonce, tag, ciphertext) ]

def decrypt(key, file):
    if file is None:
        raise IOError('You should provide a file')

    file_in = open(file, "rb")
    nonce, tag, ciphertext = [file_in.read(x) for x in (16, 16, -1)]

    # let's assume that the key is somehow available again
    cipher = AES.new(key, AES.MODE_EAX, nonce)
    data = cipher.decrypt_and_verify(ciphertext, tag)
    return data


def encrypt_file(key, in_filename, out_filename=None, chunksize=64*1024):
    if not out_filename:
        out_filename = in_filename + '.enc'

    iv = os.urandom(16)
    encryptor = AES.new(key, AES.MODE_CBC, iv)
    filesize = os.path.getsize(in_filename)

    with open(in_filename, 'rb') as infile:
        with open(out_filename, 'wb') as outfile:
            outfile.write(struct.pack('<Q', filesize))
            outfile.write(iv)

            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += (' ' * (16 - len(chunk) % 16)).encode('utf8')

                outfile.write(encryptor.encrypt(chunk))


def decrypt_file(key, in_filename, out_filename=None, chunksize=24*1024):
    if not out_filename:
        out_filename = os.path.splitext(in_filename)[0]

    with open(in_filename, 'rb') as infile:
        origsize = struct.unpack('<Q', infile.read(struct.calcsize('Q')))[0]
        iv = infile.read(16)
        decryptor = AES.new(key, AES.MODE_CBC, iv)

        with open(out_filename, 'wb') as outfile:
            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                outfile.write(decryptor.decrypt(chunk))

            outfile.truncate(origsize)


def tardir(source_dir, tar_name, relative_dir=True):
    tar = tarfile.open(tar_name, "w:gz")
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            arcdir = (root, os.path.relpath(root, source_dir))[relative_dir]
            print('tar.add : ', os.path.join(arcdir, file))
            tar.add(os.path.join(root, file), os.path.join(arcdir, file))
    tar.close()

