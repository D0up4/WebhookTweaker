import requests
import base64

def update_webhook(webhook_url, new_name, avatar_file=None):
    webhook_id, webhook_token = webhook_url.split("/")[-2:]
    url = f"https://discord.com/api/webhooks/{webhook_id}/{webhook_token}"

    data = {"name": new_name}
    if avatar_file:
        with open(avatar_file, "rb") as f:
            b64_avatar = base64.b64encode(f.read()).decode("utf-8")
        data["avatar"] = f"data:image/png;base64,{b64_avatar}"

    response = requests.patch(url, json=data)
    if response.ok:
        print("Webhook updated successfully!")
    else:
        print("Failed to update webhook:", response.text)

# Example usage:
webhook_url = input("Insert webhook URL: ")
new_name = input("Insert new webhook name: ")
avatar_path = input("Insert avatar image path (or leave blank): ").strip() or None

update_webhook(webhook_url, new_name, avatar_path)
