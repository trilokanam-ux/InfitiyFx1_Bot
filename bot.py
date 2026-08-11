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
        "🚀 Your Genuine Gateway to Smarter, More Confident Forex Trading\n"
        "Major currencies, exotic pairs, and commodities all live under one convenient roof "
        "here, giving both first-time traders and seasoned market veterans a solid, "
        "confident launchpad regardless of their background or prior experience level. Fast "
        "execution, competitive fees, and professional-grade tools all come standard from "
        "day one, so you're never missing a single thing you need to get started."
    )
    await update.message.reply_text(text=text, reply_markup=open_button())


# =========================
# TRADING PSYCHOLOGY
# =========================

async def trading_psychology(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🧠 The Mental Game Behind Every Trade\n\nFear and greed damage more accounts over "
        "time than any flawed strategy ever could, even one that looked flawless and "
        "reliable on paper before it faced a live market. Staying calm and disciplined "
        "through chaotic, fast-moving markets — especially after a rough losing stretch "
        "that tests your nerve — is what separates consistent traders from the rest.",
        reply_markup=open_button()
    )


# =========================
# PIPS & SPREADS
# =========================

async def pips_spreads(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔢 The Small Numbers That Quietly Drive Every Move\n\nA pip is the smallest standard "
        "unit traders rely on to track gains and losses accurately across several open "
        "positions at once, day after day. The spread is simply the gap between the buy and "
        "sell price, and the tighter that gap stays over time, the more of your own money "
        "stays in your pocket.",
        reply_markup=open_button()
    )


# =========================
# MARKET GAPS
# =========================

async def market_gaps(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🕳️ When Price Jumps Suddenly Instead of Moving Gradually\n\nA market gap happens "
        "when price opens well above or below the previous close, often catching traders "
        "off guard after a weekend break or a major, unscheduled news event. Gaps can "
        "signal genuinely strong momentum building underneath the surface, or they can "
        "simply get \"filled\" as price retraces back toward where it started.",
        reply_markup=open_button()
    )


# =========================
# SUPPORT
# =========================

async def support(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "💬 Support That's Genuinely There Whenever You Need It\n\nSetting up your account, "
        "working through a tough or confusing trade, or just sharing honest feedback about "
        "your experience so far — whatever the reason, our team stays available around the "
        "clock, seven days a week, without exception. Don't hesitate to reach out at any "
        "hour; they're genuinely happy to help, no matter your time zone or how minor the "
        "question feels to you.",
        reply_markup=support_button()
    )


# =========================
# BACKTESTING
# =========================

async def backtesting(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔍 Thoroughly Testing a Strategy Before You Risk Real Money\n\nBacktesting runs a "
        "trading strategy against years of historical price data to see, in reasonably "
        "realistic terms, how it would have performed before you ever put it to genuine use "
        "in a live account. It offers no guarantee of future results, since markets are "
        "always evolving in unpredictable ways, but it remains one of the most reliable ways "
        "to catch weaknesses early.",
        reply_markup=open_button()
    )


# =========================
# TREND FOLLOWING (NEW)
# =========================

async def trend_following(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📈 Trading Steadily With the Market's Overall Direction\n\nTrend following means "
        "deliberately aligning your trades with the market's dominant, established direction "
        "rather than constantly trying to predict every single short-term turn along the "
        "way. It's a patient, disciplined approach — you may miss the very start of a big "
        "move, but in exchange you generally avoid stubbornly fighting the broader momentum.",
        reply_markup=open_button()
    )


# =========================
# LEVERAGE & MARGIN
# =========================

async def leverage_margin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "⚖️ A Genuinely Powerful Tool That Cuts Both Ways at Once\n\nLeverage lets a "
        "relatively modest amount of starting capital control a much larger overall "
        "position in the market, giving you real flexibility to shape a strategy around "
        "your own personal appetite for risk. Just remember this same mechanism amplifies "
        "losses exactly as quickly as it amplifies profits, so every single trade genuinely "
        "needs careful planning well beforehand.",
        reply_markup=open_button()
    )


# =========================
# CENTRAL BANKS
# =========================

async def central_banks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🏦 The Institutions Quietly Behind the Market's Biggest Moves\n\nFew events shake "
        "currency markets quite as hard or as fast as a central bank's rate decision, an "
        "official policy statement, or a sudden, unexpected intervention that catches "
        "everyone off guard. Traders who follow these signals closely, and genuinely "
        "understand the deeper context surrounding them, often spot major moves developing "
        "well before the rest of the crowd.",
        reply_markup=open_button()
    )


# =========================
# ORDER TYPES
# =========================

async def order_types(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎯 Understanding Market, Limit, and Stop Orders Clearly and Fully\n\nA market order "
        "executes immediately at whatever price happens to be current, while limit and stop "
        "orders give you the real power to set your entry or exit well in advance, without "
        "babysitting the screen. Knowing precisely when to reach for each type of order puts "
        "you firmly and confidently in the driver's seat.",
        reply_markup=open_button()
    )


# =========================
# CANDLESTICK PATTERNS
# =========================

async def candlestick_patterns(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🕯️ What a Single Candlestick Is Quietly Telling You\n\nA doji, an engulfing candle, "
        "or a hammer can subtly hint at a coming shift in market momentum long before that "
        "shift ever becomes obvious anywhere else on the chart in front of you. Learning to "
        "spot these small, recurring patterns early adds a genuinely valuable extra layer of "
        "timing to both your entries and your exits.",
        reply_markup=open_button()
    )


# =========================
# BLACK SWAN EVENTS (NEW)
# =========================

async def black_swan_events(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🦢 When the Truly Unexpected Rewrites the Rulebook Overnight\n\nA black swan event "
        "is a rare, largely unpredictable shock — a sudden policy shift, a fast-moving "
        "geopolitical crisis, or an abrupt currency peg break — capable of moving markets "
        "violently within a very short window of time. No strategy fully protects you "
        "against one, but genuinely sound risk management can meaningfully limit the damage "
        "to your account.",
        reply_markup=open_button()
    )


# =========================
# DEMO TRADING
# =========================

async def demo_trading(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎮 Practice Thoroughly Before You Ever Risk a Single Real Dime\n\nA demo account "
        "gives you plenty of room to test out new strategies and get genuinely comfortable "
        "with the platform's tools using virtual funds, all without any real financial "
        "exposure attached. Most experienced, long-term traders strongly recommend spending "
        "real, meaningful time here first, before committing any live capital at all.",
        reply_markup=open_button()
    )


# =========================
# ECONOMIC INDICATORS
# =========================

async def economic_indicators(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📊 When Scheduled Data Releases Send Prices Swinging Fast\n\nA surprise interest "
        "rate move, an inflation report, or a monthly jobs number can jolt currency prices "
        "within a matter of seconds, often with very little advance warning to prepare for "
        "it properly. Staying on top of the economic calendar consistently helps you "
        "anticipate volatility ahead of time, instead of getting caught completely "
        "blindsided.",
        reply_markup=open_button()
    )


# =========================
# POSITION SIZING
# =========================

async def position_sizing(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📏 Why Position Size Genuinely Matters More Than the Idea Itself\n\nHow much you "
        "actually choose to risk on any given trade usually matters more over the long run "
        "than whether the underlying idea itself was particularly good or well-timed to "
        "begin with. Sizing your positions carefully, based on your account balance and "
        "your personal risk tolerance, keeps a single bad trade from doing serious, lasting "
        "damage.",
        reply_markup=open_button()
    )


# =========================
# RISK / REWARD RATIO
# =========================

async def risk_reward_ratio(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "⚖️ Carefully Weighing What You Stand to Gain Against What You Risk\n\nThe "
        "risk-reward ratio compares how much capital you're putting on the line for a given "
        "trade against how much you stand to gain if the setup genuinely plays out the way "
        "you expect it to. A consistently favorable ratio means you can afford to be wrong "
        "more often than you're right and still come out ahead.",
        reply_markup=open_button()
    )


# =========================
# MINOR PAIRS
# =========================

async def minor_pairs(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "💹 Trading Beyond the US Dollar Entirely for a Change\n\nLooking for genuine "
        "exposure to other major world economies without having the US dollar sitting on "
        "the other side of every single position you take on? Pairs like EUR/GBP and "
        "AUD/JPY make that entirely possible, directly and reliably, and they also tend to "
        "be noticeably less crowded than the busiest major pairs.",
        reply_markup=open_button()
    )


# =========================
# TRADING JOURNAL
# =========================

async def trading_journal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📝 The Small Daily Habit With a Surprisingly Big Long-Term Payoff\n\nLogging every "
        "entry, exit, and the actual reasoning behind each trade — along with exactly how "
        "it eventually played out in practice — turns your scattered, day-to-day trading "
        "experience into something you can genuinely study and build on. Traders who review "
        "their journal on a consistent, regular basis tend to catch recurring mistakes much "
        "faster.",
        reply_markup=open_button()
    )


# =========================
# COMMODITY CURRENCIES
# =========================

async def commodity_currencies(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🛢️ When Currencies Move Closely in Step With Commodities\n\nThe Canadian dollar, "
        "Australian dollar, and Norwegian krone often move in step with real-world "
        "commodities like oil, gold, and natural gas across extended stretches of time and "
        "shifting market cycles. Watching broader commodity trends closely can give you a "
        "genuinely useful edge in forecasting where these particular currencies might "
        "realistically head next.",
        reply_markup=open_button()
    )


# =========================
# TRADING STRATEGIES
# =========================

async def trading_strategies(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📈 Finding the Trading Style That Genuinely Fits Your Life\n\nScalping, day "
        "trading, swing trading, and longer-term position trading each demand a very "
        "different amount of time, patience, and personal risk tolerance from the trader "
        "attempting them. The goal isn't blindly chasing whatever style happens to be "
        "trending online — it's finding the steady rhythm that fits you and your schedule.",
        reply_markup=open_button()
    )


# =========================
# COPY TRADING
# =========================

async def copy_trading(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👥 Learning the Ropes by Closely Watching Others Trade Live\n\nCopy trading lets "
        "you mirror the live trades of more experienced traders in real time, offering a "
        "genuinely hands-on way to learn the ropes while still staying actively involved "
        "yourself. It's certainly not a guaranteed shortcut to profit, since your overall "
        "results still depend heavily on who you personally choose to follow.",
        reply_markup=open_button()
    )


# =========================
# TECHNICAL ANALYSIS
# =========================

async def technical_analysis(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📉 Turning Raw Charts Into Genuinely Useful, Actionable Signals\n\nSupport and "
        "resistance zones, moving averages, and candlestick patterns often hint at where "
        "price is realistically headed well before the actual move ever fully plays out on "
        "the chart in front of you. Mastering this visual language over time gradually "
        "turns trading from pure guesswork into a structured, repeatable process you can "
        "rely on.",
        reply_markup=open_button()
    )


# =========================
# SUPPORT & RESISTANCE (NEW)
# =========================

async def support_resistance(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📊 The Price Levels the Market Keeps Reacting To\n\nSupport and resistance are "
        "price zones where buying or selling pressure has repeatedly stepped in before, "
        "making them genuinely useful reference points for entries, exits, and stop "
        "placement alike. The more times a level gets tested without actually breaking, the "
        "more closely traders across the market tend to watch it going forward.",
        reply_markup=open_button()
    )


# =========================
# FOREX TRADING
# =========================

async def forex_trading(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "💱 A Global Market That Genuinely Never Stops Moving\n\nForex runs a full 24 hours "
        "a day, seven days a week, as trading sessions overlap continuously across nearly "
        "every time zone on the planet without any true pause at all. With trillions of "
        "dollars changing hands daily across the globe, there's usually some real "
        "opportunity sitting on the table for anyone paying close attention.",
        reply_markup=open_button()
    )


# =========================
# DRAWDOWN MANAGEMENT
# =========================

async def drawdown_management(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📉 Staying Steady and Composed Through a Genuinely Rough Drawdown\n\nA drawdown — "
        "the decline from an account's peak value down to its lowest point before "
        "eventually recovering — is a completely normal part of trading, not necessarily a "
        "sign that something has gone seriously wrong. Handling it well ultimately comes "
        "down to sizing your trades sensibly and knowing well in advance how much of a dip "
        "you can genuinely tolerate.",
        reply_markup=open_button()
    )


# =========================
# LIQUIDITY EXPLAINED
# =========================

async def liquidity_explained(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "💧 The Quiet Force Sitting Behind Every Single Trade You Place\n\nHow easily a "
        "currency pair can be bought or sold without causing a noticeable shift in price "
        "depends heavily on liquidity, which tends to run considerably deeper in the major "
        "pairs than almost anywhere else. Trading during genuinely thin liquidity "
        "conditions often brings wider spreads and unexpected slippage that's well worth "
        "watching closely.",
        reply_markup=open_button()
    )


# =========================
# CARRY TRADE
# =========================

async def carry_trade(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "💰 Steadily Earning the Spread With Carry Trades Over Time\n\nThe carry trade "
        "strategy works by borrowing in a currency with a low interest rate and holding a "
        "position in one offering a meaningfully higher rate, letting you pocket that rate "
        "difference alongside whatever price movement happens along the way. It suits "
        "patient, long-term traders best, though a sudden rate change can flip the trade "
        "against you fast.",
        reply_markup=open_button()
    )


# =========================
# TRADING DISCIPLINE
# =========================

async def trading_discipline(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎯 Holding the Line When It's Genuinely Hardest to Do So\n\nDiscipline means "
        "sticking closely to your trading plan and your predefined risk rules even when raw "
        "emotion is pushing you hard to deviate from them, especially right after a painful "
        "loss or one unusually large win. Long-term traders aren't immune to that same "
        "pull; they simply train themselves to consistently choose not to act on the "
        "impulse.",
        reply_markup=open_button()
    )


# =========================
# OVERTRADING
# =========================

async def overtrading(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🚫 Recognizing When It's Genuinely Time to Step Back\n\nOvertrading happens when a "
        "trader keeps opening new positions out of boredom, impatience, or a rushed desire "
        "to recover recent losses, rather than acting on a genuine, well-planned setup "
        "that's actually worth taking. Recognizing these warning signs early helps protect "
        "both your trading account and your long-term decision-making from unnecessary, "
        "avoidable damage.",
        reply_markup=open_button()
    )


# =========================
# CHART PATTERNS
# =========================

async def chart_patterns(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📐 Reading Triangles, Flags, and Head-and-Shoulders Well Ahead of Time\n\nBeyond "
        "individual candlesticks, broader chart formations like head-and-shoulders, "
        "triangles, and flags can often hint at a coming breakout or a sharp reversal well "
        "before it ever fully unfolds on the chart in front of you. Catching these patterns "
        "early, well ahead of the wider trading crowd, adds a genuinely useful extra layer "
        "of insight.",
        reply_markup=open_button()
    )


# =========================
# VOLATILITY EXPLAINED
# =========================

async def volatility_explained(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📊 Understanding Market Volatility Before It Ever Catches You Off Guard\n\n"
        "Volatility measures how sharply and how frequently price moves over a given "
        "stretch of time, and higher volatility usually brings the potential for bigger "
        "gains right alongside the risk of noticeably bigger losses. Knowing a currency "
        "pair's typical volatility ahead of time helps you set realistic stop-loss "
        "distances and avoid getting shaken out too early.",
        reply_markup=open_button()
    )


# =========================
# MAJOR PAIRS
# =========================

async def major_pairs(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🌍 Where the Bulk of Global Trading Volume Actually Lives\n\nEUR/USD, GBP/USD, and "
        "USD/JPY dominate the bulk of daily trading volume across the globe, and that's "
        "really no accident once you consider the sheer size and strength of the economies "
        "standing behind them. These pairs consistently offer deep liquidity, tighter "
        "spreads, and price action that's generally far easier and more predictable to "
        "read.",
        reply_markup=open_button()
    )


# =========================
# MARKET SENTIMENT
# =========================

async def market_sentiment(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🌡️ Reading the Market's Overall Mood Carefully Before You Trade\n\nMarket "
        "sentiment reflects whether traders as a whole are broadly leaning bullish or "
        "bearish on a given pair, often shaped by recent news, positioning data, and prior "
        "price action across the session. Gauging sentiment alongside your own technical "
        "and fundamental analysis can help confirm — or seriously challenge — the trade "
        "idea you're currently considering.",
        reply_markup=open_button()
    )


# =========================
# FIBONACCI RETRACEMENT
# =========================

async def fibonacci_retracement(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🌀 Mapping Likely Pullback Zones With Fibonacci Levels Carefully\n\nFibonacci "
        "retracement levels help highlight the zones where a price pullback might "
        "realistically pause or reverse before the underlying trend eventually resumes its "
        "original path forward once again. They're never a guarantee of exactly where price "
        "goes next, but they still give you clear, well-defined zones worth watching "
        "closely when mapping out entries and exits.",
        reply_markup=open_button()
    )


# =========================
# EXOTIC PAIRS
# =========================

async def exotic_pairs(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🌏 Higher Risk, Potentially Higher Reward With Exotic Currency Pairs\n\nCurrencies "
        "from smaller, developing economies scattered around the world tend to swing more "
        "sharply and unpredictably than the majors do — which is precisely their appeal to "
        "certain, more risk-tolerant traders out there. That added volatility is genuinely "
        "a double-edged sword, but it also creates opportunities the established major "
        "pairs rarely offer in practice.",
        reply_markup=open_button()
    )


# =========================
# TIMEFRAMES
# =========================

async def timeframes(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "⏱️ Picking a Chart Timeframe That Genuinely Matches Your Style\n\nFast-paced "
        "traders often gravitate naturally toward 1-minute or 5-minute charts for quick, "
        "in-and-out style trading, while a more patient, methodical approach tends to fit "
        "better on daily or weekly timeframes instead. Matching your timeframe carefully to "
        "both your strategy and your daily schedule makes a genuinely real difference in "
        "your overall results.",
        reply_markup=open_button()
    )


# =========================
# RISK MANAGEMENT
# =========================

async def risk_management(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🛡️ Guard Your Capital Carefully Before Chasing Bigger Gains\n\nStop-loss and "
        "take-profit orders quietly protect your account around the clock, freeing you up "
        "to focus more on strategy instead of nervously watching every single price tick "
        "with constant, anxious attention. The traders who stick around for years, rather "
        "than burning out early, are almost always the ones who treat risk management as a "
        "genuine, ongoing priority.",
        reply_markup=open_button()
    )


# =========================
# SLIPPAGE
# =========================

async def slippage(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "⚡ Why Your Fill Price Isn't Always the Price You Originally Expected\n\nSlippage "
        "occurs when a trade ends up filling at a different price than originally planned, "
        "most often during fast-moving markets or right after a major piece of news hits "
        "unexpectedly hard. It can work in your favor just as easily as against you, but "
        "understanding the mechanics behind it makes planning your entries and exits far "
        "more realistic.",
        reply_markup=open_button()
    )


# =========================
# CURRENCY CORRELATIONS
# =========================

async def currency_correlations(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔗 How Currency Pairs Move in Tandem — or Don't at All\n\nCertain currency pairs "
        "tend to move almost perfectly in sync with each other over extended periods of "
        "time and shifting conditions, while others reliably and consistently head in "
        "nearly opposite directions without much noticeable deviation. Understanding these "
        "underlying relationships helps you avoid unknowingly stacking the exact same risk "
        "across what looks like several different trades.",
        reply_markup=open_button()
    )


# =========================
# NEWS TRADING
# =========================

async def news_trading(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📰 Navigating Big News Events Wisely and Genuinely Without Panic\n\nEmployment "
        "data, inflation reports, and central bank announcements can all spark sudden, "
        "sharp price swings within seconds that catch completely unprepared traders off "
        "guard without much real warning beforehand. Planning carefully ahead of these "
        "scheduled releases, rather than scrambling to react afterward, puts you in a "
        "noticeably stronger position every single time.",
        reply_markup=open_button()
    )


# =========================
# TRADING TOOLS
# =========================

async def trading_tools(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🛠️ The Everyday Toolkit for Serious, Committed Traders Alike\n\nA full range of "
        "technical indicators, live interactive charts, and a fast, clean, responsive "
        "interface all put everything you could realistically need well within easy reach "
        "at any given moment during the trading day. Every single tool here is genuinely "
        "built to help you react quickly and confidently to shifting market conditions as "
        "they unfold.",
        reply_markup=open_button()
    )


# =========================
# TRADING PLAN
# =========================

async def trading_plan(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📋 A Written Plan That Genuinely Holds Up Under Real Pressure\n\nClear entries, "
        "exits, risk limits, and precisely defined trading conditions all belong spelled "
        "out in a solid, written trading plan, cutting down significantly on guesswork once "
        "things start moving fast and unpredictably. Traders who consistently stick to a "
        "written plan tend to make far fewer impulsive decisions when markets suddenly turn "
        "chaotic around them.",
        reply_markup=open_button()
    )


# =========================
# SETUP MENU COMMANDS
# =========================

async def setup_commands(app):
    commands = [
        ("start",                  "Start Bot"),
        ("trading_psychology",     "Trading Psychology"),
        ("pips_spreads",           "Pips & Spreads"),
        ("market_gaps",            "Market Gaps"),
        ("support",                "Help & Support"),
        ("backtesting",            "Backtesting"),
        ("trend_following",        "Trend Following"),
        ("leverage_margin",        "Leverage & Margin"),
        ("central_banks",          "Central Banks"),
        ("order_types",            "Order Types"),
        ("candlestick_patterns",   "Candlestick Patterns"),
        ("black_swan_events",      "Black Swan Events"),
        ("demo_trading",           "Demo Trading"),
        ("economic_indicators",    "Economic Indicators"),
        ("position_sizing",        "Position Sizing"),
        ("risk_reward_ratio",      "Risk/Reward Ratio"),
        ("minor_pairs",            "Minor Pairs"),
        ("trading_journal",        "Trading Journal"),
        ("commodity_currencies",   "Commodity Currencies"),
        ("trading_strategies",     "Trading Strategies"),
        ("copy_trading",           "Copy Trading"),
        ("technical_analysis",     "Technical Analysis"),
        ("support_resistance",     "Support & Resistance"),
        ("forex_trading",          "Forex Trading"),
        ("drawdown_management",    "Drawdown Management"),
        ("liquidity_explained",    "Liquidity Explained"),
        ("carry_trade",            "Carry Trade"),
        ("trading_discipline",     "Trading Discipline"),
        ("overtrading",            "Overtrading"),
        ("chart_patterns",         "Chart Patterns"),
        ("volatility_explained",   "Volatility Explained"),
        ("major_pairs",            "Major Pairs"),
        ("market_sentiment",       "Market Sentiment"),
        ("fibonacci_retracement",  "Fibonacci Retracement"),
        ("exotic_pairs",           "Exotic Pairs"),
        ("timeframes",             "Chart Timeframes"),
        ("risk_management",        "Risk Management"),
        ("slippage",               "Slippage"),
        ("currency_correlations",  "Currency Correlations"),
        ("news_trading",           "News Trading"),
        ("trading_tools",          "Trading Tools & Charts"),
        ("trading_plan",           "Trading Plan"),
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

app.add_handler(CommandHandler("start",                  start))
app.add_handler(CommandHandler("trading_psychology",      trading_psychology))
app.add_handler(CommandHandler("pips_spreads",             pips_spreads))
app.add_handler(CommandHandler("market_gaps",              market_gaps))
app.add_handler(CommandHandler("support",                  support))
app.add_handler(CommandHandler("backtesting",              backtesting))
app.add_handler(CommandHandler("trend_following",          trend_following))
app.add_handler(CommandHandler("leverage_margin",          leverage_margin))
app.add_handler(CommandHandler("central_banks",            central_banks))
app.add_handler(CommandHandler("order_types",              order_types))
app.add_handler(CommandHandler("candlestick_patterns",     candlestick_patterns))
app.add_handler(CommandHandler("black_swan_events",        black_swan_events))
app.add_handler(CommandHandler("demo_trading",              demo_trading))
app.add_handler(CommandHandler("economic_indicators",       economic_indicators))
app.add_handler(CommandHandler("position_sizing",           position_sizing))
app.add_handler(CommandHandler("risk_reward_ratio",         risk_reward_ratio))
app.add_handler(CommandHandler("minor_pairs",                minor_pairs))
app.add_handler(CommandHandler("trading_journal",            trading_journal))
app.add_handler(CommandHandler("commodity_currencies",       commodity_currencies))
app.add_handler(CommandHandler("trading_strategies",         trading_strategies))
app.add_handler(CommandHandler("copy_trading",                copy_trading))
app.add_handler(CommandHandler("technical_analysis",          technical_analysis))
app.add_handler(CommandHandler("support_resistance",          support_resistance))
app.add_handler(CommandHandler("forex_trading",                forex_trading))
app.add_handler(CommandHandler("drawdown_management",          drawdown_management))
app.add_handler(CommandHandler("liquidity_explained",          liquidity_explained))
app.add_handler(CommandHandler("carry_trade",                   carry_trade))
app.add_handler(CommandHandler("trading_discipline",            trading_discipline))
app.add_handler(CommandHandler("overtrading",                    overtrading))
app.add_handler(CommandHandler("chart_patterns",                 chart_patterns))
app.add_handler(CommandHandler("volatility_explained",           volatility_explained))
app.add_handler(CommandHandler("major_pairs",                     major_pairs))
app.add_handler(CommandHandler("market_sentiment",                market_sentiment))
app.add_handler(CommandHandler("fibonacci_retracement",           fibonacci_retracement))
app.add_handler(CommandHandler("exotic_pairs",                     exotic_pairs))
app.add_handler(CommandHandler("timeframes",                       timeframes))
app.add_handler(CommandHandler("risk_management",                  risk_management))
app.add_handler(CommandHandler("slippage",                          slippage))
app.add_handler(CommandHandler("currency_correlations",             currency_correlations))
app.add_handler(CommandHandler("news_trading",                       news_trading))
app.add_handler(CommandHandler("trading_tools",                      trading_tools))
app.add_handler(CommandHandler("trading_plan",                       trading_plan))


# =========================
# START BOT
# =========================

print("✅ Forex Bot Running...")
app.run_polling()