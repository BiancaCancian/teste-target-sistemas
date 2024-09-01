"""
3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

IMPORTANTE:
a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;

"""

import json

def carregar_dados_json(caminho_arquivo):
    with open(caminho_arquivo, 'r') as file:
        dados = json.load(file)
    return dados['faturamento_diario']


def calcular_estatisticas(faturamento_diario):
    
    valores_validos = [item['valor'] for item in faturamento_diario if item['valor'] is not None and item['valor'] > 0]
    
    if not valores_validos:
        return None, None, 0


    menor_faturamento = min(valores_validos)
    maior_faturamento = max(valores_validos)
    

    media_mensal = sum(valores_validos) / len(valores_validos)
    dias_acima_media = sum(1 for valor in valores_validos if valor > media_mensal)

    return menor_faturamento, maior_faturamento, dias_acima_media


faturamento_diario = carregar_dados_json('faturamento.json')

menor_faturamento, maior_faturamento, dias_acima_media = calcular_estatisticas(faturamento_diario)


print(f"Menor valor de faturamento: R${menor_faturamento:.2f}")
print(f"Maior valor de faturamento: R${maior_faturamento:.2f}")
print(f"Número de dias com faturamento superior à média mensal: {dias_acima_media}")
