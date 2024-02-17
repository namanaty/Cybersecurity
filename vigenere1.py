decoded = 'EUVk4NaRo/R_cR_kX\``Vkw0V_V\a`Z`o[`cRRY\]YR[UVRRL}Nt{kd\^ReV^RdkRYd\oX_\h[oNdkeUVkaVXkX\``VwoVdkRkd]VPZRdk`SoT`\dRoR_QVZZPoa`kd\faYRc[o.f`e_RYZN}k:aoVdkRkUVdaZ[TaZcVk]NcTVwoTcRjkSVcQoaYNekZ`oZ``eYjkeRc_V`e_ZN]kR[UkZ`o[`aoP]\dR]fo_VYRaVQoa`k`aYRckVeeN_aoZVZSRc`o\WkeUVkdbSSRZZYjk2[dRcV_NVy'
# count_dict = {}
# for i in range (0, len(decoded)-1):
#     trigram = decoded[i:i+2]
#     occurance_count = decoded.count(trigram)
#     if occurance_count > 2:
#         if occurance_count in count_dict:
#             count_dict[occurance_count].add(trigram)
#         else:
#             count_dict[occurance_count] = {trigram}

# print(count_dict)

# trigrm analysis
# occurances = {'UVk': [], 'dkR':[], 'Z`o':[]}
# index_dict = {}
# for i in range (0, len(decoded)-2):
#     if decoded[i:i+3] in occurances:
#         occurances[decoded[i:i+3]].append(i)

# print(occurances)

# {'UVk': [1, 78, 263], 'dkR': [61, 93, 148], 'Z`o': [29, 186, 212]}
# 'UVk': [77, 262, 185]
# 'dkR': [32, 87, 55]
# 'Z`o': [157, 183, 26]
# Factors of 77: 1, 7, 11, 77
# Factors of 262: 1, 2, 131, 262
# Factors of 185: 1, 5, 37, 185
# Factors of 32: 1, 2, 4, 8, 16, 32
# Factors of 87: 1, 3, 29, 87
# Factors of 55: 1, 5, 11, 55
# Factors of 157: 1, 157
# Factors of 183: 1, 3, 61, 183
# Factors of 26: 1, 2, 13, 26

# digrm analysis
# occurances = {'dk': [], 'Vk': [], 'Rc': [], 'UV': []}
# occurances = {'YR': [], 'kR': [], '`o': [], 'kd': [], 'Z`': []}
# index_dict = {}
# for i in range (0, len(decoded)-1):
#     if decoded[i:i+2] in occurances:
#         occurances[decoded[i:i+2]].append(i)

# for i in occurances:
#     print(i + ": "+ str([j-occurances[i][0] for j in occurances[i][1:]]))
# print(occurances)

#5 occurances
# {'dk': [61, 75, 93, 103, 148], 'Vk': [2, 20, 79, 162, 264], 'Rc': [129, 197, 241, 255, 279], 'UV': [1, 43, 78, 152, 263]}
# 'dk': [14, 32, 42, 87]
# 'Vk': [18, 77, 160, 262]
# 'Rc': [68, 112, 126, 150]
# 'UV': [42, 77, 151, 262]

# 4 occurances
# YR: [88, 189, 200]
# kR: [32, 87, 145]
# `o: [157, 183, 227]
# kd: [44, 72, 213]
# Z`: [157, 160, 183]

# cut = 4
# cc = 0
# words = 5 
# wc = 0
# final = ""
# i = 0
# while i < len(decoded):
#     print(decoded[i], end ="")
#     cc += 1
#     i += 1
#     if cc == cut:
#         cc = 0
#         print('   ', end ="")
#         wc += 1
#     if words == wc:
#         wc = 0
#         print()


sep = '''EU   Vk   4N   aR   o/   R_   cR   _k   X\   ``
Vk   w0   V_   V\   a`   Z`   o[   `c   RR   Y\
]Y   R[   UV   RR   L}   Nt   {k   d\   ^R   eV
^R   dk   RY   d\   oX   _\   h[   oN   dk   eU
Vk   aV   Xk   X\   ``   Vw   oV   dk   Rk   d]
VP   ZR   dk   `S   oT   `\   dR   oR   _Q   VZ
ZP   oa   `k   d\   fa   YR   c[   o.   f`   e_
RY   ZN   }k   :a   oV   dk   Rk   UV   da   Z[
Ta   Zc   Vk   ]N   cT   Vw   oT   cR   jk   SV
cQ   oa   YN   ek   Z`   oZ   ``   eY   jk   eR
c_   V`   e_   ZN   ]k   R[   Uk   Z`   o[   `a
oP   ]\   dR   ]f   o_   VY   Ra   VQ   oa   `k
`a   YR   ck   Ve   eN   _a   oZ   VZ   SR   c`
o\   Wk   eU   Vk   db   SS   RZ   ZY   jk   2[
dR   cV   _N   Vy'''
# c = 0
# letters_map = {}
# for s in (sep.replace('   ', '\n')).split('\n'):
#     for i in range(2):
#         if s[i] in letters_map:
#             if i in letters_map[s[i]]:
#                 letters_map[s[i]][i] += 1
#             else:
#                 letters_map[s[i]][i] = 1
#         else:
#             letters_map[s[i]] = {}
#             letters_map[s[i]][i] = 1
#     c+=1
# print(letters_map)

# 0: o
# 1: k
# 2: V
# 3: k

def vigenere_decrypt(ciphertext, key):
    decrypted_text = ''
    key_length = len(key)

    for i, char in enumerate(ciphertext):
        key_char = key[i % key_length]
        decrypted_char = chr((ord(char) - ord(key_char)) % 128)
        decrypted_text += decrypted_char

    return decrypted_text

# ciphertext = "EUVk4NaRo/R_cR_kX\``Vkw0V_V\a`Z`o[`cRRY\\]YR[UVRRL}Nt{kd\\^ReV^RdkRYd\\oX_\\h[oNdkeUVkaVXkX\\``VwoVdkRkd]VPZRdk`SoT`\\dRoR_QVZZPoa`kd\\faYRc[o.f`e_RYZN}k:aoVdkRkUVdaZ[TaZcVk]NcTVwoTcRjkSVcQoaYNekZ`oZ``eYjkeRc_V`e_ZN]kR[UkZ`o[`aoP]\\dR]fo_VYRaVQoa`k`aYRckVeeN_aoZVZSRc`o\WkeUVkdbSSRZZYjk2[dRcV_NVy"
key = "qm"  # Replace with the actual key

plaintext = vigenere_decrypt(decoded, key)
print(plaintext)