# Fungsi untuk enkripsi teks
def encrypt(text, shift):
    result = ""
    # Loop untuk setiap karakter dalam teks
    for char in text:
        # Mengecek apakah karakter adalah huruf besar
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Mengecek apakah karakter adalah huruf kecil
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            # Jika karakter bukan huruf (misalnya angka atau tanda baca), tambahkan langsung
            result += char
    return result

# Fungsi untuk dekripsi teks
def decrypt(cipher_text, shift):
    result = ""
    # Loop untuk setiap karakter dalam teks terenkripsi
    for char in cipher_text:
        # Mengecek apakah karakter adalah huruf besar
        if char.isupper():
            result += chr((ord(char) - shift - 65) % 26 + 65)
        # Mengecek apakah karakter adalah huruf kecil
        elif char.islower():
            result += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            # Jika karakter bukan huruf (misalnya angka atau tanda baca), tambahkan langsung
            result += char
    return result

# Input dari pengguna
print("Caesar Cipher Program")
mode = input("Pilih mode (encrypt/decrypt): ").lower()
message = input("Masukkan pesan: ")
shift = int(input("Masukkan kunci (shift): "))

# Proses enkripsi atau dekripsi berdasarkan mode yang dipilih
if mode == 'encrypt':
    encrypted_message = encrypt(message, shift)
    print(f"Pesan terenkripsi: {encrypted_message}")
elif mode == 'decrypt':
    decrypted_message = decrypt(message, shift)
    print(f"Pesan terdekripsi: {decrypted_message}")
else:
    print("Mode yang dipilih tidak valid.")
