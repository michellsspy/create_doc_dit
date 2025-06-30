import platform
import os

sistema = platform.system()
if sistema == "Windows":
    print("Estou no Windows")
    # Pega o diretório onde está o script atual
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    print(diretorio_atual)
elif sistema == "Linux":
    print("Estou no Linux")
else:
    print(f"Estou em outro sistema: {sistema}")
