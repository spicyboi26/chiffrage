def pgcd(a,b):
    '''
    Entrée: deux entiers positifs a et b
    Sortie: le Plus Grand Diviseur Commun (PGCD) de a et b
    '''
    a,b=max(a,b), min(a,b)
    r=a%b
    if r==0:
        return b
    return pgcd(b,r)

def ppcm(a,b):
    '''
    Entrée: deux entiers positifs a et b
    Sortie: le Plus Petit Commun Multiple (PPCM) de a et b
    '''
    return int(a*b/pgcd(a,b))

def coefficient_bezout(a,b):
    '''
    Entrée: deux entiers positifs a et b premiers entre eux
    Sortie: le premier coefficient Bézout
    '''
    r1, r2 = a,b
    s1, s2 = 1,0
    # t1, t2 = 0,1
    while r2!=0:
        q=r1//r2
        r1,r2 = r2, r1-q*r2
        s1,s2 = s2, s1-q*s2
        #t1,t2 = t2, t1-q*t2
    return s1 #, t1
