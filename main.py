from dotenv import load_dotenv
from module.sms import envia_mensagem_sms
from module.whatsapp import envia_mensagem_whatsapp

# Cria uma função para enviar SMS e WhatsApp
def envia_mensagem(numero, mensagem):
    # Envia SMS e WhatsApp ao destinatário
    return envia_mensagem_sms(numero, mensagem), envia_mensagem_whatsapp(numero, mensagem)

if __name__ == '__main__':
    # Carrega as variáveis de ambiente
    load_dotenv()
    # Envia SMS para o destinatário
    print(envia_mensagem_sms(numero='', mensagem=''))
    # Envia WhatsApp para o destinatário
    print(envia_mensagem_whatsapp(numero='', mensagem=''))
    # Envia SMS e WhatsApp para o destinatário
    print(envia_mensagem(numero='', mensagem=''))
