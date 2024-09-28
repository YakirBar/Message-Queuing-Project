import pika

# Connection parameters with admin credentials
credentials = pika.PlainCredentials('admin', 'secret')
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', 5672, '/', credentials))
channel = connection.channel()

# Declare a queue for sending messages
channel.queue_declare(queue='hello')

# Publish a message to the queue
message = "Hello, RabbitMQ with Authentication!"
channel.basic_publish(exchange='', routing_key='hello', body=message)

print(f" [x] Sent '{message}'")

# Close the connection
connection.close()
