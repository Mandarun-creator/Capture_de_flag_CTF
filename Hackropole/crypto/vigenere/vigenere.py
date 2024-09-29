# Fonction de chiffrement Vigenère
def vigenere_crypt(key, plaintext):
    # Listes des alphabets en minuscules et majuscules
    minuscule = list("abcdefghijklmnopqrstuvwxyz")
    majuscule = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    # Texte chiffré qui sera retourné
    encrypted_text = ""

    # Supprimer les espaces en début et fin de chaîne
    plaintext_sup = plaintext.strip()

    len_key = len(key)
    len_plaintext = len(plaintext_sup)

    # Ajuster la longueur de la clé pour qu'elle corresponde à la longueur du texte
    if len_key != len_plaintext:
        key = (key * (len_plaintext // len_key)) + key[:len_plaintext % len_key]

    key_count = 0  # Compteur pour suivre la position de la clé
    for i in range(len(plaintext_sup)):
        if plaintext_sup[i].isupper():  # Si le caractère est en majuscule
            pos_plain = majuscule.index(plaintext_sup[i])  # Position dans l'alphabet majuscule
            pos_key = majuscule.index(key[key_count].upper())  # Position de la lettre clé en majuscule

            pos = (pos_plain + pos_key) % 26  # Calcul du décalage selon Vigenère
            encrypted_text += majuscule[pos]  # Ajouter la lettre chiffrée

            key_count += 1
        elif plaintext_sup[i].islower():  # Si le caractère est en minuscule
            pos_plain = minuscule.index(plaintext_sup[i])  # Position dans l'alphabet minuscule
            pos_key = minuscule.index(key[key_count].lower())  # Position de la lettre clé en minuscule

            pos = (pos_plain + pos_key) % 26  # Calcul du décalage
            encrypted_text += minuscule[pos]  # Ajouter la lettre chiffrée

            key_count += 1
        else:
            encrypted_text += plaintext_sup[i]  # Si c'est un caractère spécial, on l'ajoute directement

    return encrypted_text  # Retourner le texte chiffré


# Fonction de déchiffrement Vigenère
def vigenere_decrypt(key, ciphertext):
    # Listes des alphabets en minuscules et majuscules
    minuscule = list("abcdefghijklmnopqrstuvwxyz")
    majuscule = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    # Texte déchiffré qui sera retourné
    decrypted_text = ""

    # Supprimer les espaces en début et fin de chaîne
    ciphertext_sup = ciphertext.strip()

    len_key = len(key)
    len_ciphertext = len(ciphertext_sup)

    # Ajuster la longueur de la clé pour qu'elle corresponde à la longueur du texte
    if len_key != len_ciphertext:
        key = (key * (len_ciphertext // len_key)) + key[:len_ciphertext % len_key]

    key_count = 0  # Compteur pour suivre la position de la clé
    for i in range(len(ciphertext_sup)):
        if ciphertext_sup[i].isupper():  # Si le caractère est en majuscule
            pos_cipher = majuscule.index(ciphertext_sup[i])  # Position dans l'alphabet majuscule
            pos_key = majuscule.index(key[key_count].upper())  # Position de la lettre clé en majuscule

            pos = (pos_cipher - pos_key) % 26  # Calcul du décalage inverse pour déchiffrer
            decrypted_text += majuscule[pos]  # Ajouter la lettre déchiffrée

            key_count += 1
        elif ciphertext_sup[i].islower():  # Si le caractère est en minuscule
            pos_cipher = minuscule.index(ciphertext_sup[i])  # Position dans l'alphabet minuscule
            pos_key = minuscule.index(key[key_count].lower())  # Position de la lettre clé en minuscule

            pos = (pos_cipher - pos_key) % 26  # Calcul du décalage inverse
            decrypted_text += minuscule[pos]  # Ajouter la lettre déchiffrée

            key_count += 1
        else:
            decrypted_text += ciphertext_sup[i]  # Si c'est un caractère spécial, on l'ajoute directement

    return decrypted_text  # Retourner le texte déchiffré


# Messages codés et clé pour le déchiffrement
messages = """
Gqfltwj emgj clgfv ! Aqltj rjqhjsksg ekxuaqs, ua xtwk
n'feuguvwb gkwp xwj, ujts f'npxkqvjgw nw tjuwcz
ugwygjtfkf qz uw efezg sqk gspwonu. Jgsfwb-aqmu f
Pspygk nj 29 cntnn hqzt dg igtwy fw xtvjg rkkunqf.
"""
key_decrypted = "FCSC"

# Déchiffrement du message
decrypted_message = vigenere_decrypt(key_decrypted, messages)

# Affichage du résultat
print("\n[+] Message déchiffré \n")
print(decrypted_message)
