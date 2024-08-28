from flask import Flask, request, jsonify, render_template, flash

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta'  # Necessário para usar flash messages

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/webhook', methods=['GET'])
def verify_webhook():
    try:
        verify_token = "SEU_TOKEN_VERIFICACAO"
        mode = request.args.get('hub.mode')
        token = request.args.get('hub.verify_token')
        challenge = request.args.get('hub.challenge')

        if mode and token:
            if mode == 'subscribe' and token == verify_token:
                flash('Webhook verificado com sucesso!', 'success')
                return render_template('index.html', challenge=challenge)
            else:
                flash('Falha na verificação do webhook.', 'danger')
                return render_template('index.html'), 403
        else:
            flash('Parâmetros de verificação ausentes.', 'danger')
            return render_template('index.html'), 400
    except Exception as e:
        flash(f'Erro durante a verificação: {e}', 'danger')
        return render_template('index.html'), 500
    finally:
        # Retorna uma resposta padrão caso nenhuma das condições anteriores seja satisfeita
        return render_template('index.html')

@app.route('/webhook', methods=['POST'])
def webhook():
    try:
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
                        
        return render_template('index.html'), 200
    except Exception as e:
        flash(f'Erro ao processar o webhook: {e}', 'danger')
        return render_template('index.html'), 500

