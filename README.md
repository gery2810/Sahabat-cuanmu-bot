# Sahabat Cuanmu Bot

Bot Telegram untuk konsultasi trading sederhana.

## Cara Pakai
1. Buat bot di @BotFather dan salin token.
2. Isi token di file `.env`.
3. Deploy ke Render atau platform lain.
4. Jalankan perintah:
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 10000
   ```

Setelah itu, set webhook dengan:
```
https://api.telegram.org/bot<YOUR_TOKEN>/setWebhook?url=<PUBLIC_BASE_URL>/telegram/webhook
```
