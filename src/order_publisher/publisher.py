from pydantic import BaseModel
from credit_risk_lib.config.config import Config
from credit_risk_lib.config.config_factory import ConfigFactory 
import json

from google.cloud.pubsub_v1 import PublisherClient


class Publisher:
    def __init__(self, publisher_conf_path: str, publisher_conf_schema: BaseModel = None):
        """Initializes the Publisher with configuration settings and sets up the topic path for event publishing.

        Args:
            publisher_conf_path (str): The file path to the publisher configuration.
            publisher_conf_schema (BaseModel, optional): The schema to validate the configuration against. Defaults to None.
        """
        self._conf: Config = ConfigFactory.get_conf(publisher_conf_path, publisher_conf_schema)
        self._event_publisher = PublisherClient()
        self._topic_path = self._event_publisher.topic_path(self._conf.project_id, self._conf.topic_id)
    
    
    def publish(self, message: dict):
        """Publishes a message to the configured topic.

        Args:
            message (dict): The message to be published, structured as a dictionary. It will be serialized to JSON.

        Returns:
            Any: The result of the publish operation, returned after successful completion or timeout.
        """
        message = json.dumps(message).encode("utf-8")
        future = self._event_publisher.publish(self._topic_path, message)
        return future.result(timeout=60)