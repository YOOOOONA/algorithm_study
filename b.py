import pandas as pd

# Enter your code here. Read input from STDIN. Print output to STDOUT
#find all attributes support over threshold
import os
import sys
sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline

def supportThr(attNum, thr, row, dataset):
    attList = []
    #dataset[]
    print(*dataset)
    dataset = {i:dataset[i] for i in range(len(*dataset))}
    #dataset = {*dataset
    test_df = pd.DataFrame.from_dict(*dataset, orient='index')
    print(test_df)
    return attList#attNum개수만큼만 써서 support가 thr넘기는 것들만

if __name__ == '__main__':
    #fptr = open('test.txt', 'r')
    dataset = []
    attNum = int(input())
    thr = float(input())
    row = int(input())
    for _ in range(row):
        data = input().split(',')
        dic = dict()
        for d in data:
            dic[d.split('=')[0]] = d.split('=')[1]
        dataset.append(dic)
        
    result = supportThr(attNum, thr, row, dataset)

    #fptr.close()
    


print(editDistance("abc","gzu"))