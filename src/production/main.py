from channel.kafka_consumer import KafkaConsumer
from service.base_production_line_service import BaseProductionLineService

production = BaseProductionLineService("Packaging")

consumer = KafkaConsumer(broker="kafka:9092", 
                         topic="order-topic", callback_function=production.start_production_line)

consumer.consume_messages()