import matplotlib.pyplot as plt
import math

x=[1,2,3,4,5]
y=[2,4,5,4,5]
#c=int(input("Enter number of observations"))
c=len(x)
'''for i in range(c):
    ist=input("Enter 'X Y'\n")
    ts=ist.split()
    x.append(float(ts[0]))
    y.append(float(ts[1]))'''
mean_x=sum(x)/len(x)
mean_y=sum(y)/len(y)

Xobmm=[]
Yobmm=[]
XobmmHSQ=[]
XYobmm=[]
YobmmHSQ=[]
for i in range(c):
    Xobmm.append(x[i]-mean_x)
    Yobmm.append(y[i]-mean_y)
    XYobmm.append(Xobmm[i]*Yobmm[i])
    XobmmHSQ.append(Xobmm[i]*Xobmm[i])
    YobmmHSQ.append(Yobmm[i]*Yobmm[i])

print("Mean X",mean_x)
print("Mean Y",mean_y)

print("X-mean_x",Xobmm)
print("Y-mean_y",Yobmm)


print("X-mean_x hsq",XobmmHSQ)
print("(X-mean_x)(Y-mean_y)",XYobmm)

slope_m=sum(XYobmm)/sum(XobmmHSQ)
y_intercept=mean_y-(slope_m*mean_x)


plt.plot(x, y,label='Observations') 
plt.xlabel('x - axis') 
plt.ylabel('y - axis') 
plt.title('X vs Y observations') 
plt.show() 

print("slope",slope_m)
print("y intercept",y_intercept)

print("Equation is Y="+str(y_intercept)+"+"+str(slope_m)+"X")

y_exp=[]
y_expobmm=[]
y_expobmmHSQ=[]
yEO=[]
for i in range(c):
    y_exp.append(float(y_intercept+(slope_m*x[i])))
    y_expobmm.append(y_exp[i]-mean_y)
    y_expobmmHSQ.append(y_expobmm[i]*y_expobmm[i])
    yEO.append(y_exp[i]-y[i])
    yEO[i]*=yEO[i]

Rsquared=sum(y_expobmmHSQ)/sum(YobmmHSQ)
tmp=sum(yEO)/(len(x)-2)
Std_error=math.sqrt(tmp)
#print("calc",sum(y_expobmmHSQ),"/",sum(YobmmHSQ))
print("R squared",Rsquared)
print("Standard error",Std_error)

plt.plot(x, y,label='Observations') 
plt.plot(x, y_exp,label='Regression line') 
plt.xlabel('x - axis') 
plt.ylabel('y - axis') 
plt.title('Linear Regression line') 
plt.show() 
    
print("------------------------------------\n")
done=False
while(done==False):
    xq=input("Enter a new float to query or enter Done/done\n")
    if xq=="Done" or xq=="done":
        done=True
        break
    else:
        xq=float(xq)
        yq=y_intercept+(slope_m*xq)
        print("Y expected is",yq)
    
    