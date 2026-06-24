# 📱 WhatsApp Automation com Python

Esse projeto nasceu de uma necessidade real: precisava enviar mensagens personalizadas para uma lista de contatos no WhatsApp sem fazer isso um por um manualmente.

O script lê uma planilha Excel com os contatos, personaliza a mensagem com o nome de cada pessoa e envia tudo automaticamente pelo WhatsApp Web.

---

## O que ele faz

- Lê os contatos de uma planilha Excel
- Personaliza a mensagem com o nome de cada contato
- Envia automaticamente via WhatsApp Web
- Mostra no terminal se cada envio foi um sucesso ou erro

---

## Tecnologias usadas

- Python
- pywhatkit
- pandas
- openpyxl

---

## Como usar

**1. Clone o repositório**
```bash
git clone https://github.com/seu-usuario/whatsapp-automation.git
```

**2. Instale as dependências**
```bash
pip install -r requirements.txt
```

**3. Preencha a planilha**

Abra o arquivo `contatos_whatsapp.xlsx` e preencha com os números e nomes dos contatos.

| numero | nome |
|--------|------|
| +5511999990001 | João |
| +5511999990002 | Maria |

> O número precisa estar no formato internacional com `+` na frente.

**4. Edite a mensagem no `main.py`**

Encontre a variável `mensagem` no código e edite o texto como quiser.

**5. Abra o WhatsApp Web no Chrome**

Acesse [web.whatsapp.com](https://web.whatsapp.com) e faça login.

**6. Rode o script**
```bash
python main.py
```

Não mexa no mouse nem no teclado enquanto o script estiver rodando — ele controla o navegador automaticamente.

---

## Observações

- Funciona melhor no Google Chrome
- Se sua internet for lenta, aumente o `wait_time` no código
- Números de telefone fixo vão retornar erro — o script pula automaticamente e continua

---

Projeto feito enquanto aprendia Python. Simples, mas funcionou! 🚀