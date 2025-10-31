# ==========================================
# 🤖 جزوه پلاس - نسخه مخصوص اندروید (Pydroid3)
# پاسخ‌دهی خودکار به نام جزوه‌ها با لینک‌ها
# ==========================================

from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

# ===========================
# 🔹 اینجا توکن ربات خودت رو بذار
# مثال: "8333731852:AAGeN5c8DU6sWY4PdEXOyXleyfqd4XFYb90"
# ===========================
BOT_TOKEN = "8333731852:AAGeN5c8DU6sWY4PdEXOyXleyfqd4XFYb90"

# ===========================
# 📚 لیست جزوه‌ها (اسم => لینک)
# ===========================
JOZVE_DICT = {
    "مدار ۲ میانترم": "https://t.me/sutbasic1399/10080",
    "شیمی عمومی ۱ مکی آبادی": "https://t.me/sutbasic1399/10079",
    "سیستم ۱": "https://t.me/sutbasic1399/10021",
    "تکنولوژی بتن": "https://t.me/sutbasic1399/9875?single",
    "فیزیک ۲ راستگو": "https://t.me/sutbasic1399/9818?single",
    "اقتصاد مهندسی انصاریان": "https://t.me/sutbasic1399/9082",
    "آمار شهریاری": "https://t.me/sutbasic1399/9391",
    "مدارهای الکتریکی ۲": "https://t.me/sutbasic1399/9305",
    "الکترومغناطیس ۱۴۰۴": "https://t.me/sutbasic1399/9102",
    "استاتیک جهانشاهی": "https://t.me/sutbasic1399/9085",
    "فیزیک ۲ راستگو (نسخه قدیمی)": "https://t.me/sutbasic1399/9034",
    "آمار و احتمال مهندسی شهریاری": "https://t.me/sutbasic1399/9033",
    "محیط زیست": "https://t.me/sutbasic1399/9014",
    "الکترومغناطیس برزگر": "https://t.me/sutbasic1399/8965?single",
    "الکترونیک ۱ برزگر": "https://t.me/sutbasic1399/8950",
    "علم و مواد": "https://t.me/sutbasic1399/8949",
    "معادلات دیفرانسیل احمدی": "https://t.me/sutbasic1399/8868",
    "ریاضی ۲ محمدی": "https://t.me/sutbasic1399/8821",
    "ماشین الکتریکی ۱ مرادی": "https://t.me/sutbasic1399/8298",
    "شیمی عمومی مرتضوی": "https://t.me/sutbasic1399/8284",
    "شیمی عمومی یار احمدی": "https://t.me/sutbasic1399/8283",
    "ریاضی ۲ برفه ای": "https://t.me/sutbasic1399/8249",
    "محاسبات عددی برفه ای": "https://t.me/sutbasic1399/8248?single",
    "مدار الکتریکی ۱ دهیادگاری": "https://t.me/sutbasic1399/8203",
    "فیزیک ۲ انصاریان": "https://t.me/sutbasic1399/8202",
    "فیزیک ۲ راستگو (نسخه قدیمی 2)": "https://t.me/sutbasic1399/8196",
    "فیزیک ۱ راستگو": "https://t.me/sutbasic1399/8195",
    "مبانی علوم ریاضی میرحسین خانی": "https://t.me/sutbasic1399/8119",
    "الکترونیک ۱": "https://t.me/sutbasic1399/8109",
    "الکترومغناطیس راستگو": "https://t.me/sutbasic1399/8098",
    "مبانی آنالیز ریاضی دهقانان": "https://t.me/sutbasic1399/8097?single",
    "ریاضی ۲ افشار": "https://t.me/sutbasic1399/8084?single",
    "مبانی ماتریس و جبر خطی محمد حسنی": "https://t.me/sutbasic1399/8028",
    "ریاضی ۲ بارچی": "https://t.me/sutbasic1399/7943",
    "محاسبات عددی احمدی": "https://t.me/sutbasic1399/7918",
    "آمار و احتمال محمودی نژاد": "https://t.me/sutbasic1399/7546",
    "مبانی کامپیوتر دوماری": "https://t.me/sutbasic1399/7545",
    "ریاضی مهندسی آخوندی": "https://t.me/sutbasic1399/7467",
    "آمار مهندسی محمودی نژاد": "https://t.me/sutbasic1399/7238",
    "آز فیزیک ۱ خضری": "https://t.me/sutbasic1399/7231?single",
    "ریاضی ۱ پورمختار": "https://t.me/sutbasic1399/7222",
    "ریاضی ۱ محمدی": "https://t.me/sutbasic1399/7138",
    "برنامه نویسی خزاعی": "https://t.me/sutbasic1399/7062",
    "برنامه نویسی بهرام نژاد": "https://t.me/sutbasic1399/7061",
    "سیگنال ها و سیستم": "https://t.me/sutbasic1399/7028",
    "معادلات افشار": "https://t.me/sutbasic1399/7027?single",
    "مدار الکتریکی ۲ (نسخه قدیمی)": "https://t.me/sutbasic1399/7022",
    "فیزیک ۲ نصیری مقدم": "https://t.me/sutbasic1399/6917",
    "مبانی اقتصاد حسینی فر": "https://t.me/sutbasic1399/6292",
    "فیزیک ۲ محمدی": "https://t.me/sutbasic1399/6119",
    "ترمودینامیک ۲": "https://t.me/sutbasic1399/6041",
}

# ===========================
# 📩 منطق پاسخ‌دهی ربات
# ===========================
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message
    if not msg or not msg.text:
        return

    text = msg.text.strip()
    if text in JOZVE_DICT:
        link = JOZVE_DICT[text]
        reply = f"📚 جزوه: {text}\n\n📎 لینک: {link}"
        await msg.reply_text(reply)
    else:
        await msg.reply_text(
            "❌ این اسم جزوه ثبت نشده.\n"
            "لطفاً اسم جزوه را دقیق بنویس (مثلاً: فیزیک ۲ انصاریان)"
        )

# ===========================
# 🚀 اجرای ربات (سازگار با اندروید)
# ===========================
if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("✅ جزوه پلاس فعال شد. (برای توقف Ctrl+C بزن)")
    app.run_polling()
