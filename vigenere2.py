#  Namana Y Tarikere - G21372717 - Computer Security - Homework 1 - Problem 1.3

# The given encrypted message
decoded = '''NnyAagx9[r!Acy4#yh}4^&$(yu%'h&,'nru0^y@Am{w*yg(Ajxu+loyAix45nk%2_&!#ek(My}y6ym'#my!#hj41l&"#ly|'m&,+nn4&_t('yl'+hm}0a&+'ak)#no$0&&u0^&*5og!.s&z'_j(A\ 4&[hv.ct{A`u'Ajru0n&z1ij49cz|Abku&yy*$gk')_jBANny;yiu0yg!5i&x+pk47hjy4qg)'l&z1l&z1ij@Agu''yv'1`ow+_t).s&)*[t41nny4yju$\\r}0a&x7]q(Myg#&ysu;yg!5i&(6_g!A`u$&yl'1g&x+po#)yh}4^y45oi|A[y4%iu)'''
print()

# Code to find the most repititive trigrams or patterns of 3 in the encrypted text along with their frequencies
count_dict = {}
for i in range (0, len(decoded)-2):
    trigram = decoded[i:i+3]
    occurance_count = decoded.count(trigram)
    if occurance_count > 1:
        if occurance_count in count_dict:
            count_dict[occurance_count].add(trigram)
        else:
            count_dict[occurance_count] = {trigram}

print('Step 1: Most repeated trigrams with their frequency of occurence')
print()
print(count_dict)

# Trigram analysis to fetch the index of each pattern of occurence
occurances = {'&z1': []}
index_dict = {}
for i in range (0, len(decoded)-2):
    if decoded[i:i+3] in occurances:
        occurances[decoded[i:i+3]].append(i)
print()
print('Step 2: Finding the Index and Difference between index of each occurences of repeated trigrams') 
print()
print(occurances)
print()

# Calculate the difference in index in each of the pattern of occurence
# {'&z1': [169, 225, 229]}
# '&z1': [56, 60, 4]

# Find the factors of all the difference in index calculated
# Factors of 4: 1, 2, 4
# Factors of 56: 1, 2, 4, 7, 8, 14, 28, 56
# Factors of 60: 1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60

# Possible Key Length: Most repeated factors 2 and 4 
# Highest and most repeating key length = 4

# Split the entire encrypted text to length of 4 for frequency analysis
print('Step 3: Split the encrypted text by length 4')
print()
cut = 4
cc = 0
words = 5 
wc = 0
final = ""
i = 0
while i < len(decoded):
    print(decoded[i], end ="")
    cc += 1
    i += 1
    if cc == cut:
        cc = 0
        print('   ', end ="")
        wc += 1
    if words == wc:
        wc = 0
        print()
print()
print()

# Split text
sep = '''NnyA   agx9   [r!A   cy4#   yh}4
^&$(   yu%'   h&,'   nru0   ^y@A
m{w*   yg(A   jxu+   loyA   ix45
nk%2   _&!#   ek(M   y}y6   ym'#
my!#   hj41   l&"#   ly|'   m&,+
nn4&   _t('   yl'+   hm}0   a&+'
ak)#   no$0   &&u0   ^&*5   og!.
s&z'   _j(A   \ 4&   [hv.   ct{A
`u'A   jru0   n&z1   ij49   cz|A
bku&   yy*$   gk')   _jBA   Nny;
yiu0   yg!5   i&x+   pk47   hjy4
qg)'   l&z1   l&z1   ij@A   gu''
yv'1   `ow+   _t).   s&)*   [t41
nny4   yju$   \\r}0   a&x7   ]q(M
yg#&   ysu;   yg!5   i&(6   _g!A
`u$&   yl'1   g&x+   po#)   yh}4
^y45   oi|A   [y4%   iu)%'''

# Frequency analysis of split text
c = 0
letters_map = {}
for s in (sep.replace('   ', '\n')).split('\n'):
    if len(s) == 1:
        s = '\ '
    for i in range(4):
        if s[i] in letters_map:
            if i in letters_map[s[i]]:
                letters_map[s[i]][i] += 1
            else:
                letters_map[s[i]][i] = 1
        else:
            letters_map[s[i]] = {}
            letters_map[s[i]][i] = 1
    c+=1

print('Step 4: Frequency analysis of split letters for respective index points')
print()
print(letters_map)
print()

print('Step 5: Observe that y is occuring 16 times at 0th index and & is occuring 17 times at 1st index making them the possible keys')
print()

# Possible keys
# 0: y
# 1: &
# 2: 4, u, !', y(
# 3: A


# Possible keys for key length 4
# y&4A
# z'5B
# {(6C
# u"0=
# v#1>
# }*8E
# |)7D

# Algorithm to decrypt the ciphertext
# For Vigenere ciphers, decryption formula: P = D(C, K) = (Ci -Ki) mod 127
def vigenere_decrypt(ciphertext, key):
    decrypted_text = ""
    key_length = len(key)

    for i, char in enumerate(ciphertext):
        key_char = key[i % key_length]
        decrypted_char = chr((ord(char) - ord(key_char)) % 127)
        decrypted_text += "" + str(decrypted_char)

    return str(decrypted_text)

key = "y&4A"  # Possible key

# z<6><20>!z<6><20>Bz<6>5!z<6><20>B
plaintext = vigenere_decrypt(decoded, key)
print('Step 6: The decrypted message for possible key', key, 'is:')
print()
print(plaintext)
print()
