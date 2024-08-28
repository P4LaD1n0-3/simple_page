from flask import Flask, flash, jsonify, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/webhook', methods=['GET'])
def verify_webhook():
    verify_token = "SEU_TOKEN_VERIFICACAO"
    mode = request.args.get('hub.mode')
    token = request.args.get('hub.verify_token')
    challenge = request.args.get('hub.challenge')

    if mode and token:
        if mode == 'subscribe' and token == verify_token:
            return challenge, 200
        else:
            return 'Verificação falhou', 403
        


@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()

    # Verificar se há mensagens recebidas
    if data.get('entry') and data['entry'][0].get('changes') and data['entry'][0]['changes'][0].get('value'):
        messages = data['entry'][0]['changes'][0]['value'].get('messages')

        if messages:
            for message in messages:
                sender_id = message['from']  # ID do remetente
                message_body = message.get('text', {}).get('body')  # Texto da mensagem

                if message_body:
                    # Exibe a mensagem no site
                    flash(f'Mensagem recebida de {sender_id}: {message_body}', 'success')
                    print(f"Mensagem recebida de {sender_id}: {message_body}")
                    
    return jsonify({"status": "mensagem recebida"}), 200

