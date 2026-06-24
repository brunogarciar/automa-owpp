import pywhatkit
import pandas as pd
import time

df = pd.read_excel("contatos_whatsapp.xlsx"
                   "", dtype=str)

print(f"📋 {len(df)} contatos carregados!\n")

for index, linha in df.iterrows():
    numero = str(linha["numero"]).strip()


    if not numero.startswith("+"):
        numero = "+" + numero

    nome = str(linha["nome"]).strip()

    mensagem = f"""Olá, . {nome}! Tudo bem?

Meu nome é Bruno Garcia """

    try:
        print(f"📤 Enviando para {nome} ({numero})...")
        pywhatkit.sendwhatmsg_instantly(
            phone_no=numero,
            message=mensagem,
            wait_time=12,
            tab_close=True,
            close_time=3
        )
        print(f"   ✅ Enviado com sucesso!")

    except Exception as e:
        print(f"   ❌ Erro: {e}")

    time.sleep(6)

print("\n🎉 Envio finalizado!")