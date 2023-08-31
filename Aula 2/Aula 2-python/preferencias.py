import json

data_preferencias = [
    {
        'Nome do Hóspede': 'Hóspede 1',
        'Preferência de Alimentação': 'Vegetariana',
        'Solicitações Especiais': 'Berço',
        'Atividades de Lazer': ['Piscina', 'Spa']
    },
    {
        'Nome do Hóspede': 'Hóspede 2',
        'Preferência de Alimentação': 'Carnívora',
        'Solicitações Especiais': '',
        'Atividades de Lazer': ['Academia', 'Passeios']
    },
    {
        'Nome do Hóspede': 'Hóspede 3',
        'Preferência de Alimentação': 'Vegana',
        'Solicitações Especiais': 'Travesseiros Extras',
        'Atividades de Lazer': ['Piscina']
    }
]

with open('preferencias.json', 'w') as file:
    json.dump(data_preferencias, file, indent=4)
with open('preferencias.json', 'r') as file:
    data = json.load(file)
preferencias_alimentacao = [item['Preferência de Alimentação'] for item in data]
solicitacoes_especiais = [item['Solicitações Especiais'] for item in data]
atividades_lazer = [item['Atividades de Lazer'] for item in data]

preferencia_alimentacao_comum = max(set(preferencias_alimentacao), key=preferencias_alimentacao.count)

solicitacoes_especiais_total = sum([len(s.split(',')) if s else 0 for s in solicitacoes_especiais])

atividades_lazer_flat = [item for sublist in atividades_lazer for item in sublist]
atividade_lazer_popular = max(set(atividades_lazer_flat), key=atividades_lazer_flat.count)

print(f"Preferência de Alimentação Mais Comum: {preferencia_alimentacao_comum}")
print(f"Total de Solicitações Especiais: {solicitacoes_especiais_total}")
print(f"Atividade de Lazer Mais Popular: {atividade_lazer_popular}")