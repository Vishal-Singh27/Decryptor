def decrytor_normal(cyphercode, key):
    tmpkey = 0
    decypheredlist = list()
    for char in cyphercode:
        if ord(char) > 96 and ord(char) < 123:
            if ord(char) + key > 122:
                tmpkey = key - (26 - (ord(char) - 96))
                decypheredlist.append(chr(96 + tmpkey))
            else:
                decypheredlist.append(chr(ord(char) + key))
                
        elif ord(char) > 64 and ord(char) < 91:
            if ord(char) + key > 90:
                tmpkey = key - (26 - (ord(char) - 64))
                decypheredlist.append(chr(64 + tmpkey))
            else:
                decypheredlist.append(chr(ord(char) + key))
                
        else:
            decypheredlist.append(char)
            
    return ''.join(decypheredlist)
    
    
def decrytor_advanced(cyphercode):
    raise NotImplementedError