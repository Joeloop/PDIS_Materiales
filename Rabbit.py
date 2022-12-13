import pika


class Rabbit:

    connection = None
    channel = None

    def __init__(self):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost'))
        self.channel = self.connection.channel()

    def publish(self, message: str, exchange: str):
        self.channel.exchange_declare(exchange=exchange, exchange_type='fanout')
        self.channel.basic_publish(exchange=exchange, routing_key='', body=message)
        print(" [x] Sent %r\nto %s exchange" % (message, exchange))

    def consume(self, exchange: str):
        self.channel.exchange_declare(exchange=exchange, exchange_type='fanout')

        result = self.channel.queue_declare(queue='', exclusive=True, durable=True, auto_delete=True)
        queue_name = result.method.queue

        self.channel.queue_bind(exchange=exchange, queue=queue_name)
        self.channel.basic_consume(
            queue=queue_name, on_message_callback=self.callback, auto_ack=True)

        print(" [*] Started %s exchange" % exchange)
        self.channel.start_consuming()

    @staticmethod
    def callback(ch, method, properties, body):

        print(" [x] %r" % body)
