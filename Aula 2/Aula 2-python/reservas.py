import pandas as pd

dataReservas = {
    'Nome do Hóspede': ['Hóspede 1', 'Hóspede 2', 'Hóspede 3', 'Hóspede 4', 'Hóspede 5'],
    'Data de Check-in': ['2023-08-01', '2023-08-02', '2023-08-03', '2023-08-04', '2023-08-05'],
    'Data de Check-out': ['2023-08-04', '2023-08-05', '2023-08-06', '2023-08-07', '2023-08-08'],
    'Número de Quartos Reservados': [1, 2, 1, 1, 3],
    'Tipo de Quarto': ['Standard', 'Deluxe', 'Standard', 'Suite', 'Deluxe'],
    'Valor Total da Reserva': [300, 600, 350, 800, 900]
}

df_reservas = pd.DataFrame(dataReservas)

valorTotal = df_reservas['Valor Total da Reserva'].mean()
quartosMaisReservados = df_reservas['Tipo de Quarto'].value_counts().idxmax()
mediaNoites = (pd.to_datetime(df_reservas['Data de Check-out']) - pd.to_datetime(df_reservas['Data de Check-in'])).mean().days

print(f"Média do Valor Total das Reservas: ${valorTotal:.2f}")
print(f"Tipo de Quarto Mais Reservado: {quartosMaisReservados}")
print(f"Média de Noites por Reserva: {mediaNoites:.1f} noites")

