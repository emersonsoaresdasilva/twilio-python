import os
from twilio.rest import Client

# Cria uma função para enviar WhatsApp
def envia_mensagem_whatsapp(numero, mensagem):
    # Busca a chave da conta no arquivo .env
    account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
    # Busca o token da conta no arquivo .env
    auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
    # Cria um objeto cliente do Twilio
    client = Client(account_sid, auth_token)
    try:
        # Tenta enviar a mensagem
        client.messages.create(
                            from_=os.environ.get('TWILIO_FROM_WHATSAPP'),
                            body=mensagem,
                            to=f'whatsapp:+55{numero}'
        )
        # Caso tenha enviado, retorna a mensagem
        return f'\nWhatsApp enviado com sucesso, para o número: {numero}'
    except Exception:
        # Caso não tenha enviado, retorna o erro
        return f'\nNão foi possível enviar o WhatsApp, verifique o número digitado: {numero}'