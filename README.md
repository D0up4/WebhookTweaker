# 📌 WebhookTweaker

> *Quick and simple tweaks for your Discord webhooks.*

**WebhookTweaker** is a lightweight command-line tool that lets you easily update the **name** and **avatar** of any Discord webhook — without needing to touch the Discord UI or manually encode images. Just plug in your webhook URL, enter your new settings, and you’re done.

---

## ✨ Features

- 🔧 Change the **username** of any valid Discord webhook  
- 🖼️ Update the **avatar** by providing a local image file path  
- 🧪 Simple CLI flow — no code or JSON required  
- 💻 Works on Linux, macOS, and Windows (Python-based)  
- 🔒 No Discord account login required — just the webhook URL  

---

## 🚀 Demo

```bash
$ python webhook_tweaker.py

Insert Webhook URL: https://discord.com/api/webhooks/...
Insert New Webhook Name: My Cool Bot
Insert Avatar Image Path (or leave blank): ./avatar.png

✅ Webhook updated successfully!

```
## 🔧 Requirements

- Python 3.7+

- requests library (install with pip install requests)

## 🛠️ Usage
```bash

- python WebhookTweaker.py

```
You'll be prompted to enter:

- The full webhook URL

- A new name for the webhook

- (Optional) A path to an image file to set as the new avatar

## ⚠️ Disclaimer

This tool only works with valid Discord webhook URLs (which include the webhook token). It doesn’t access your Discord account or require OAuth.

Use responsibly. Abusing webhooks can result in bans or restrictions from Discord.
