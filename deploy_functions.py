from tabpy.tabpy_tools.client import Client

# URL de tu servidor TabPy en Render
client = Client('http://tabpy-on-render.onrender.com/')

import numpy as np

def ewma_tableau(arg1):
    # Parameters for EWMA (target conception rate and lambda)
    TARGET = 0.35  
    LAMBDA = 0.01
    
    # Variables for EWMA
    S = TARGET  # Initial value of EWMA
    ewma = np.full(len(arg1), TARGET)
    
    # Calculate EWMA trace
    for i in range(len(arg1)):
        ewma[i] = (1 - LAMBDA) * S + LAMBDA * arg1[i]
        S = ewma[i]  
    
    return ewma.tolist()

if __name__ == "__main__":
    client.staging_dir = "./tabpy_staging"  # directorio local donde hacer staging (asegúrate que existe)
    client.deploy('ewma_tableau', ewma_tableau, override=True)
    print("Función desplegada correctamente")
