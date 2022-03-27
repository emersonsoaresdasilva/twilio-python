from dotenv import load_dotenv
from module.sms import envia_mensagem_sms
from module.whatsapp import envia_mensagem_whatsapp

# Cria uma função para enviar SMS e WhatsApp
def envia_mensagem(numero, mensagem):
    # Envia SMS ao destinatário
    envia_mensagem_sms(numero, mensagem)
    # Envia WhatsApp ao destinatário
    envia_mensagem_whatsapp(numero, mensagem)

if __name__ == '__main__':
    # Carrega as variáveis de ambiente
    load_dotenv()
    # Envia SMS para o destinatário
    print(envia_mensagem_sms('', ''))
    # Envia WhatsApp para o destinatário
    print(envia_mensagem_whatsapp('', ''))
    # Envia SMS e WhatsApp para o destinatário
    print(envia_mensagem('', ''))
