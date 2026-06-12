import os
import json
import hmac
import hashlib
import urllib.request

BOT_TOKEN = "8988271542:AAHP-C5_AXfTzgx9VkjdYuk96jaZ4pB00bE"
MINI_APP_URL = "https://mini-app-btcloude.vercel.app"
TELEGRAM_API = f"https://api.telegram.org/bot{BOT_TOKEN}"

def send_message(chat_id, text, reply_markup=None):
    payload = {
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "HTML"
    }
    if reply_markup:
        payload["reply_markup"] = json.dumps(reply_markup)

    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        f"{TELEGRAM_API}/sendMessage",
        data=data,
        headers={"Content-Type": "application/json"}
    )
    urllib.request.urlopen(req)

def handler(request, response):
    if request.method != "POST":
        response.status_code = 200
        return "OK"

    try:
        body = json.loads(request.body)
        message = body.get("message") or body.get("edited_message")
        if not message:
            response.status_code = 200
            return "OK"

        chat_id = message["chat"]["id"]
        text = message.get("text", "")
        first_name = message.get("from", {}).get("first_name", "Miner")

        if text.startswith("/start"):
            keyboard = {
                "inline_keyboard": [[
                    {
                        "text": "⛏️ Buka BTcloude Mining",
                        "web_app": {"url": MINI_APP_URL}
                    }
                ]]
            }
            send_message(
                chat_id,
                f"🪙 Halo <b>{first_name}</b>!\n\n"
                f"Selamat datang di <b>BTcloude Mining</b>!\n"
                f"Klik tombol di bawah untuk mulai menambang BTC ⬇️",
                reply_markup=keyboard
            )

        elif text.startswith("/help"):
            send_message(
                chat_id,
                "⛏️ <b>BTcloude Mining Bot</b>\n\n"
                "/start — Buka aplikasi mining\n"
                "/help — Bantuan"
            )

    except Exception as e:
        print(f"Error: {e}")

    response.status_code = 200
    return "OK"
