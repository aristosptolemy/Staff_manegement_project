
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import os


test_key = b'by\x86\x10\xad\xb3\xf3\xf3\xb6i\x89\x96\x13\x8f\x17\xcd\xd7S\x96\xe8\xcc\x99\xaaE\x84\x04\xebA\xb2\xd5\x14\xfd'

not_encode = ["id","就業場所"]

class Out_Put_Test(object):
    def __init__(self,data):
        self.data = data
        self.out_put(self.data)
        
    def out_put(self,data):
        print(data)




class Decrypt_Data_Conversion(object):
    def __init__(self,data):
        self.data = data
        self.decrypt_data(self.data,test_key)
    
    
    def decrypt_data(self, encrypted_list, key):
        
        decrypted_dict = {}
        for d_key,d_value in encrypted_list.items():
            if d_key in not_encode:
                decrypted_dict[d_key] = d_value
            else:
                iv, encrypted = d_value

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
                
                decrypted_dict[d_key] = plaintext.decode('utf-8')
            
            
        print(decrypted_dict)
        return decrypted_dict
    
    





class Encryption_Data_Conversion(object):
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