#!python
def tour1(password):
    string = str("".join( "".join(password[::-1])[::-1])[::-1])
    return [ord(c) for c in string]


def tour2(password):
    new = []
    i = 0
    while password != []:
        new.append(password[password.index(password[i])])
        new.append(password[password.index(password[i])] + password[password.index(password[ i + 1 %len(password)])])
        password.pop(password.index(password[i]))
        i += int('qkdj', base=27) - int('QKDJ', base=31) + 267500
    print(new)
    return new

def tour3(password):
    mdp =['l', 'x', 'i', 'b', 'i', 'i', 'q', 'u', 'd', 'v', 'a', 'v', 'b', 'n', 'l', 'v', 'v', 'l', 'g', 'z', 'q', 'g', 'i', 'u', 'd', 'u', 'd', 'j', 'o', 'r', 'y', 'r', 'u', 'a']
    for i in range(len(password)):
        mdp[i], mdp[len(password) - i -1 ] = chr(password[len(password) - i -1 ] + i % 4),  chr(password[i] + i % 4)
    return "".join(mdp)




# mdp = input("Mot de passe : ")

def rev_t1(data):
    out = ""
    for i in data[::-1]:
        out+=chr(i)
    return out

def rev_t2(data):
    return data[0::2]

def clean(data):
    mdp =['l', 'x', 'i', 'b', 'i', 'i', 'q', 'u', 'd', 'v', 'a', 'v', 'b', 'n', 'l', 'v', 'v', 'l', 'g', 'z', 'q', 'g', 'i', 'u', 'd', 'u', 'd', 'j', 'o', 'r', 'y', 'r', 'u', 'a']
    mdp = "".join(mdp)
    l = len(data) -1

    for i in range(l): # remove end
        if data[l] == mdp[l]:
            data = data[:-1]
            mdp = mdp[:-1]
            l-=1
        else:
            break
    return data

def rev_t3(data):
    data = clean(data)
    out = [0]*len(data)
    for i in range(len(data)):
        out[i] = ord(data[len(data) -i -1 ]) - i % 4
        out[len(data) - i -1 ] = ord(data[i]) - i % 4

    return out

def revall(data):
    return rev_t1(rev_t2(rev_t3(data)))

def t_all(data):
    return tour3(tour2(tour1(data)))

print(revall("¡P6¨sÉU1T0d¸VÊvçu©6RÈx¨4xFw5"))

flag = "P4sS1R0bUst3Qu3C4"

mdp = input("Mot de passe : ")

if tour3(tour2(tour1(mdp))) == "¡P6¨sÉU1T0d¸VÊvçu©6RÈx¨4xFw5":
    print("Bravo ! Le flag est 404CTF{" + mdp + "}")
else :
    print("Désolé, le mot-de-passe n'est pas correct")
