from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Центральная база ключей на сервере
VALID_KEYS = {
    "WLYR-A7B9-XM24-991A": "ANY_PC_NAME",
    "WLYR-K3R8-PL77-024B": "ANY_PC_NAME",
    "WLYR-N5E2-QQ11-846C": "ANY_PC_NAME",
    "WLYR-Z9X4-VV88-305D": "ANY_PC_NAME",
    "WLYR-M1O7-BB33-741E": "ANY_PC_NAME",
    "WLYR-L6P2-FF55-192F": "ANY_PC_NAME",
    "WLYR-C8V3-GG44-558G": "ANY_PC_NAME",
    "WLYR-U4Y9-HH22-663H": "ANY_PC_NAME",
    "WLYR-T2I5-SS99-884K": "ANY_PC_NAME",
    "WLYR-Q9W1-JJ66-115M": "ANY_PC_NAME"
}

@app.route('/verify', methods=['POST'])
def verify_key():
    data = request.json
    if not data:
        return jsonify({"status": "error", "message": "Нет данных"}), 400
        
    user_key = data.get("key", "").strip()
    pc_name = data.get("pc_name", "").strip().upper()
    
    if user_key in VALID_KEYS:
        allowed_pc = VALID_KEYS[user_key].strip().upper()
        
        # Если ключ свободный, привязываем его к ПК кента
        if allowed_pc == "ANY_PC_NAME":
            VALID_KEYS[user_key] = pc_name
            return jsonify({"status": "success", "message": "Ключ успешно привязан к вашему ПК!"})
            
        # Проверка соответствия железа
        if allowed_pc == pc_name:
            return jsonify({"status": "success", "message": "Доступ разрешен"})
        else:
            return jsonify({"status": "denied", "message": f"Этот ключ уже привязан к другому ПК: {allowed_pc}"})
    else:
        return jsonify({"status": "invalid", "message": "Введен неверный ключ активации!"})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
