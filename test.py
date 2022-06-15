from mb import mb
import sys
import matplotlib.pyplot as plt

_,MB_A,MB_B,MB_C,IP_SRC=[0]+[int(x) for x in sys.argv[1:-1]]+[sys.argv[-1]]


x=[1]
r=[mb(IP_SRC,1)]
for n in range(MB_A,MB_B+1,MB_C):
    r.append(mb(IP_SRC,n))
    x.append(n)
    print(f"{n} MBs => {r[-1]:.02f} s")
    
plt.plot(x,r)
plt.savefig("latencia.png")