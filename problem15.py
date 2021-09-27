n=20

dic={}
def rec_path(i,j):
    if (1/2*(i+j)*(i+j+1)+j) in dic.keys(): return dic[1/2*(i+j)*(i+j+1)+j]
    
    if i==n and j==n: return 0
    elif i==n:return 1
    elif j==n:return 1
    else: 
        temp1=rec_path(i+1,j);
        temp2=rec_path(i,j+1); 
        dic[1/2*(i+j+1)*(i+j+2)+j]=temp1
        dic[1/2*(i+j+1)*(i+j+2)+j+1]=temp2
        return temp1+temp2
print(rec_path(0, 0))
