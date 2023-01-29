
# 1- Bir listeyi düzleştiren (flatten) fonksiyon yazın. Elemanları birden çok katmanlı listelerden ([[3],2] gibi) oluşabileceği gibi, non-scalar verilerden de oluşabilir. Örnek olarak:

#input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

#output: [1,'a','cat',2,3,'dog',4,5]


def flatten(inList):
    flattened_list = []
    for item in inList:
        if type(item) == type([]):
            flattened_list.extend(flatten(item))
        else:
            flattened_list.append(item)
    return flattened_list


#2- Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın. Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürün. Örnek olarak:

#input: [[1, 2], [3, 4], [5, 6, 7]]

#output: [[[7, 6, 5], [4, 3], [2, 1]]


def rev(inList):
    C=[]
    for e in inList:
        if type(e) == type ([]):
            C.append(e[::-1])   
    return C[::-1]     
