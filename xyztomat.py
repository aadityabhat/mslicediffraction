import scipy
import numpy

f = open("CaWO4.xyz","r")
a = f.readlines()
f.close()

x = [0]
y = [0]
z = [0]
xl = 42.08
yl = 45.4
zl = 105.2
dwf = [0]
e = ["0"]
temp = []

for i in range(len(a)-2):
    temp = a[i+2].split()
    x.append(float(temp[1])/xl)
    y.append(float(temp[2])/yl)
    z.append(float(temp[3])/zl)
    e.append(str(temp[0]))
    if (temp[0] == "Ca"):
        dwf.append(0.08)
    if (temp[0] == "O"):
        dwf.append(0.08)
    if (temp[0] == "W"):
        dwf.append(0.08)
    if (temp[0] == "Bi"):
        dwf.append(0.08)

e.remove("0")
x.remove(0)
y.remove(0)
z.remove(0)
dwf.remove(0)

estr = numpy.asarray(e, dtype='object')

scipy.io.savemat('atomlistxyz.mat', {'e': estr, 'x': x, 'y': y, 'z': z, 'mx': xl, 'my': yl, 'mz':zl, 'dwf': dwf})

