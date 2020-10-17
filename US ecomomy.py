import xlrd
import numpy as np
import matplotlib.pylab as pyl
import statsmodels.api as sm

wlabor=xlrd.open_workbook('C:\\Users\\dell\\Downloads\\CLF16OV.xls')
wgdp=xlrd.open_workbook('C:\\Users\\dell\\Downloads\\A191RL1A225NBEA.xls')
winvest=xlrd.open_workbook('C:\\Users\\dell\\Downloads\\A006RL1A225NBEA.xls')

sheet1=wlabor.sheet_by_index(0)
mv=[]
av=[]
for i in range(11,875):
    mv.append(sheet1.cell_value(i,1))

for j in range(0,72):
    b=0
    for k in range(0,12):
        b+=mv[12*j+k]
    b=b/12
    av.append(b)

rate=[]
for w in range(71):
    r=100*(av[w+1]-av[w])/av[w]
    rate.append(r)

sheet2=wgdp.sheet_by_index(0)
sheet3=winvest.sheet_by_index(0)
agdp=[]
ainvest=[]
for i in range(30,101):
    agdp.append(sheet2.cell_value(i,1))
for i in range(30,101):
    ainvest.append(sheet3.cell_value(i,1))

years=[]
for i in range(1949,2020):
    years.append(i)




pyl.plot(years,rate,'b',label=u'labor')
pyl.plot(years,agdp,'r',label=u'gdp')
pyl.plot(years,ainvest,'k',label=u'investment')
pyl.legend()
pyl.xlabel(u"years")
pyl.ylabel(u"percent")
pyl.show()



'''
y=np.array(agdp)
x1=np.array(rate)
x2=np.array(ainvest)
x=np.vstack((x1,x2))
x=x.transpose()
model=sm.OLS(y,x)
result=model.fit()
print(result.summary())
'''

gl=[agdp[i]-rate[i] for i in range(len(agdp))]
il=[ainvest[i]-rate[i] for i in range(len(agdp))]
y=np.array(gl)
x=np.array(il)
x=sm.add_constant(x)
model=sm.OLS(y,x)
result=model.fit()
print(result.summary())

y2=[1.2666+0.1814*(ainvest[i]-rate[i])+rate[i] for i in range(len(agdp))]
y2=np.array(y2)
print(np.corrcoef(y2,y))