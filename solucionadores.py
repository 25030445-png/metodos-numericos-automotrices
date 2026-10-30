"""Métodos numéricos para Ax=b. Autor: Yacob Aminadab Barrientos Espinosa."""
from math import isfinite

def validar(A,b):
    n=len(A)
    if n==0 or any(len(f)!=n for f in A) or len(b)!=n:
        raise ValueError("Dimensiones incorrectas")
    a=[[float(x) for x in f] for f in A]; v=[float(x) for x in b]
    if not all(isfinite(x) for f in a for x in f) or not all(isfinite(x) for x in v):
        raise ValueError("Valores no finitos")
    return a,v

def residuo(A,b,x):
    return max(abs(sum(a*y for a,y in zip(f,x))-c) for f,c in zip(A,b))

def directo(A,b,jordan=False,eps=1e-12):
    original,rhs=validar(A,b)
    n=len(rhs); m=[f+[rhs[i]] for i,f in enumerate(original)]
    fila=0; operaciones=[]
    for col in range(n):
        piv=max(range(fila,n),key=lambda i:abs(m[i][col]))
        if abs(m[piv][col])<=eps: continue
        if piv!=fila:
            m[fila],m[piv]=m[piv],m[fila]
            operaciones.append(f"F{fila+1} ↔ F{piv+1}")
        if jordan:
            z=m[fila][col]
            m[fila]=[v/z for v in m[fila]]
            operaciones.append(f"F{fila+1} ← F{fila+1}/{z:.6g}")
            filas=[i for i in range(n) if i!=fila]
        else:
            filas=range(fila+1,n)
        for i in filas:
            factor=m[i][col]/(1 if jordan else m[fila][col])
            if abs(factor)>eps:
                m[i]=[v-factor*w for v,w in zip(m[i],m[fila])]
                operaciones.append(f"F{i+1} ← F{i+1} - ({factor:.6g})F{fila+1}")
        fila+=1
        if fila==n: break
    if any(all(abs(v)<eps for v in f[:n]) and abs(f[-1])>=eps for f in m):
        return dict(estado="inconsistente",solucion=None,operaciones=operaciones,residuo=None)
    if fila<n:
        return dict(estado="indeterminado",solucion=None,operaciones=operaciones,residuo=None)
    if jordan:
        x=[m[i][-1] for i in range(n)]
    else:
        x=[0.0]*n
        for i in range(n-1,-1,-1):
            x[i]=(m[i][-1]-sum(m[i][j]*x[j] for j in range(i+1,n)))/m[i][i]
    return dict(estado="resuelto",solucion=x,operaciones=operaciones,residuo=residuo(original,rhs,x))

def gauss_pivoteo(A,b):
    return directo(A,b,False)

def jordan_reducido(A,b):
    return directo(A,b,True)

def jacobi(A,b,x0=None,tolerancia=1e-10,max_iter=150):
    a,v=validar(A,b); n=len(v)
    if tolerancia<=0 or max_iter<1: raise ValueError("Parámetros incorrectos")
    x=[0.0]*n if x0 is None else list(map(float,x0))
    if len(x)!=n or not all(isfinite(t) for t in x): raise ValueError("x0 incorrecto")
    if any(abs(a[i][i])<=1e-12 for i in range(n)):
        return dict(estado="diagonal_nula",solucion=None,historial=[],residuo=None)
    historial=[]; escala=max(1.0,max(map(abs,v)))
    for k in range(1,max_iter+1):
        nuevo=[(v[i]-sum(a[i][j]*x[j] for j in range(n) if j!=i))/a[i][i] for i in range(n)]
        if not all(isfinite(y) for y in nuevo): break
        cambio=max(abs(y-z) for y,z in zip(nuevo,x))/max(1,max(map(abs,nuevo)))
        r=residuo(a,v,nuevo)
        historial.append(dict(iteracion=k,vector=nuevo[:],cambio=cambio,residuo=r))
        if cambio<=tolerancia and r/escala<=tolerancia:
            return dict(estado="resuelto",solucion=nuevo,historial=historial,residuo=r)
        if max(map(abs,nuevo))>1e22: break
        x=nuevo
    return dict(estado="no_convergencia",solucion=None,historial=historial,residuo=None)

METODOS={"gauss":gauss_pivoteo,"jordan":jordan_reducido,"jacobi":jacobi}
