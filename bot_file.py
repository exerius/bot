from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="""This is a simple scheduler bot. The following commands can be used:
/schedule <task> — adds task to the task list
/list — writes down list of all of the task added y previous command
/done <number> — marks chosen task as completed.
""")


async def schedule(update: Update, context: ContextTypes.DEFAULT_TYPE):
    task = update.message.text.replace("/schedule ", "")
    tasks.append([task, False])
    await update.message.reply_text(f"Task {task} is saved.")


async def list_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    report = ""
    for i in range(len(tasks)):
        report += f"{i + 1}. {tasks[i][0]} | {'Done' if tasks[i][1] else 'Not done'}\n"
    await update.message.reply_text(report)


async def do(update: Update, context: ContextTypes.DEFAULT_TYPE):
    tasks[int(context.args[0]) - 1][1] = True
    await update.message.reply_text(f"Task {context.args[0]} is completed! Congratulations!")


if __name__ == '__main__':
    tasks = []
    application = ApplicationBuilder().token('7301016466:AAF2Cd-ktxIcup6iYS-GCu4mwlsmKCDoB5k').build()

    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)
    application.add_handler(CommandHandler("schedule", schedule))
    application.add_handler(CommandHandler("list", list_handler))
    application.add_handler(CommandHandler("done", do))
    application.run_polling()
