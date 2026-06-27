from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Список твоих валидных ключей. Название ПК здесь больше НЕ НУЖНО.
# Сюда можно вписывать любые новые ключи, которые ты придумаешь.
VALID_KEYS = [
    "WLYR-A7B9-XM24-991A",
    "WLYR-K3R8-PL77-024B",
    "WLYR-N5E2-QQ11-846C",
    "WLYR-Z9X4-VV88-305D",
    "WLYR-M1O7-BB33-741E",
    "WLYR-L6P2-FF55-192F",
    "WLYR-C8V3-GG44-558G",
    "WLYR-U4Y9-HH22-663H",
    "WLYR-T2I5-SS99-884K",
    "WLYR-Q9W1-JJ66-115M"
]

@app.route('/verify', methods=['POST'])
def verify_key():
    data = request.json
    if not data:
        return jsonify({"status": "error", "message": "Нет данных"}), 400
        
    user_key = data.get("key", "").strip()
    
    # Проверяем просто наличие ключа в списке
    if user_key in VALID_KEYS:
        return jsonify({"status": "success", "message": "Доступ разрешен"})
    else:
        return jsonify({"status": "invalid", "message": "Введен неверный ключ активации!"})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
