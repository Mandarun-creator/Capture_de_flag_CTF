
# Résolution d'un CTF - Chiffrement de Vigenère

## Qu'est-ce que le chiffrement de Vigenère ?

Le chiffrement de Vigenère est une méthode de chiffrement par substitution polyalphabétique, qui utilise une série de différentes substitutions basées sur les lettres d'un mot-clé. Il est plus sécurisé que le simple chiffrement par décalage (ou César) car il varie en fonction de la position des lettres dans le texte et du mot clé.

### Comment fonctionne-t-il ?

1. **Texte en clair** : Le texte que vous voulez chiffrer.
2. **Clé** : Un mot ou une phrase qui sert de base pour le chiffrement. La clé est répétée autant de fois que nécessaire pour correspondre à la longueur du texte en clair.
3. **Chiffrement** : Chaque lettre du texte en clair est décalée d'un certain nombre de positions dans l'alphabet en fonction de la lettre correspondante dans la clé. Le chiffrement se fait indépendamment pour les majuscules et les minuscules.

### Exemple simple :

- Texte en clair : `HELLO`
- Clé : `KEY`

La clé est répétée pour correspondre à la longueur du texte : `KEYKE`
Ensuite, chaque lettre du texte en clair est décalée par la valeur correspondante de la clé. Voici les décalages :

| Texte en clair | H | E | L | L | O |
|----------------|---|---|---|---|---|
| Clé            | K | E | Y | K | E |
| Texte chiffré  | R | I | J | V | S |

## Instructions pour ce CTF

Dans ce CTF, nous avons un texte chiffré en utilisant la méthode de Vigenère avec une clé donnée. L'objectif est de déchiffrer ce texte pour obtenir un message lisible.

### Étapes de la résolution

1. **Texte chiffré** :
   ``` 
   Gqfltwj emgj clgfv ! Aqltj rjqhjsksg ekxuaqs, ua xtwk
   n'feuguvwb gkwp xwj, ujts f'npxkqvjgw nw tjuwcz
   ugwygjtfkf qz uw efezg sqk gspwonu. Jgsfwb-aqmu f
   Pspygk nj 29 cntnn hqzt dg igtwy fw xtvjg rkkunqf.
   ```

2. **Clé utilisée** : `FCSC`

3. **Déchiffrement** :
   Le script Python fourni ci-dessous permet de déchiffrer le message chiffré. Le programme utilise une fonction qui compare chaque lettre du texte chiffré avec celle de la clé pour effectuer une opération inverse et restaurer le texte original.

### Script Python

```python
# Fonction de déchiffrement Vigenère
def vigenere_decrypt(key, ciphertext):
    minuscule = list("abcdefghijklmnopqrstuvwxyz")
    majuscule = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    decrypted_text = ""
    ciphertext_sup = ciphertext.strip()

    len_key = len(key)
    len_ciphertext = len(ciphertext_sup)

    if len_key != len_ciphertext:
        key = (key * (len_ciphertext // len_key)) + key[:len_ciphertext % len_key]

    key_count = 0
    for i in range(len(ciphertext_sup)):
        if ciphertext_sup[i].isupper():
            pos_cipher = majuscule.index(ciphertext_sup[i])
            pos_key = majuscule.index(key[key_count].upper())

            pos = (pos_cipher - pos_key) % 26
            decrypted_text += majuscule[pos]

            key_count += 1
        elif ciphertext_sup[i].islower():
            pos_cipher = minuscule.index(ciphertext_sup[i])
            pos_key = minuscule.index(key[key_count].lower())

            pos = (pos_cipher - pos_key) % 26
            decrypted_text += minuscule[pos]

            key_count += 1
        else:
            decrypted_text += ciphertext_sup[i]

    return decrypted_text


# Utilisation du script pour déchiffrer le message
messages = '''
Gqfltwj emgj clgfv ! Aqltj rjqhjsksg ekxuaqs, ua xtwk
n'feuguvwb gkwp xwj, ujts f'npxkqvjgw nw tjuwcz
ugwygjtfkf qz uw efezg sqk gspwonu. Jgsfwb-aqmu f
Pspygk nj 29 cntnn hqzt dg igtwy fw xtvjg rkkunqf.
'''

key = "FCSC"

print(vigenere_decrypt(key, messages))
```

### Explication du résultat

Une fois le script exécuté, il déchiffre le message et révèle le texte caché derrière le chiffrement de Vigenère.

## Conclusion

Ce CTF est un excellent exemple de la manière dont le chiffrement de Vigenère peut être utilisé pour masquer un message. Bien que ce chiffrement soit relativement simple, il est toujours intéressant dans le cadre de l'apprentissage de la cryptographie. Si vous souhaitez approfondir vos connaissances, essayez de chiffrer et de déchiffrer différents messages avec différentes clés !
