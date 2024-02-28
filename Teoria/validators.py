def valida_dni(candidato):
    for i in range(1000):
        print("hago muchas cosas")
    
    if candidato[-1] in ["A","B","C"]:
        return candidato
    else:
        raise ValueError("error")