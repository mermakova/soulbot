import helpers.rmq_helper as q_helper
import configs.config as conf
import helpers.tlg_helper as tlg

# TODO: log it!
bot = tlg.BotHelper(conf.TOKEN)


def on_message(ch, method, properties, body):
    print(" [x] Received %r" % body)
    msg = tlg.Messaging(conf.TOKEN, body)
    if msg.get_command() is not None:
        print(msg.get_command())
        msg.command_execute(msg.get_command())
        return 0
    result = bot.sendMessage(msg._chat_id, msg.get_text())
    return result


if __name__ == '__main__':
    queue_handler = q_helper.QueueHelper(conf.QUEUE_NAME)
    queue_handler.consume_message(on_message)
    queue_handler._channel.start_consuming()
