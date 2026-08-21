import os

from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    MenuButtonCommands,
    WebAppInfo,
)

from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)

# =========================
# LOAD ENV
# =========================

BOT_TOKEN   = os.environ.get("BOT_TOKEN")
WEBAPP_URL  = os.environ.get("WEBAPP_URL")
SUPPORT_URL = os.environ.get("SUPPORT_URL")


# =========================
# OPEN BUTTON
# =========================

def open_button():
    return InlineKeyboardMarkup([[
        InlineKeyboardButton(text="Open", web_app=WebAppInfo(url=WEBAPP_URL))
    ]])


# =========================
# SUPPORT BUTTON
# =========================

def support_button():
    return InlineKeyboardMarkup([[
        InlineKeyboardButton(text="Support", url=SUPPORT_URL)
    ]])


# =========================
# START COMMAND
# =========================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "🚀 Your Genuine Gateway to Smarter, More Confident Forex Trading\n\n"
        "Major currencies, exotic pairs, and commodities all live under one convenient "
        "roof, giving both new traders and seasoned veterans a solid launchpad. Fast "
        "execution, competitive fees, and professional-grade tools come standard, so "
        "you're always ready to trade confidently."
    )
    await update.message.reply_text(text=text, reply_markup=open_button())


# =========================
# MAJOR PAIRS
# =========================

async def major_pairs(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🌍 Where the Bulk of Global Trading Volume Actually Lives\n\n"
        "EUR/USD, GBP/USD, and USD/JPY dominate daily trading volume worldwide, "
        "reflecting the size and strength of the economies behind them. These pairs "
        "offer deep liquidity, tighter spreads, and price action that's generally "
        "easier to read and trade.",
        reply_markup=open_button()
    )


# =========================
# LEVERAGE & MARGIN
# =========================

async def leverage_margin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "⚖️ A Genuinely Powerful Tool That Cuts Both Ways at Once\n\n"
        "Leverage lets a modest amount of capital control a much larger position, "
        "giving you flexibility to shape a strategy around your own risk appetite. "
        "Remember, it amplifies losses just as fast as profits, so every trade needs "
        "careful planning.",
        reply_markup=open_button()
    )


# =========================
# TRADING STRATEGIES
# =========================

async def trading_strategies(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📈 Finding the Trading Style That Genuinely Fits Your Life\n\n"
        "Scalping, day trading, swing trading, and position trading each demand a "
        "different amount of time, patience, and risk tolerance. The goal isn't "
        "chasing whatever style is trending online, it's finding the steady rhythm "
        "that genuinely fits your schedule.",
        reply_markup=open_button()
    )


# =========================
# SUPPORT
# =========================

async def support(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "💬 Support That's Genuinely There Whenever You Need It\n\n"
        "Setting up your account, working through a tricky trade, or sharing "
        "feedback about your experience — whatever the reason, our team stays "
        "available around the clock, seven days a week. Don't hesitate to reach out "
        "any time; we're happy to help.",
        reply_markup=support_button()
    )


# =========================
# SETUP MENU COMMANDS
# =========================

async def setup_commands(app):
    commands = [
        ("start",               "Start Bot"),
        ("major_pairs",         "Major Pairs"),
        ("leverage_margin",     "Leverage & Margin"),
        ("trading_strategies",  "Trading Strategies"),
        ("support",             "Help & Support"),
    ]
    await app.bot.set_my_commands(commands)
    await app.bot.set_chat_menu_button(menu_button=MenuButtonCommands())


async def post_init(app):
    await setup_commands(app)


# =========================
# CREATE APP
# =========================

app = (
    Application.builder()
    .token(BOT_TOKEN)
    .post_init(post_init)
    .build()
)

app.add_handler(CommandHandler("start",              start))
app.add_handler(CommandHandler("major_pairs",        major_pairs))
app.add_handler(CommandHandler("leverage_margin",    leverage_margin))
app.add_handler(CommandHandler("trading_strategies", trading_strategies))
app.add_handler(CommandHandler("support",            support))


# =========================
# START BOT
# =========================

print("✅ Forex Bot Running...")
app.run_polling()