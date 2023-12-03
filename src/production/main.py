from subscriber.mqtt_subscriber import MQTTSubscriber
from service.production_line import BaseProductionLineService

production = BaseProductionLineService("Packaging")

mqtt_subscriber = MQTTSubscriber(broker="mosquitto",
                                  topic="order-topic",
                                  callback_function=production.start_production_line)

mqtt_subscriber.consume_messages()