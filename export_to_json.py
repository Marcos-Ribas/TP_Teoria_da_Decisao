
import json

def export_solutions_to_json(solucoes, file_path='solucoes.json'):
    # Estrutura para armazenar os dados das soluções
    vetor_solucoes = []
    for elem in solucoes:
        for pas_utilizados, users, (num_pas, distancias_totais) in elem:
            pas_info = []
            for pa in pas_utilizados:
                pa_info = {
                    'indice': pa.indice,
                    'coordenadas': pa.coordenadas,
                    'banda_disponivel': pa.banda_disponivel,
                    'PA_ativado': pa.PA_ativado,
                    'total_distance': pa.total_distance,
                    'usuarios_atendidos': []
                }
                for user in pa.usuarios_atendidos:
                    user_info = {
                        'coordenadas': user.coordenadas,
                        'demanda': user.demandaRede,
                    }
                    pa_info['usuarios_atendidos'].append(user_info)
                pas_info.append(pa_info)
            
            vetor_solucoes.append({'num_pas': num_pas, 'distancias_totais': distancias_totais, 'pas': pas_info})

    # Salvando todas as soluções em um arquivo JSON
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(vetor_solucoes, f, ensure_ascii=False, indent=4)

def pareto_eval(solucoes):
    paretos = []
    for solucao in solucoes:
        temp = next((x for x in solucoes if (x['num_pas'] < solucao['num_pas'] and x['distancias_totais'] < solucao['distancias_totais'])), None)
        if temp == None and (solucao not in paretos):
            paretos.append(solucao)
    return paretos
        
def export_pareto_to_json(solucoes, file_path='solucoes_pareto.json'):
    # Estrutura para armazenar os dados das soluções
    vetor_solucoes = []
    for elem in solucoes:
        for pas_utilizados, users, (num_pas, distancias_totais) in elem:
            pas_info = []
            for pa in pas_utilizados:
                pa_info = {
                    'indice': pa.indice,
                    'coordenadas': pa.coordenadas,
                    'banda_disponivel': pa.banda_disponivel,
                    'PA_ativado': pa.PA_ativado,
                    'total_distance': pa.total_distance,
                    'usuarios_atendidos': []
                }
                for user in pa.usuarios_atendidos:
                    user_info = {
                        'coordenadas': user.coordenadas,
                        'demanda': user.demandaRede,
                    }
                    pa_info['usuarios_atendidos'].append(user_info)
                pas_info.append(pa_info)
            
            vetor_solucoes.append({'num_pas': num_pas, 'distancias_totais': distancias_totais, 'pas': pas_info})

    # Salvando todas as soluções em um arquivo JSON
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(pareto_eval(vetor_solucoes), f, ensure_ascii=False, indent=4)
