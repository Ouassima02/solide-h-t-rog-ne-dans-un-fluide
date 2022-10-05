import numpy as np
MV1=input("entrer la valeur de la masse volumique de platine:")
MV2=input("entrer la valeur de la masse volumique de zinc:")
MV=input("entrez la valeur de la masse volumique de mercure:")
try:
    MV1=float(MV1)
    MV2=float(MV2)
    MV=float(MV)
    min=MV1-MV/MV-MV2
    print("la valeur minimal du rapport h2/h1 est:",min,"m")
except:
    print("la valeur de la masse volumique de platine et/ou la masse volumique de zinc et/ou la masse volumique de mercure que vous avez donné pas correct")
coeff=[1,-2.4,-3.62]
sol=np.roots(coeff)
print(sol[0].real)
print("la valeur maximal de h2/h1 est :",sol,"m")