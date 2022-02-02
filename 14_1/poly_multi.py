print()
f = list(map(int, input("Enter the coefficients of 1 st polynomial starting with degree zero: ").split()))
w = list(map(int, input("Enter the coefficients of 2 nd polynomial starting with degree zero: ").split()))
m = len(f)
n = len(w)
print("\nConvolution product of ",f," and ",w ," is\n")

def convolution_product(f,w,degree):
    product=[]
    for i in range(2*degree + 1):
        sum=0
        if i<=degree:
            for j in range(i+1):
                sum=sum+(f[j]*w[degree-i+j])
            product.append(sum)
        else:
            k=0
            for j in range(i-degree,degree+1,1):
                sum=sum+(f[j]*w[k])
                k=k+1
            product.append(sum)
    for i in reversed(range(2*degree + 1)):
        if product[i]!=0 and i!=0:
            print(str(product[i]),"x^"+str(i)," + ",end =" ")
        elif product[i]!=0 and i==0:
            print(str(product[i]),"x^"+str(i))

degree=m-1
if(m!=n):
    if(m>n):
        for i in range(m-n):
            w.append(0)
    elif(m<n):
        for i in range(n-m):
            f.append(0)
        degree=n-1
w.reverse();
convolution_product(f,w,degree)