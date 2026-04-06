import os
import telebot
import subprocess

# جلب التوكن من إعدادات GitHub Secrets
TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'run'])
def run_tool(message):
    bot.reply_to(message, "🚀 جاري تشغيل الأداة... انتظر لحظة.")
    try:
        # تشغيل ملفك المشفر
        # تأكد أن اسم الملف مطابق تماماً للمرفوع
        result = subprocess.run(['python', 'سبام تليجرام.py_Enc.py'], capture_output=True, text=True)
        
        # إرسال النتيجة (إذا كانت الأداة تطبع مخرجات في الكونسول)
        if result.stdout:
            bot.send_message(message.chat.id, f"✅ المخرجات:\n{result.stdout}")
        else:
            bot.send_message(message.chat.id, "✅ تم التنفيذ بنجاح (لا توجد مخرجات نصية).")
            
    except Exception as e:
        bot.reply_to(message, f"❌ حدث خطأ أثناء التشغيل: {str(e)}")

bot.polling()
