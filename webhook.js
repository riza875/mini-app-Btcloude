const BOT_TOKEN = "8988271542:AAHP-C5_AXfTzgx9VkjdYuk96jaZ4pB00bE";
const MINI_APP_URL = "https://mini-app-btcloude.vercel.app";

async function sendMessage(chatId, text, replyMarkup) {
  const body = {
    chat_id: chatId,
    text: text,
    parse_mode: "HTML"
  };
  if (replyMarkup) body.reply_markup = replyMarkup;

  await fetch(`https://api.telegram.org/bot${BOT_TOKEN}/sendMessage`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(body)
  });
}

export default async function handler(req, res) {
  if (req.method !== "POST") {
    return res.status(200).send("OK");
  }

  try {
    const body = req.body;
    const message = body.message || body.edited_message;
    if (!message) return res.status(200).send("OK");

    const chatId = message.chat.id;
    const text = message.text || "";
    const firstName = message.from?.first_name || "Miner";

    if (text.startsWith("/start")) {
      await sendMessage(
        chatId,
        `🪙 Halo <b>${firstName}</b>!\n\nSelamat datang di <b>BTcloude Mining</b>!\nKlik tombol di bawah untuk mulai menambang BTC ⬇️`,
        {
          inline_keyboard: [[
            {
              text: "⛏️ Buka BTcloude Mining",
              web_app: { url: MINI_APP_URL }
            }
          ]]
        }
      );
    } else if (text.startsWith("/help")) {
      await sendMessage(
        chatId,
        "⛏️ <b>BTcloude Mining Bot</b>\n\n/start — Buka aplikasi mining\n/help — Bantuan"
      );
    }
  } catch (e) {
    console.error(e);
  }

  return res.status(200).send("OK");
}
