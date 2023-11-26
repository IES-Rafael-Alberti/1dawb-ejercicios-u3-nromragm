def domicilios_clientes(compras):
    domicilios_facturacion = {}
    
    for compra in compras:
        cliente, _, _, domicilio = compra
        
        if cliente not in domicilios_facturacion:
            domicilios_facturacion[cliente] = set()
        
        domicilios_facturacion[cliente].add(domicilio)
    
    return domicilios_facturacion

def main():
    compras = [
        ("Nuria Costa", 5, 12780.78, "Calle Las Flores 355"),
        ("Jorge Russo", 7, 699, "Mirasol 218"),
        ("Nuria Costa", 7, 532.90, "Calle Las Flores 355"),
        ("Julián Rodriguez", 12, 5715.99, "La Mancha 761"),
        ("Jorge Russo", 15, 958, "Mirasol 218")
    ]

    resultado = domicilios_clientes(compras)

    for cliente, domicilios in resultado.items():
        print(f"Cliente: {cliente}, Domicilios para factura: {', '.join(domicilios)}")

if __name__ == "__main__":
    main()
