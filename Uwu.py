import nbformat

# Carga los dos notebooks
with open("Notebook_Condoy Estéfano.ipynb", "r", encoding="utf-8") as f1:
    nb1 = nbformat.read(f1, as_version=4)

with open("Notebook2_Condoy Estéfano.ipynb", "r", encoding="utf-8") as f2:
    nb2 = nbformat.read(f2, as_version=4)

# Fusiona las celdas
nb1.cells.extend(nb2.cells)

# Guarda el nuevo notebook
with open("combinado.ipynb", "w", encoding="utf-8") as f_out:
    nbformat.write(nb1, f_out)