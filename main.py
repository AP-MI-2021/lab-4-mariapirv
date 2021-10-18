def CitireLista():
    lst = []
    listaString = input("Dati elementele listei separate prin virgula: ")
    numarString = listaString.split(",")
    for x in numarString:
        lst.append(int(x))
    return lst

def este_Prim (n):
    '''
    determina daca un numar este prim sau nu
    :param n: nr intreg
    :return: True daca nt n este prim, sau False in caz contrar
    '''
    if n < 2:
        return False
    else:
        for i in range(2, n//2+1):
            if n % i == 0:
                return False
    return True

def Eliminare_nrPrime (lst):
    '''
    elimina numerele prime din lista
    :param lst: lista de nr intregi
    :return: lista fara numere prime
    '''
    new_lst = []
    for x in lst:
        if este_Prim(x) is False:
            new_lst.append(x)
    return new_lst

def test_Eliminare_nrPrime():
    assert Eliminare_nrPrime([3,8,9,5]) == [8,9]
    assert Eliminare_nrPrime([100,4,5,78]) == [100,4,78]
    assert Eliminare_nrPrime([11,13,7]) == []

def MediaAritmetica_mai_mare_ca_nr (lst,n):
    '''
    verifica daca media aritmetica a elem din lista este mai mare decat un numar n dat
    :param lst: lista de nr intregi
    :param n: nr intreg
    :return: True daca media aritmetica este mai mare decat un numar dat, sau False in caz contrar
    '''
    suma = 0
    for x in lst:
        suma = suma + x
    media = suma // len(lst)
    if media > n:
        return True
    else:
        return False

def test_MediaAritmetica_mai_mare_ca_nr():
    assert MediaAritmetica_mai_mare_ca_nr([10, -3, 25, -1, 3, 25, 18],10) is True
    assert MediaAritmetica_mai_mare_ca_nr([1,2,3,10],20) is False

def cati_div_proprii(n):
    '''
    calculeaza numarul de divizori proprii a unui numar
    :param n: numar intreg
    :return: numarul de divizori proprii a numarului
    '''
    if n < 0:
        return 0
    else:
        catiDiv = 0
        for div in range(2,n):
            if n % div == 0:
                catiDiv = catiDiv + 1
        return catiDiv

def ListacuNumeresiDivizoriProprii (lst):
    '''
    creeaza o noua lista, adaugand dupa fiecare numar din lista initiala, numarul de divizori proprii ai sai
    :param lst: lista de nr intregi
    :return: lista noua in care fiecare numar din lista initiala este urmat de numar sau de divizori proprii
    '''
    new_lst = []
    for x in lst:
        new_lst.append(x)
        new_lst.append(cati_div_proprii(x))
    return new_lst

def test_ListacuNumeresiDivizoriProprii():
    assert ListacuNumeresiDivizoriProprii([19,5,24,12,9]) == [19,0,5,0,24,6,12,4,9,1]
    assert ListacuNumeresiDivizoriProprii([1]) == [1,0]
    assert ListacuNumeresiDivizoriProprii ([4,7,0]) == [4,1,7,0,0,0]

def main ():
    test_Eliminare_nrPrime()
    test_MediaAritmetica_mai_mare_ca_nr()
    test_ListacuNumeresiDivizoriProprii()
    lst = []
    while True:
        print("1. Citire lista")
        print ("2. Afisarea listei dupa eliminarea numerelor prime din lista")
        print ("3. Să se afișeze dacă media aritmetică a numerelor este mai mare decât un număr n dat.")
        print ("4. Afișarea listei obținută prin adăugarea după fiecare element numărul de divizori proprii ai elementului.")
        optiune = input("Dati optiunea: ")
        if optiune == "1":
            lst = CitireLista()
        elif optiune == "2":
            print (Eliminare_nrPrime(lst))
        elif optiune == "3":
            n = int(input("Dati un numar cu care se va compara media aritmetica: "))
            if MediaAritmetica_mai_mare_ca_nr(lst,n):
                print ("Da")
            else:
                print ("Nu")
        elif optiune == "4":
                print (ListacuNumeresiDivizoriProprii(lst))
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincarcati")

main()