# Todo list semplice in console

todos = []

def aggiungi_todo(task):
    todos.append(task)
    print(f" Aggiunto: {task}")

def mostra_todos():
    if not todos:
        print("Nessuna task!")
        return
    print("\n I tuoi  TODO:")
    for i, task in enumerate(todos, 1):
        print(f"{i}) {task}")
        
aggiungi_todo("Setup Python environment")
aggiungi_todo("Imparare variabili")
aggiungi_todo("Creare primo script")
mostra_todos()