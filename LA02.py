def main():
    zips=dict()
    zips['A']=[[1,6],[5,2]]
    zips['B']=[[2,3],[3,-6]]
    zips['C']=[[7,2],[4,-1]]
    zips['X']=[[1,1],[-1,1]]
    zips['Z']=[[0,0],[0,0]]
    I=[[1,0],[0,1]]
    '''
    Line 2~8
    zip裝著所有的測資(用字典的形式)
    I為單位矩陣
    '''
    for i in zips:
        lists=lambdas(i,zips[i])#find eigenvalue
        for j in lists:
            vector(i,zips[i],j,I)#find eigenvector

def vector(name,V,j,I):
    NI=[[j*I[x][y] for y in range(2)] for x in range(2)]
    N=[[V[p][q]-NI[p][q] for q in range(2)] for p in range(2)]
    '''
    Line 20~21:
    NI=λI
    N=A-λI
    = |  A11-λI     A12  |
      |   A21     A22-λI |
    '''
    try:
        baserate=N[1][0]/N[0][0]
    except:
        baserate=0
    '''
    Line 29~32
    先試試看baserate=N[1][0]/N[0][0]會不會出錯，若出錯則baserate=0。
    '''
    for i in range(2):
        N[1][i]=N[1][i]-(N[0][i]*baserate)#將N[1]變成[0,0]
    G=[abs(i) for i in N[0]]#生成不分正負的列表
    if type(N[0][0]) is complex or type(N[0][1]) is complex:
        if N[0][0].real>0 or (N[0][0].real==0 and N[0][0].imag>0) or (N[0][0]*N[0][1]).real>0 or ((N[0][0]*N[0][1]).real==0 and (N[0][0]*N[0][1]).imag>0):
            S=[-1*N[0][1]/min(G),N[0][0]/min(G)]#[a,b]a,b其中一個必為1
        elif N[0][1].real>0 or (N[0][1].real==0 and N[0][1].imag>0):
            S=[N[0][1]/min(G),-1*N[0][0]/min(G)]#[a,b]a,b其中一個必為1
        else:
            S=['R2-[0,0]']#例外情形:[0-0j,0-0j]
        for i in S:
            if i.imag==0:
                S[S.index(i)]=float(i.real)
        '''
        此處為複複數向量運算區(Line 40~49)
        Z=a+bj，其中a,b要個別判斷
        N=| a b |
          | 0 0 |
        ==>x=[x1,x2]=x2[-b/a,1]
        ==>x=[-b,a]
        '''
    else:
        if (N[0][0]>0 or N[0][0]*N[0][1]>0):
            S=[-1*N[0][1]/min(G),N[0][0]/min(G)]#[a,b]a,b其中一個必為1
        elif N[0][1]>0:
            S=[N[0][1]/min(G),-1*N[0][0]/min(G)]#[a,b]a,b其中一個必為1
        else:
            S='R2-[0.0, 0.0]'#例外情形:[0,0]
        '''
        N=| a b |
          | 0 0 |
        ==>x=[x1,x2]=x2[-b/a,1]
        ==>x=[-b,a]
        '''
    print(name+'矩陣在λ=',j,'的時候，特徵向量為',S)

def lambdas(name,A):
    a=1
    b=0
    c=A[0][0]*A[1][1]-A[0][1]*A[1][0]
    for i in range(len(A)):
        b-=A[i][i]
    '''
    |  A11-λI     A12  |
    |   A21     A22-λI |
    =1λ2+(-A11-A22)λ+A11*A22-A12*A21
    '''
    r=b**2-4*a*c#判別式
    lambdas1=((-1)*b+r**(0.5))/2*a
    lambdas2=((-1)*b-r**(0.5))/2*a
    if type(lambdas2)==complex:
        lambdas2=complex(str(round(lambdas2.real,10))+str(round(lambdas2.imag,10))+'j')
    if r==0:
        print(name+'矩陣的特徵值為',lambdas1)
        return [lambdas1]
    else:
        print(name+'矩陣的特徵值為',lambdas1,lambdas2)
        return [lambdas1,lambdas2]

main()