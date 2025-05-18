import streamlit as st
import google.generativeai as genai
from datetime import datetime, timedelta
from urllib.parse import quote_plus
import base64

# 🔐 Carrega a API key a partir do arquivo secrets.toml
api_key = st.secrets["gemini"]["api_key"]
genai.configure(api_key=api_key)

# 🤖 Função para criar o modelo de IA
def criar_modelo_organizai():
    return genai.GenerativeModel(
        model_name="gemini-2.0-flash-001",
        generation_config={"temperature": 1},
        system_instruction="""
Você é a OrganizAÍ, uma assistente de produtividade gentil e direta ao ponto. Seu trabalho é organizar o dia da pessoa com carinho, mas também com inteligência prática. O resultado final deve ser uma tabela com 4 colunas: Início | Fim | Tarefa | Prioridade. Na coluna de prioridade, você deve escrever "Sim" para tarefas que são prioritárias e "-" para pausas, transições (Por exemplo: Ir para a academia, Voltar da academia, fazer almoço, fazer a janta, ou qualquer deslocamento que o usuário precisa fazer) ou tempo livre.

Regras que você sempre deve seguir:
1. Se o usuário indicar um horário específico para uma tarefa (ex: “almoçar de 14h às 15h”), use esse horário exato e adapte os horários restantes em torno disso.
2. Se o usuário mencionar que quer fazer algo em um horário específico, leve isso como sugestão forte. Respeite.
3. Entre cada bloco de tarefa inclua uma pausa de 15 minutos antes da próxima tarefa sendo ela prioritária ou não, se houver tempo.
4. Evite engessar a resposta. Você deve analisar as tarefas que o usuário quer fazer, a energia dele para fazer as tarefas, os blocos de tempo que ele sugeriu e os horários de começar e terminar. Depois disso, você precisa pensar em como melhorar o planejamento do dia dele sempre de forma leve, prática e util.
5. Evite criar blocos de foco em cima de horários fixos informados. Ex: se a pessoa disse que almoça às 14h, não faz sentido colocar a próxima tarefa para às 14h30, ela precisa do descanso antes de começar a próxima tarefa. Para isso, use um tempo de transição.
6. Se sobrar tempo ao final do dia, ofereça um bloco escrito "Tempo livre para curtir o dia" 🧘‍♀️.
7. Não adicione negrito, markdown nem formatações visuais fora da tabela. Apenas a tabela markdown e a frase final.
8. O título "🤖 Pronto! Organizei ai pra ti" deve ser incluído no topo da resposta da IA, como parte do markdown.
9. Sempre termine o planner com uma frase simpática, engraçada e motivacional — sem clichês de coach, logo após a tabela no mesmo markdown.


Exemplo esperado de saída (formato da tabela lembre-se de centralizar a tabela '<div align="center">'):

| Início | Fim   | Tarefa                           | Prioridade |
|--------|-------|----------------------------------|------------|
| 13:45  | 14:00 | Relaxar antes do almoço          | -          |
| 14:00  | 15:00 | Almoçar                          | Sim        |
| 15:00  | 15:15 | Pausa (volta do almoço)          | -          |
| 15:15  | 16:00 | Estudar IA                       | Sim        |
| 16:00  | 16:15 | Pausa (respira fundo!)           | -          |
| 16:15  | 17:00 | Estudar IA                       | Sim        |
| 17:00  | 17:15 | Pausa (ir para a academia)       | -          |
| 17:15  | 18:00 | Treinar na academia              | Sim        |
| 18:00  | 18:15 | Pausa (volta da academia)        | -          |
| 18:15  | 19:00 | Estudar (opcional)               | Sim        |
| 19:00  | 19:45 | Tempo livre pra curtir o dia 🧘‍♀️  | -          |


"""
    )

# Cria a instância do modelo
model = criar_modelo_organizai()

# 🌆 Aplica fundo da página
def set_background(image_file):
    with open(image_file, "rb") as img:
        encoded = base64.b64encode(img.read()).decode()

    st.markdown(
        f"""
        <style>
        table {{
            margin-left: auto; 
            margin-right: auto;

        }}

        .botao-personalizado {{
        display: inline-block; /* Permite que o botão se ajuste ao conteúdo */
        color: white;
        font-weight: bold;
        background: linear-gradient(135deg, rgba(255, 159, 207, 0.4), rgba(0, 255, 247, 0.4));
        padding: 6px 12px; /* Aumentei um pouco o padding para melhor toque em mobile */
        border-radius: 5px;
        text-decoration: none;
        font-size: 14px; /* Tamanho de fonte um pouco maior para mobile */
        margin-right: 10px; /* Adiciona margem à direita para criar espaço entre os botões */
        margin-bottom: 10px; /* Adiciona margem abaixo para criar espaço entre os botões */
        white-space: nowrap; /* Evita que o texto quebre em várias linhas, se possível */
        }}

    
        @media (max-width: 600px) {{ 
        .botao-personalizado {{
            display: block; /* Faz o botão ocupar a largura total disponível */
            width: auto; /* Garante que o botão ocupe toda a largura */
            margin-bottom: 8px; /* Adiciona um espaço abaixo do botão se houver outros elementos */
            text-align: center; /* Centraliza o texto dentro do botão */
            box-sizing: border-box; /* Garante que o padding não aumente a largura total */
            margin-right: 0; /* Remove a margem direita em telas menores */
        }}
        }}

        p {{
            text-align: center;
            }}

        .stApp {{
            background-image: url("data:image/png;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}

        h1 {{
            text-align: center;
            font-weight: 800;
            text-shadow: 2px 2px 4px #FF9FCF;
        }}

        h2, .markdown-text-container h2 {{
            text-align: center !important;
            font-size: 1.2rem !important;
            font-weight: 400 !important;
            margin-top: -10px !important;
            color: #C6D8D9 !important;
        }}

        label, .stTextInput label, .stSelectbox label, .stNumberInput label, .stTextArea label {{
            color: #C6D8D9 !important;
            font-weight: 700;
        }}

        input, textarea {{
            background-color: rgba(255, 255, 255, 0.1);
            border: 2px solid #00FFF7;
            border-radius: 8px;
            color: white;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# ⚙️ Configura a página e aplica o fundo
st.set_page_config(page_title="OrganizAÍ pra mim?", page_icon="🧠")
set_background("fundo.png")

# Cabeçalho do app
st.markdown("""
    <h1>🧠 OrganizAÍ pra mim?</h1>
    <h2>Seu dia com eficiência e uma pitada de inteligência.</h2>
    <hr>
""", unsafe_allow_html=True)

# ⏰ Cria lista de horários em intervalos de 15 minutos
horas = [f"{h:02d}:{m:02d}" for h in range(0, 24) for m in (0, 15, 30, 45)]

# 📋 Formulário de entrada de dados
with st.form("formulario"):
    col1, col2 = st.columns(2)
    with col1:
        horario_inicio = st.selectbox("⏰ **Que horas você quer começar?**", horas)
        energia = st.selectbox("🔋 **Como está sua energia?**", ["Alta", "Média", "Baixa"], index=1)
        tarefas = st.text_area("📋 **Tarefas do dia (separadas por vírgula)**", placeholder="Trabalhar, Estudar IA, Ir à academia...")
    with col2:
        horario_fim = st.selectbox("🛌 **Até que horas quer produzir?**", horas, index=horas.index("22:00"))
        bloco = st.number_input("⏱️ **Duração dos blocos (min)**", min_value=15, value=45, step=5)
        prioridades = st.text_area("⭐ **Tarefas prioritárias (ou 'Todas')**", placeholder="Estudar IA, Trabalhar...")
    enviar = st.form_submit_button(
        "Organiza aí pra mim! 🚀",
        use_container_width=True
    )
  

# 🧠 Extrai eventos do texto em Markdown gerado pela IA
def extrair_eventos(texto):
    eventos = []
    linhas = texto.split("\n")
    for linha in linhas:
        if "|" in linha and "-" not in linha:
            partes = [p.strip() for p in linha.split("|") if p.strip()]
            if len(partes) >= 3:
                inicio, fim, tarefa = partes[0], partes[1], partes[2]
                if ":" in inicio and ":" in fim:
                    eventos.append({"titulo": tarefa, "inicio_str": inicio, "fim_str": fim})
    return eventos

# 📅 Gera link do Google Calendar
def gerar_link_google_calendar(titulo, inicio_str, fim_str, data_hoje_str):
    try:
        inicio_fmt = data_hoje_str + "T" + inicio_str.replace(":", "") + "00"
        fim_fmt = data_hoje_str + "T" + fim_str.replace(":", "") + "00"
    except:
        return None
    base = "https://www.google.com/calendar/render?action=TEMPLATE"
    text = f"&text={quote_plus(titulo)}"
    dates = f"&dates={quote_plus(inicio_fmt)}/{quote_plus(fim_fmt)}"
    details = f"&details=Gerado%20pelo%20OrganizAÍ"
    timezone = "&ctz=America/Sao_Paulo"
    return f"{base}{text}{dates}{details}{timezone}"

# 🚀 Geração do planner
if enviar:
    if not tarefas.strip():
        st.warning("Você precisa colocar pelo menos uma tarefa.")
    else:
        tarefas_list = [t.strip() for t in tarefas.split(",") if t.strip()]
        prioridades_list = tarefas_list if prioridades.strip().lower() == "todas" else [p.strip() for p in prioridades.split(",") if p.strip()]

        prompt = f"""
Planeje meu dia considerando:
- Começo: {horario_inicio}
- Fim: {horario_fim}
- Energia: {energia}
- Blocos de foco: {bloco} minutos
- Tarefas: {', '.join(tarefas_list)}
- Prioridades: {', '.join(prioridades_list)}

Regras que você sempre deve seguir:
1. Se o usuário indicar um horário específico para uma tarefa (ex: “almoçar de 14h às 15h”), use esse horário exato e adapte os horários restantes em torno disso.
2. Se o usuário mencionar que quer fazer algo em um horário específico, leve isso como sugestão forte. Respeite.
3. Entre cada bloco de tarefa inclua uma pausa de 15 minutos antes da próxima tarefa sendo ela prioritária ou não, se houver tempo.
4. Evite engessar a resposta. Você deve analisar as tarefas que o usuário quer fazer, a energia dele para fazer as tarefas, os blocos de tempo que ele sugeriu e os horários de começar e terminar. Depois disso, você precisa pensar em como melhorar o planejamento do dia dele sempre de forma leve, prática e util.
5. Evite criar blocos de foco em cima de horários fixos informados. Ex: se a pessoa disse que almoça às 14h, não faz sentido colocar a próxima tarefa para às 14h30, ela precisa do descanso antes de começar a próxima tarefa. Para isso, use um tempo de transição.
6. Se sobrar tempo ao final do dia, ofereça um bloco escrito "Tempo livre para curtir o dia" 🧘‍♀️.
7. Não adicione negrito, markdown nem formatações visuais fora da tabela. Apenas a tabela markdown e a frase final.
8. O título "🤖 Pronto! Organizei ai pra ti" deve ser incluído no topo da resposta da IA, como parte do markdown.
9. Sempre termine o planner com uma frase simpática, engraçada e motivacional — sem clichês de coach, logo após a tabela no mesmo markdown.


Exemplo esperado de saída (formato da tabela, lembre-se de centralizar a tabela '<div align="center">'):

| Início | Fim   | Tarefa                           | Prioridade |
|--------|-------|----------------------------------|------------|
| 13:45  | 14:00 | Relaxar antes do almoço          | -          |
| 14:00  | 15:00 | Almoçar                          | Sim        |
| 15:00  | 15:15 | Pausa (volta do almoço)          | -          |
| 15:15  | 16:00 | Estudar IA                       | Sim        |
| 16:00  | 16:15 | Pausa (respira fundo!)           | -          |
| 16:15  | 17:00 | Estudar IA                       | Sim        |
| 17:00  | 17:15 | Pausa (ir para a academia)       | -          |
| 17:15  | 18:00 | Treinar na academia              | Sim        |
| 18:00  | 18:15 | Pausa (volta da academia)        | -          |
| 18:15  | 19:00 | Estudar (opcional)               | Sim        |
| 19:00  | 19:45 | Tempo livre pra curtir o dia 🧘‍♀️  | -          |

"""

        with st.spinner("Organizando seu dia com inteligência... 🧠"):
            resposta = model.generate_content(prompt)
            texto_gerado = resposta.text
        

            st.markdown("""
                <div style="
                    background-color: rgba(255, 255, 255, 0.05);
                    padding: 2rem;
                    border-radius: 20px;
                    box-shadow: 0 0 15px rgba(255, 159, 207, 0.3);
                    margin-top: 2rem;
                    margin-bottom: 1rem;
                ">
                    <h3 style='color:#ffffff; text-align:center;'>📋 Planner do dia</h3>
                </div>
            """, unsafe_allow_html=True)

            eventos = extrair_eventos(texto_gerado)

            eventos_formatados = []
            for ev in eventos:
                titulo_lower = ev["titulo"].lower()
                if "almoço" in titulo_lower or "almoçar" in titulo_lower:
                    inicio_dt = datetime.strptime(ev["inicio_str"], "%H:%M")
                    fim_dt = inicio_dt + timedelta(hours=1)
                    ev["fim_str"] = fim_dt.strftime("%H:%M")
                    ev["tipo"] = "almoco"
                elif "pausa" in titulo_lower:
                    ev["tipo"] = "pausa"
                elif "estudar" in titulo_lower:
                    if titulo_lower.strip() == "estudar":
                        ev["tipo"] = "estudo_vazio"
                    else:
                        ev["tipo"] = "estudo"
                        ev["termo_estudo"] = titulo_lower.replace("estudar", "").strip()
                else:
                    ev["tipo"] = "tarefa"
                eventos_formatados.append(ev)

            eventos = eventos_formatados

            eventos_com_pausas = []
            for i in range(len(eventos)):
                eventos_com_pausas.append(eventos[i])
                if i < len(eventos) - 1:
                    fim_atual = datetime.strptime(eventos[i]["fim_str"], "%H:%M")
                    inicio_prox = datetime.strptime(eventos[i + 1]["inicio_str"], "%H:%M")
                    if fim_atual < inicio_prox:
                        eventos_com_pausas.append({
                    "titulo": "Pausa ☕",
                    "inicio_str": fim_atual.strftime("%H:%M"),
                    "fim_str": inicio_prox.strftime("%H:%M"),
                    "tipo": "pausa"
                })

            markdown_tabela = "| Início | Fim | Tarefa | Prioridade |\n|--------|-----|--------|------------|\n"
            for ev in eventos_com_pausas:
                markdown_tabela += f"| {ev['inicio_str']} | {ev['fim_str']} | {ev['titulo']} | {'-' if 'pausa' in ev['titulo'].lower() else 'Sim'} |\n"

            st.markdown(texto_gerado)

            if eventos_com_pausas:
                st.markdown("""
                    <div style="
                        background-color: rgba(255, 255, 255, 0.05);
                        padding: 2rem;
                        border-radius: 20px;
                        box-shadow: 0 0 15px rgba(255, 159, 207, 0.3);
                        margin-top: 3rem;
                        margin-bottom: 1rem;
                    ">
                        <h3 style='color:#ffffff; text-align:center;'>📅 Adicionar ao Google Calendar</h3>
                    </div>
                """, unsafe_allow_html=True)

                data_str = datetime.now().strftime("%Y%m%d")

                for ev in eventos_com_pausas:
                    tipo = ev.get("tipo", "tarefa")
                    texto = f"{ev['inicio_str']} - {ev['fim_str']}: {ev['titulo']}"
                    botao_html = ""
                    if tipo == "pausa":
                        botao_html = '<a href="https://www.google.com/maps/search/cafeterias+padarias+parques+perto+de+mim" class="botao-personalizado" style="text-decoration: none; color: white">☕ Hora do cafezinho</a>'

                    elif tipo == "almoco":
                        botao_html = '<a href="https://www.google.com/maps/search/restaurantes+perto+de+mim" class="botao-personalizado" style="text-decoration: none; color: white">🍽️ Ver restaurantes</a>'

                    elif tipo == "estudo_vazio":
                        botao_html = (
                            '<a href="https://www.google.com" class="botao-personalizado" style="text-decoration: none; color: white">🔍 Abrir Google</a><br>'

                            + f'<a href="{gerar_link_google_calendar(ev["titulo"], ev["inicio_str"], ev["fim_str"], data_str)}" class="botao-personalizado" style="text-decoration: none; color: white">➕ Add</a>'
                        )

                    elif tipo == "estudo":
                        termo = quote_plus("assuntos recentes sobre " + ev.get("termo_estudo", ""))
                        botao_html = (
                            f'<a href="https://www.google.com/search?q={termo}" class="botao-personalizado" style="text-decoration: none; color: white">🔍 Pesquisar</a><br>'

                            + f'<a href="{gerar_link_google_calendar(ev["titulo"], ev["inicio_str"], ev["fim_str"], data_str)}" class="botao-personalizado" style="text-decoration: none; color: white">➕ Add</a>'
                        )
                    else:
                        botao_html = f'<a href="{gerar_link_google_calendar(ev["titulo"], ev["inicio_str"], ev["fim_str"], data_str)}" class="botao-personalizado" style="text-decoration: none; color: white">➕ Add</a>'

                    st.markdown(f"""
                        <div style="
                            background-color: rgba(255, 255, 255, 0.06);
                            padding: 1rem 1.5rem;
                            margin-bottom: 0.8rem;
                            border-radius: 12px;
                            box-shadow: 0 0 10px rgba(255, 255, 255, 0.05);
                            display: flex;
                            justify-content: space-between;
                            align-items: center;
                        ">
                            <span style='font-size: 0.85rem; color: #EAEAEA;'>{texto}</span>
                            {botao_html}
                        </div>
                    """, unsafe_allow_html=True)

                st.caption("Lembre-se de ajustar a data no Google Calendar se estiver planejando para outro dia.")
