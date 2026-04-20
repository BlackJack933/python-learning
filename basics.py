# Prova questi
nome = "Mattia"
eta = 24
altezza = 1.75
is_student = True

print(f"Ciao, mi chiamo {nome} e ho {eta} anni")
print(type(nome)) # Che tipo è ? stringa
print(type(eta)) # E questo ? intero

# Lista di tecnologie che vuoi imparare
tech_stack = ["Python", "FastAPI", "React", "PostgreSQL"]

# Dizionario con info personali

persona = {
    "nome" : "Mattia",
    "skills" : ["Python", "Excel", "Git"],
    "obiettivo" : "Backend Developer"
}

# Prova ad accedere e modificare
print(tech_stack[0]) # Python
persona["skills"].append("Testing")
print(persona)

# For loop
for tech in tech_stack:
    print(f"Sto imparando: {tech}")

# While loop
count = 0
while count < 5:
    print(f"Interazione {count}")
    count += 1
    
# Funzioni:

def calcola_ore_studio(settimane, ore_per_settimana):
    """Calcola totale ore di studio in un periodo"""
    totale = settimane * ore_per_settimana
    return totale

# Testa la funzione
ore_aprile = calcola_ore_studio(4,8)
print(f"Ore di studio previste ad Aprile: {ore_aprile}")