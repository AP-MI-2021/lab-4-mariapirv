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
    :return: o lista fara numere prime
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

def main ():
    test_Eliminare_nrPrime()
    lst = []
    while True:
        print("1. Citire lista")
        print ("2. Afisarea listei dupa eliminarea numerelor prime din lista")
        optiune = input("Dati optiunea: ")
        if optiune == "1":
            lst = CitireLista()
        elif optiune == "2":
            print (Eliminare_nrPrime(lst))
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincarcati")

main()