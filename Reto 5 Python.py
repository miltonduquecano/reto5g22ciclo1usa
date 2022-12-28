def leer_datos():
    operacion=input()
    producto=input().split()
    producto[0] = int(producto[0])
    producto[2] = float(producto[2])
    producto[3] = int(producto[3])
    return operacion,producto
def agregar(basedatos,lineaproducto):
    if lineaproducto[0] in basedatos:
        return False
    llave=lineaproducto[0]
    lineaproducto.pop(0)
    basedatos[llave]=lineaproducto
    return True
def borrar(basedatos,lineaproducto):
    if lineaproducto[0] in basedatos:
        basedatos.pop(lineaproducto[0])
        return True
    return False
def actualizar(basedatos,lineaproducto):
    if lineaproducto[0] in basedatos:
        llave=lineaproducto[0]
        lineaproducto.pop(0)
        basedatos[llave]=lineaproducto
        return True
    return False
def promedio_precios(basedatos):
    promedio=0
    for i in basedatos:
        promedio += basedatos[i][1]
    promedio = round(promedio / len(basedatos),1)
    return promedio
def valor_inventario(basedatos):
    inventario_total=0.0
    for i in basedatos:
        inventario_total += basedatos[i][1] * basedatos[i][2]
    inventario_total = round(inventario_total,1)
    return inventario_total
def precio_mayor(basedatos):
    mayor= list(basedatos.keys())[0]
    for i in basedatos:
        if basedatos[i][1] > basedatos[mayor][1]:
            mayor=i
    return basedatos[mayor][0]
def precio_menor(basedatos):
    menor= list(basedatos.keys())[0]
    for i in basedatos:
        if basedatos[i][1] < basedatos[menor][1]:
            menor=i
    return basedatos[menor][0]
productos ={
    1:['Manzanas',5000.0,25],
    2:['Limones',2300.0,15], 
    3:['Peras',2700.0,33],
    4:['Arandanos',9300.0,5],
    5:['Tomates',2100.0,42],
    6:['Fresas',4100.0,3],
    7:['Helado',4500.0,41],
    8:['Galletas',500.0,8],
    9:['Chocolates',3500.0,80],
    10:['Jamon',15000.0,10]
}
operacion,producto = leer_datos()
if operacion=='ACTUALIZAR':
    bandera=actualizar(productos,producto)
elif operacion=='BORRAR':
    bandera=borrar(productos,producto)
elif operacion=='AGREGAR':
    bandera=agregar(productos,producto)
if bandera:
    print(f"{precio_mayor(productos)} {precio_menor(productos)} {promedio_precios(productos)} {valor_inventario(productos)}")
else:
    print('ERROR')