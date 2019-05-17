# -*- coding: utf-8 -*-
#共现矩阵算法

import xlrd
import pandas

def readxls_col(path):
    xl = xlrd.open_workbook(path)
    sheet = xl.sheets()[0]
    data = []
    for i in range(0, sheet.ncols):
        data.append(list(sheet.col_values(i)))
    return data




def readxls(path):
    xl = xlrd.open_workbook(path)
    sheet = xl.sheets()[0]
    data = []
    for i in range(0, sheet.ncols):
        data.append(list(sheet.col_values(i)))
    return (data[0])


def wryer(path, text):
    with open(path, 'a', encoding='utf-8') as f:
        f.write(text)
    return path+' is ok!'


def buildmatrix(x, y):
    return [[0 for j in range(y)] for i in range(x)]


def dic(xlspath):
    keygroup = readxls(xlspath)
    keytxt = '/'.join(keygroup)
    keyfir = keytxt.split('/')
    keylist = list(set([key for key in keytxt.split('/') if key != '']))
    keydic = {}
    pos = 0
    for i in keylist:
        pos = pos+1
        keydic[pos] = str(i)
    return keydic


def showmatrix(matrix):
    matrixtxt = ''
    count = 0
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix)):
            matrixtxt = matrixtxt+str(matrix[i][j])+'\t'
        matrixtxt = matrixtxt[:-1]+'\n'
        count = count+1
        print('No.'+str(count)+' had been done!')
    return matrixtxt


def inimatrix(matrix, dic, length):
    matrix[0][0] = '+'
    for i in range(1, length):
        matrix[0][i] = dic[i]
    for i in range(1, length):
        matrix[i][0] = dic[i]
    # pt(matrix)
    return matrix


def countmatirx(matrix, dic, mlength, keylis):
    for i in range(1, mlength):
        for j in range(1, mlength):
            count = 0
            for k in keylis:
                ech = str(k).split('/')
                if str(matrix[0][i]) in ech and str(matrix[j][0]) in ech and str(matrix[0][i]) != str(matrix[j][0]):
                    if abs(ech.index(str(matrix[0][i]))-ech.index(str(matrix[j][0])))<2:
                        count = count+1
                else:
                    continue
            matrix[i][j] = str(count)
    return matrix
def exchange(matrix,mlength):
    for i in range(1,mlength):
        for j in range(1,mlength):
            count=0
            matrix1 = buildmatrix(mlength*10,3)
            if matrix[i][j]!=0:
                matrix1[count][0]=matrix[i][0]
                matrix1[count][1] = matrix[0][ j]
                matrix1[count][2] = matrix[i][ j]
                count += 1
    print(count)
    return matrix1


def main():
    xlspath = r'test.xlsx'
    wrypath = r'1.txt'
    keylis = (readxls(xlspath))
    keydic = dic(xlspath)
    length = len(keydic)+1
    matrix = buildmatrix(length, length)
    print('Matrix had been built successfully!')
    matrix = inimatrix(matrix, keydic, length)
    print('Col and row had been writen!')
    matrix = countmatirx(matrix, keydic, length, keylis)
    print('Matrix had been counted successfully!')
    matrixtxt = showmatrix(matrix)
    # pt(matrix)
    print(wryer(wrypath, matrixtxt))
    # print(keylis)
    data = pandas.DataFrame(matrix)  # 为了能够使这组数据成为可以让pandas处理的数据，需要通过这个数组创建DataFrame。
    data.to_csv('test.csv', index=False, header=False)



if __name__ == '__main__':
    main()
