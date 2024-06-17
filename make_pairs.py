def load_terms(filename):
    terms = []
    with open(filename, 'r') as file:
        for line in file:
            if line.strip():
                term = line.split(':')[0].strip()
                terms.append(term)
    return terms

symptoms = load_terms('symptom.txt')
diseases = load_terms('disease.txt')

pairs = [(symptom, disease) for symptom in symptoms for disease in diseases]

with open('symptom_disease_pairs.txt', 'w') as file:
    for symptom, disease in pairs:
        file.write(f"{symptom}, {disease}\n")

print("Done. Pairs of symptoms and diseases have been saved to 'symptom_disease_pairs.txt'.")
