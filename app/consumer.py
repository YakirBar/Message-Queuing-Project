import pika

# Callback function to handle received messages
def callback(ch, method, properties, body):
    print(f" [x] Received {body.decode()}")

# Connection parameters with admin credentials
credentials = pika.PlainCredentials('admin', 'secret')
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', 5672, '/', credentials))
channel = connection.channel()

# Declare the same queue to ensure it exists
channel.queue_declare(queue='hello')

# Set up subscription on the queue
channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')

# Start consuming (waiting for messages)
channel.start_consuming()
