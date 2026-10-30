"""18 ejercicios didácticos (datos sintéticos, no mediciones reales)."""
def rhs(A,x):
    return [sum(a*y for a,y in zip(f,x)) for f in A]
def bien(id,metodo,titulo,A,x,unidad):
    return dict(id=id,metodo=metodo,titulo=titulo,A=A,b=rhs(A,x),referencia=x,esperado="resuelto",unidad=unidad)
def fallo(id,metodo,titulo,A,b,estado,unidad):
    return dict(id=id,metodo=metodo,titulo=titulo,A=A,b=b,referencia=None,esperado=estado,unidad=unidad)
CASOS=[
 bien("G01","gauss","Par en tren planetario",[[4,1,-1],[2,5,1],[-1,1,6]],[80,60,40],"N m"),
 bien("G02","gauss","Ventilador del radiador",[[8,-1,1],[1,7,-2],[0,2,6]],[9,6,4],"A"),
 bien("G03","gauss","Fuerzas del sistema de dirección",[[7,1,0,-1],[1,8,-1,0],[0,-1,9,2],[1,0,2,10]],[120,80,90,60],"N"),
 bien("G04","gauss","Aceleraciones en soporte antivibratorio",[[0,3,1],[5,-1,0],[1,2,6]],[3,4,2],"m/s²"),
 fallo("G05","gauss","Caudales contradictorios",[[2,1,0],[4,2,0],[0,1,3]],[11,23,14],"inconsistente","L/min"),
 fallo("G06","gauss","Rigideces insuficientemente identificadas",[[1,-2,1],[2,-4,2],[0,1,1]],[7,14,5],"indeterminado","u.a."),
 bien("J01","jordan","Velocidades de ruedas",[[5,1,0],[1,6,-1],[0,2,7]],[12,9,6],"m/s"),
 bien("J02","jordan","Corrientes del inversor",[[3,-1,1],[2,4,0],[1,1,5]],[14,10,8],"A"),
 bien("J03","jordan","Recorridos del varillaje",[[1,2,0,1],[0,1,-1,2],[2,0,1,0],[1,-1,0,3]],[2,4,3,1],"mm"),
 bien("J04","jordan","Reacciones aerodinámicas",[[0,2,-1],[1,0,3],[2,1,1]],[40,30,20],"N"),
 fallo("J05","jordan","Calibraciones incompatibles",[[1,3,0],[2,6,0],[0,1,2]],[13,27,5],"inconsistente","V"),
 fallo("J06","jordan","Sensor con parámetros libres",[[1,0,2],[3,0,6],[0,1,-1]],[17,51,2],"indeterminado","u.a."),
 bien("C01","jacobi","Temperaturas del estator",[[13,-2,1],[-1,12,-2],[2,-1,11]],[65,62,60],"°C"),
 bien("C02","jacobi","Voltajes del módulo de carrocería",[[9,1,-1],[2,10,1],[-1,1,8]],[5,4,3],"V"),
 bien("C03","jacobi","Presiones neumáticas",[[10,-1],[1,9]],[7,5],"bar"),
 bien("C04","jacobi","Climatización de cuatro zonas",[[16,-2,0,1],[1,15,-1,0],[0,2,14,-1],[-1,0,1,13]],[23,22,21,20],"°C"),
 fallo("C05","jacobi","Diagonal nula en actuador",[[0,3],[2,8]],[3,12],"diagonal_nula","V"),
 fallo("C06","jacobi","Realimentación divergente",[[1,3],[4,1]],[7,6],"no_convergencia","u.a.")
]
