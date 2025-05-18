# 🧠 Hey, OrganizAÍ pra mim? 

Esse é um planejador de tarefas inteligente, que entende a sua rotina e te entrega um cronograma realista, humano e com pausas pra tomar aquele cafezinho ☕. 

## 🌟 Sobre o projeto

O **OrganizAÍ** é uma aplicação web feita com **Streamlit** que combina inteligência artificial e usabilidade para ajudar pessoas a organizarem seu dia de forma prática e personalizada. Utilizando a **API do Gemini**, o app interpreta as tarefas e preferências do usuário e entrega um planner interativo com:

- Sugestões de pausas, transições e tempo livre
- Adição rápida ao Google Calendar
- Sugestões de links úteis para estudar, descansar ou almoçar
- Um toque de humor e acolhimento em cada resposta ❤️

Você pode testar agora 👉 [https://organizaai-imersao-alura-2025.streamlit.app](https://organizaai-imersao-alura-2025.streamlit.app)

---

## ✨ Funcionalidades

- ✅ Geração de planner com base nas suas tarefas e energia do dia
- ✅ Adição automática de pausas entre blocos de foco
- ✅ Botões para adicionar tarefas ao Google Calendar
- ✅ Sugestões de links: pesquisa de estudo, locais para café ou restaurante
- ✅ Interface responsiva e com design acolhedor
- ✅ Respostas com toque humano: o planner vem com título, tabela e uma frase motivacional (sem coach quântico 😄)

---

## 🌐 Interface Web
<table>
  <tr>
    <td style="width: 50%;">
      <img src="/imagem/Imagem pc.jpg" alt="Descrição da Imagem 1" style="width:100%;">
    </td>
    <td style="width: 50%;">
      <img src="/imagem/Imagem mobile.jpg" style="width:100%;">
    </td>
  </tr>
</table>

A interface foi criada com **Streamlit** e totalmente customizada com HTML e CSS para parecer um app moderno. Ela conta com:

- Formulário intuitivo para inserir tarefas e preferências
- Tabela com planner diário
- Blocos interativos com botões personalizados
- Sou adaptado para mobile e notebook
- Não é um Nubank, mas tem o estilo visual com fundo em gradiente roxo aesthetic 💜

---

## 🚀 Como rodar localmente

### ⚙️ Requisitos

- Python 3.10+
- API Key do Gemini (Google AI Studio)

### 💻 Instalação

Clone o repositório:

```bash
git clone https://github.com/seu-usuario/organizai.git
cd organizai
```

Crie e ative o ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Crie o arquivo `secrets.toml` dentro da pasta `.streamlit/`:

```toml
[gemini]
api_key = "SUA_CHAVE_AQUI"
```

Rode o app:

```bash
streamlit run app.py
```

---

## 📁 Estrutura do Projeto

```
organizai/
├── .streamlit/
│   └── secrets.toml
├── app.py              # Código principal com lógica do app e da IA
├── fundo.png           # Imagem de fundo do site
├── requirements.txt    # Dependências
├── README.md           # Este arquivo lindíssimo ✨
```

---

## 🧠 IA por trás do Planner

O modelo Gemini é configurado para:

- Entender e organizar tarefas em blocos de tempo
- Respeitar horários fixos e prioridades informadas pelo usuário
- Adicionar pausas inteligentes entre blocos
- Gerar planner com tom leve, realista e empático
- Finalizar com uma frase simpática no estilo "força na peruca" 😄

---

## 🎨 Estilo e Identidade Visual

- Fundo em gradiente roxo escuro com efeito glow
- Botões com gradientes neon (rosa + ciano)
- Emojis e frases personalizadas
- Layout inspirado em apps mobile de produtividade
- Tipografia sem serifa para leveza e legibilidade

---

## 🔮 Próximos passos

- [ ] Login e histórico de planners por usuário
- [ ] Envio do planner por WhatsApp
- [ ] Exportação para Google Calendar direto
- [ ] Integração com Google Tasks
- [ ] Modo escuro/claro automático

---

## 📝 Licença

MIT ©

Projeto desenvolvido durante a Imersão IA Alura + Gemini 2025.
