from pydantic import BaseModel
from credit_risk_lib.config.config import Config
from credit_risk_lib.config.config_factory import ConfigFactory 
import json

from google.cloud.pubsub_v1 import PublisherClient


class Publisher:
    def __init__(self, publisher_conf_path: str, publisher_conf_schema: BaseModel = None):
        self._conf: Config = ConfigFactory.get_conf(publisher_conf_path, publisher_conf_schema)
        self._event_publisher = PublisherClient()
        self._topic_path = self._event_publisher.topic_path(self._conf.project_id, self._conf.topic_id)
    
    
    def publish(self, message: dict):
        message = json.dumps(message).encode("utf-8")
        future = self._event_publisher.publish(self._topic_path, message)
        return future.result()