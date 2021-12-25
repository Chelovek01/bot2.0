# TradingView Example Alert Message:
# {
# "key":"111111", "telegram":"-1001598944846", "msg":"Long #{{ticker}} at `{{close}}`"
# }

sec_key = (
    "111111"  # Can be anything. Has to match with "key" in your TradingView alert message
)

# Telegram Settings
send_telegram_alerts = False
tg_token = "5000701161:AAGDMpLL19yykW8W9bTToarm1ORSCkU_HTM"  # Bot token. Get it from @Botfather
channel = -1001598944846  # Channel ID (ex. -1001487568087)