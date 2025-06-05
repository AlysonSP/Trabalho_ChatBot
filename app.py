
from flask import Flask, render_template, request, jsonify, session
from flask_session import Session # Lembre-se: pip install Flask-Session

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem" # Cria uma pasta flask_session
Session(app)

# --- Lógica do Chatbot Adaptada ---

def menu_opcao_display():
    messages = [
        "Seja bem-vindo, eu sou o Pinbot, como posso te ajudar?",
        "1 - Abertura de chamados",
        "2 - Falar com o setor Comercial",
        "3 - Falar com um atendente",
        "0 - Sair"
    ]
    session['current_handler'] = 'tratar_opcao_handler'
    session['context'] = {} # Limpa contexto para o menu principal
    return messages

def tratar_opcao_handler(user_input):
    if user_input == "1":
        return abertura_chamado_menu_display()
    elif user_input == "2":
        return comercial_menu_display()
    elif user_input == "3":
        return atendente_menu_display()
    elif user_input == "0":
        session.clear()
        return ["Encerrando atendimento. Até logo."]
    else:
        messages = menu_opcao_display() # Mostra o menu novamente
        messages.insert(0, "Opção inválida, verifique novamente as opções do nosso menu e tente novamente.")
        return messages

# --- Funções de Abertura de Chamado ---
def abertura_chamado_menu_display():
    messages = [
        "Claro! Vamos realizar a abertura do seu chamado. Em qual das opções se encaixa sua requisição:",
        "1- Problema em um Circuito",
        "2- Liberação de Prefixo",
        "3- Manutenção Agendada",
        "0- Voltar"
    ]
    session['current_handler'] = 'tratar_abertura_chamado_handler'
    return messages

def tratar_abertura_chamado_handler(user_input):
    if user_input == "1":
        return problema_circuito_menu_display()
    elif user_input == "2":
        session['form_fields'] = ["Nome do cliente requisitante:", "IP do Prefixo que deseja anunciar:", "AS do Prefixo:", "Chamado interno do cliente requisitante:"]
        session['form_data_keys'] = ['nome_cliente', 'ip_prefixo', 'as_prefixo', 'chamado_interno']
        session['form_title'] = "Para Liberação de Prefixos preciso que você informe os seguintes dados:"
        session['form_summary_handler'] = 'liberacao_prefixo_summary'
        # Inicia coleta de dados
        session['current_handler'] = 'collect_form_data_handler'
        session['current_field_index'] = 0
        session['context'] = {}
        return [session['form_title'], session['form_fields'][0]]
    elif user_input == "3":
        session['form_fields'] = ["Nome do cliente requisitante:", "ID da atividade que vai ser realizada:", "Horario de Inicio da Manutenção:", "Horario de Finalização da Manutenção:", "Chamado interno do cliente requisitante:"]
        session['form_data_keys'] = ['nome_cliente', 'id_atividade', 'inicio_manutencao', 'fim_manutencao', 'chamado_interno']
        session['form_title'] = "Para notificar o Agendamento de uma Manutenção preciso que você informe os seguintes dados:"
        session['form_summary_handler'] = 'manutencao_agendada_summary'
        # Inicia coleta de dados
        session['current_handler'] = 'collect_form_data_handler'
        session['current_field_index'] = 0
        session['context'] = {}
        return [session['form_title'], session['form_fields'][0]]
    elif user_input == "0":
        return menu_opcao_display()
    else:
        messages = abertura_chamado_menu_display()
        messages.insert(0, "Opção inválida, tente novamente.")
        return messages

def problema_circuito_menu_display():
    messages = [
        "Qual problema o circuito está apresentando?",
        "1- Intermitência",
        "2- Perda de Pacote",
        "3- Alta Latência",
        "4- Incremento de Erros",
        "5- Indisponível / Down",
        "0- Voltar"
    ]
    session['current_handler'] = 'tratar_problema_circuito_handler'
    return messages

def tratar_problema_circuito_handler(user_input):
    form_fields_base = ["Nome do cliente requisitante:", "ID do circuito:", "Tipo do circuito:", "Chamado interno do cliente requisitante:"]
    form_data_keys_base = ['nome_cliente', 'id_circuito', 'tipo_circuito', 'chamado_interno']

    if user_input == "1": # Intermitência
        session['form_fields'] = [form_fields_base[0], form_fields_base[1], "Horário em que os flaps começaram:", form_fields_base[2], form_fields_base[3]]
        session['form_data_keys'] = [form_data_keys_base[0], form_data_keys_base[1], 'horario_flaps', form_data_keys_base[2], form_data_keys_base[3]]
        session['form_title'] = "Para Intermitências no circuito preciso que você informe os seguintes dados:"
        session['form_summary_handler'] = 'intermitencia_summary'
    elif user_input == "2": # Perda de Pacote
        session['form_fields'] = [form_fields_base[0], form_fields_base[1], "Horário em que as perdas começaram:", form_fields_base[2], form_fields_base[3]]
        session['form_data_keys'] = [form_data_keys_base[0], form_data_keys_base[1], 'horario_perdas', form_data_keys_base[2], form_data_keys_base[3]]
        session['form_title'] = "Para Perda de Pacotes no circuito preciso que você informe os seguintes dados:"
        session['form_summary_handler'] = 'perda_pacote_summary'
    elif user_input == "3": # Alta Latência
        session['form_fields'] = [form_fields_base[0], form_fields_base[1], "Horário em que houve alteração da latência:", form_fields_base[2], form_fields_base[3]]
        session['form_data_keys'] = [form_data_keys_base[0], form_data_keys_base[1], 'horario_latencia', form_data_keys_base[2], form_data_keys_base[3]]
        session['form_title'] = "Para Alta Latência no circuito preciso que você informe os seguintes dados:"
        session['form_summary_handler'] = 'alta_latencia_summary'
    elif user_input == "4": # Incremento de Erros
        session['form_fields'] = form_fields_base
        session['form_data_keys'] = form_data_keys_base
        session['form_title'] = "Para Incremento de Erros no circuito preciso que você informe os seguintes dados:"
        session['form_summary_handler'] = 'incremento_erros_summary'
    elif user_input == "5": # Indisponível / Down
        session['form_fields'] = [form_fields_base[0], form_fields_base[1], "Horário em que o circuito ficou Indisponível:", form_fields_base[2], form_fields_base[3]]
        session['form_data_keys'] = [form_data_keys_base[0], form_data_keys_base[1], 'horario_indisponibilidade', form_data_keys_base[2], form_data_keys_base[3]]
        session['form_title'] = "Para Indisponibilidade do circuito preciso que você informe os seguintes dados:"
        session['form_summary_handler'] = 'indisponivel_down_summary'
    elif user_input == "0":
        return abertura_chamado_menu_display()
    else:
        messages = problema_circuito_menu_display()
        messages.insert(0, "Opção inválida, tente novamente.")
        return messages

    # Inicia coleta de dados para o problema escolhido
    session['current_handler'] = 'collect_form_data_handler'
    session['current_field_index'] = 0
    session['context'] = {}
    return [session['form_title'], session['form_fields'][0]]


# --- Handler genérico para coletar dados de formulários ---
def collect_form_data_handler(user_input):
    current_index_answered = session.get('current_field_index', 0) # Índice da pergunta que FOI RESPONDIDA
    form_fields = session.get('form_fields', [])
    form_data_keys = session.get('form_data_keys', [])
    
    # Salva a resposta atual
    if current_index_answered < len(form_data_keys):
        key_to_save = form_data_keys[current_index_answered]
        session['context'][key_to_save] = user_input
    else:
        # Erro improvável se a lógica de configuração do formulário estiver correta
        return ["Erro: Índice de campo inválido ao salvar dados."]

    # Prepara para a próxima pergunta ou finaliza
    next_field_index_to_ask = current_index_answered + 1
    session['current_field_index'] = next_field_index_to_ask # Atualiza para o índice da PRÓXIMA pergunta

    if next_field_index_to_ask < len(form_fields):
        # Ainda há campos para perguntar
        next_question = form_fields[next_field_index_to_ask]
        return [next_question]
    else:
        # Todos os campos foram coletados, chama o handler de resumo
        summary_handler_name = session.get('form_summary_handler')
        if summary_handler_name and summary_handler_name in globals():
            summary_handler_func = globals()[summary_handler_name]
            return summary_handler_func(session['context'])
        else:
            return ["Erro: Handler de resumo do formulário não encontrado."]

# --- Funções de Resumo e Finalização ---
def finalizar_atendimento(summary_messages):
    final_message = "Atendimento finalizado. Agradecemos o contato. Até logo!"
    session.clear()
    return summary_messages + [final_message]

def intermitencia_summary(data):
    messages = [
        "Obrigado, os dados foram registrados para a abertura do seu chamado. Estamos abrindo seu chamado...",
        "=== RESUMO DO CHAMADO ===",
        f"Cliente: {data.get('nome_cliente', 'N/A')}",
        f"ID do circuito: {data.get('id_circuito', 'N/A')}",
        f"Horário dos flaps: {data.get('horario_flaps', 'N/A')}",
        f"Tipo do circuito: {data.get('tipo_circuito', 'N/A')}",
        f"Chamado interno: {data.get('chamado_interno', 'N/A')}",
    ]
    return finalizar_atendimento(messages)

def perda_pacote_summary(data):
    messages = [
        "Obrigado, os dados foram registrados para a abertura do seu chamado. Estamos abrindo seu chamado...",
        "=== RESUMO DO CHAMADO ===",
        f"Cliente: {data.get('nome_cliente', 'N/A')}",
        f"ID do circuito: {data.get('id_circuito', 'N/A')}",
        f"Horário das perdas: {data.get('horario_perdas', 'N/A')}",
        f"Tipo do circuito: {data.get('tipo_circuito', 'N/A')}",
        f"Chamado interno: {data.get('chamado_interno', 'N/A')}",
    ]
    return finalizar_atendimento(messages)

def alta_latencia_summary(data):
    messages = [
        "Obrigado, os dados foram registrados para a abertura do seu chamado. Estamos abrindo seu chamado...",
        "=== RESUMO DO CHAMADO ===",
        f"Cliente: {data.get('nome_cliente', 'N/A')}",
        f"ID do circuito: {data.get('id_circuito', 'N/A')}",
        f"Horário da Alta Latência: {data.get('horario_latencia', 'N/A')}",
        f"Tipo do circuito: {data.get('tipo_circuito', 'N/A')}",
        f"Chamado interno: {data.get('chamado_interno', 'N/A')}",
    ]
    return finalizar_atendimento(messages)

def incremento_erros_summary(data):
    messages = [
        "Obrigado, os dados foram registrados para a abertura do seu chamado. Estamos abrindo seu chamado...",
        "=== RESUMO DO CHAMADO ===",
        f"Cliente: {data.get('nome_cliente', 'N/A')}",
        f"ID do circuito: {data.get('id_circuito', 'N/A')}",
        f"Tipo do circuito: {data.get('tipo_circuito', 'N/A')}",
        f"Chamado interno: {data.get('chamado_interno', 'N/A')}",
    ]
    return finalizar_atendimento(messages)

def indisponivel_down_summary(data):
    messages = [
        "Obrigado, os dados foram registrados para a abertura do seu chamado. Estamos abrindo seu chamado...",
        "=== RESUMO DO CHAMADO ===",
        f"Cliente: {data.get('nome_cliente', 'N/A')}",
        f"ID do circuito: {data.get('id_circuito', 'N/A')}",
        f"Horário da Indisponibilidade: {data.get('horario_indisponibilidade', 'N/A')}",
        f"Tipo do circuito: {data.get('tipo_circuito', 'N/A')}",
        f"Chamado interno: {data.get('chamado_interno', 'N/A')}",
    ]
    return finalizar_atendimento(messages)

def liberacao_prefixo_summary(data):
    messages = [
        "Obrigado, os dados foram registrados para a abertura do seu chamado. Estamos abrindo seu chamado...",
        "=== RESUMO DO CHAMADO ===",
        f"Cliente: {data.get('nome_cliente', 'N/A')}",
        f"IP do Prefixo: {data.get('ip_prefixo', 'N/A')}",
        f"AS do Prefixo: {data.get('as_prefixo', 'N/A')}",
        f"Chamado interno: {data.get('chamado_interno', 'N/A')}",
    ]
    return finalizar_atendimento(messages)

def manutencao_agendada_summary(data):
    messages = [
        "Obrigado, os dados foram registrados para a abertura do seu chamado. Estamos abrindo seu chamado...",
        "=== RESUMO DO CHAMADO ===",
        f"Cliente: {data.get('nome_cliente', 'N/A')}",
        f"ID da atividade: {data.get('id_atividade', 'N/A')}", # Corrigido de 'ativvidade'
        f"Horário de Inicio: {data.get('inicio_manutencao', 'N/A')}",
        f"Horário de Finalização: {data.get('fim_manutencao', 'N/A')}",
        f"Chamado interno: {data.get('chamado_interno', 'N/A')}",
    ]
    return finalizar_atendimento(messages)

# --- Comercial e Atendente ---
def comercial_menu_display():
    messages = [
        "Nosso setor Comercial atende no horário 9:00 - 19:00:",
        "1- Email para contato",
        "0- Voltar"
    ]
    session['current_handler'] = 'tratar_comercial_handler'
    return messages

def tratar_comercial_handler(user_input):
    if user_input == "1":
        messages = ["O email para contato com o Comercial é o comercial@pinpoint.com"]
        return finalizar_atendimento(messages)
    elif user_input == "0":
        return menu_opcao_display()
    else:
        messages = comercial_menu_display()
        messages.insert(0, "Opção inválida, tente novamente.")
        return messages

def atendente_menu_display():
    messages = [
        "Nossos atendentes estão de prontidão para te atender:",
        "1- Entrar em contato",
        "0- Voltar"
    ]
    session['current_handler'] = 'tratar_atendente_handler'
    return messages

def tratar_atendente_handler(user_input):
    if user_input == "1":
        messages = ["Para entrar em contato com um dos nossos atendentes ligue no telefone 9 xxxx-xxxx"]
        return finalizar_atendimento(messages)
    elif user_input == "0":
        return menu_opcao_display()
    else:
        messages = atendente_menu_display()
        messages.insert(0, "Opção inválida, tente novamente.")
        return messages

# --- Rotas Flask ---
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat_endpoint(): # Renomeado para evitar conflito com o módulo 'chat' se houvesse
    user_message = request.json.get('message')
    bot_responses = []
    
    current_handler_name = session.get('current_handler')
    if not current_handler_name : # Sessão expirou ou foi limpa (fim de conversa)
        bot_responses = menu_opcao_display()
        session['active_session'] = True # Marca que uma nova sessão está ativa
    else:
        handler_function = globals().get(current_handler_name)
        if handler_function:
            bot_responses = handler_function(user_message)
            # Verifica se a sessão foi limpa por 'finalizar_atendimento'
            session['active_session'] = 'current_handler' in session 
        else:
            bot_responses = ["Desculpe, ocorreu um erro interno no bot (handler não encontrado)."]
            session.clear()
            session['active_session'] = False
            
    return jsonify({'responses': bot_responses, 'session_active': session.get('active_session', False)})

@app.route('/start_chat', methods=['GET'])
def start_chat():
    session.clear() 
    bot_responses = menu_opcao_display()
    session['active_session'] = True
    return jsonify({'responses': bot_responses, 'session_active': True})

if __name__ == '__main__':
    app.run(debug=True)