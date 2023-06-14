import numpy as np

def calculate(List):

#   input list [0,1,2,3,4,5,6,7,8]
    if len(List) !=9:
        raise ValueError("List must contain nine numbers.")
    arr=np.array(List).reshape(3,3)
    calculations=dict()
    mean=[]
    mean.append(list(arr.mean(axis=0)))
    mean.append(list(arr.mean(axis=1)))
    mean.append((arr.mean()))
    variance=[]
    variance.append(list(arr.var(axis=0)))
    variance.append(list(arr.var(axis=1)))
    variance.append((arr.var())    )
    stndDeviation=[]
    stndDeviation.append(list((arr.var(axis=0)**0.5)))
    stndDeviation.append(list((arr.var(axis=1)**0.5)))
    stndDeviation.append(((arr.var())**0.5))
    max=[]
    max.append(list(arr.max(axis=0)))
    max.append(list(arr.max(axis=1)))
    max.append((arr.max()) )
    min=[]
    min.append(list(arr.min(axis=0)))
    min.append(list(arr.min(axis=1)))
    min.append((arr.min()) )
    sum=[]
    sum.append(list(arr.sum(axis=0)))
    sum.append(list(arr.sum(axis=1)))
    sum.append((arr.sum())         )
    calculations['mean']=mean
    calculations['variance']=variance
    calculations['standard deviation']=stndDeviation
    calculations['max']=max
    calculations['min']=min
    calculations['sum']=sum
    return calculations