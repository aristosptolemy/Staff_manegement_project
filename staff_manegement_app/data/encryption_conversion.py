from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import os


test_key = b'by\x86\x10\xad\xb3\xf3\xf3\xb6i\x89\x96\x13\x8f\x17\xcd\xd7S\x96\xe8\xcc\x99\xaaE\x84\x04\xebA\xb2\xd5\x14\xfd'

not_encode = ["id","就業場所"]





class Decrypt_Data_Conversion:
    def __init__(self,data):
        self.data = data
        self.decrypt_data(self.data,test_key)
    
    
    def decrypt_data(self, encrypted_list, key):
        
        self.decrypted_dict = {}
        for d_key,d_value in encrypted_list.items():
            
            if d_key in not_encode:
                
                self.decrypted_dict[d_key] = d_value
            else:
                parts = d_value.split(':')
                iv_hex, encrypted_hex = parts
                iv = bytes.fromhex(iv_hex)  # IVを16進数の文字列からバイト型に変換
                encrypted = bytes.fromhex(encrypted_hex)

                cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
                decryptor = cipher.decryptor()

                try:
                    padded_plaintext = decryptor.update(encrypted) + decryptor.finalize()
                except ValueError:
                    print("Debug: Decryption failed with key =", key.hex())  # デバッグ情報
                    raise ValueError("Decryption failed due to incorrect key or corrupted data.")

                try:
                    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
                    plaintext = unpadder.update(padded_plaintext) + unpadder.finalize()
                except ValueError:
                    raise ValueError("Invalid padding bytes. Check if the key or IV are correct.")
                
                self.decrypted_dict[d_key] = plaintext.decode('utf-8')
            
        return self.decrypted_dict
    
    def get_data(self):
        return self.decrypted_dict
    
    
    





class Encryption_Data_Conversion:
    def __init__(self,data):
        self.data = data
        #self.encrypt_elements_individually(self.data,test_key)
        self.encrypted_data = self.encrypt_elements_individually(self.data,test_key)

        
    def encrypt_data(self,data, key):
        iv = os.urandom(16)
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
        encryptor = cipher.encryptor()
        padder = padding.PKCS7(algorithms.AES.block_size).padder()
        padded_data = padder.update(data.encode()) + padder.finalize()
        encrypted = encryptor.update(padded_data) + encryptor.finalize()
        return iv, encrypted
    
    def convert_encrypted_data_to_hex(self,iv, encrypted):
        iv_hex = iv.hex()
        encrypted_hex = encrypted.hex()
        return iv_hex, encrypted_hex
    
    
    def encrypt_elements_individually(self,data_list, key):
        new_encrypt_dict = {}
        #print(data_list)
        
        for d_key,d_value in data_list.items():
            if d_key in not_encode:
                new_encrypt_dict[d_key] = d_value

            else:
                iv, encrypted_data = self.encrypt_data(str(d_value), key)
                iv_hex, encrypted_hex = self.convert_encrypted_data_to_hex(iv, encrypted_data)  # 変換
                new_encrypt_dict[d_key] = f'{iv_hex}:{encrypted_hex}'  # IVと暗号文を一つの文字列として保存
        
        return new_encrypt_dict
    
    def get_data(self):
        return self.encrypted_data