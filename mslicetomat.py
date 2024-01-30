import scipy
import numpy

s = "CaWO4"
m = s+".mslice"
f = open(m,"r")
a = f.readlines()
f.close()

x = [0]
y = [0]
z = [0]
e = ["0"]
dwf = [0]
xl = float(a[183][46:50])
yl = float(a[182][46:50])
zl = float(a[181][46:50])

for i in range(int((len(a)-209)/8)):
    x.append(float(a[191+8*i][41:min(49,(len(a[191+8*i])-13))]))
    y.append(float(a[190+8*i][41:min(49,(len(a[190+8*i])-13))]))
    z.append(float(a[189+8*i][41:min(49,(len(a[189+8*i])-13))]))
    dwf.append(float(a[192+8*i][46:min(54,(len(a[189+8*i])-13))]))
    if a[194+8*i][52] == '1':
        e.append('Si')
    if a[194+8*i][52] == '6' and a[194+8*i][53] != '8' and a[194+8*i][53] != '4':
        e.append('C')
    if a[194+8*i][52] == '2' and a[194+8*i][53] == '4':
        e.append('Cr')
    if a[194+8*i][52] == '3' and a[194+8*i][53] == '4':
        e.append('Se')
    if a[194+8*i][52] == '4' and a[194+8*i][53] == '4':
        e.append('Ru')
    if a[194+8*i][52] == '5' and a[194+8*i][53] == '4':
        e.append('Xe')
    if a[194+8*i][52] == '6' and a[194+8*i][53] == '4':
        e.append('Gd')
    if a[194+8*i][52] == '6' and a[194+8*i][53] == '8':
        e.append('Er')
    if a[194+8*i][52] == '2' and a[194+8*i][53] == '0':
        e.append('Ca')
    if a[194+8*i][52] == '8' and a[194+8*i][53] != '3':
        e.append('O')
    if a[194+8*i][52] == '8' and a[194+8*i][53] == '3':
        e.append('Bi')
    if a[194+8*i][52] == '7' and a[194+8*i][53] == '4':
        e.append('W')
e.remove("0")
x.remove(0)
y.remove(0)
z.remove(0)
dwf.remove(0)

estr = numpy.asarray(e, dtype='object')

scipy.io.savemat('atomlist.mat', {'e': estr, 'x': x, 'y': y, 'z': z, 'mx': xl, 'my': yl, 'mz':zl, 'dwf': dwf})

