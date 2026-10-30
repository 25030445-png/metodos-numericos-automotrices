"""Ejecutar y comprobar 18 ejercicios; guardar resultados en CSV."""
import csv
import argparse
from casos import CASOS
from solucionadores import METODOS

def probar(detalle=False, destino="resultados.csv"):
    registros=[]
    for c in CASOS:
        r=METODOS[c["metodo"]](c["A"],c["b"])
        aprobado=r["estado"]==c["esperado"]
        if aprobado and c["esperado"]=="resuelto":
            aprobado=(r["residuo"]<1e-6 and
                       max(abs(u-v) for u,v in zip(r["solucion"],c["referencia"]))<1e-5)
        registros.append(dict(id=c["id"],metodo=c["metodo"],ejercicio=c["titulo"],
                              esperado=c["esperado"],obtenido=r["estado"],
                              residuo=r["residuo"] if r["residuo"] is not None else "N/A",
                              resultado="APROBADA" if aprobado else "REVISAR"))
        if detalle: print(c["id"],c["titulo"],r["estado"],r["solucion"],registros[-1]["resultado"])
    with open(destino,"w",newline="",encoding="utf-8-sig") as f:
        w=csv.DictWriter(f,fieldnames=list(registros[0]))
        w.writeheader(); w.writerows(registros)
    aprobadas=sum(r["resultado"]=="APROBADA" for r in registros)
    print(f"Resultado: {aprobadas}/{len(registros)} pruebas aprobadas")
    if aprobadas!=len(registros): raise SystemExit(1)
    return registros

if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--detalle",action="store_true")
    p.add_argument("--csv",default="resultados.csv")
    a=p.parse_args()
    probar(detalle=a.detalle,destino=a.csv)
