from unittest.mock import MagicMock, patch
from order_publisher.publisher import Publisher

import pytest
from credit_risk_lib.config.config import Config


@pytest.fixture
def mock_config() -> Config:
    return MagicMock(spec=Config)


def test_initialization(mock_config: Config):  # TODO: Fix this test
    mock_config.project_id = "test_project"
    mock_config.topic_id = "test_topic"

    with patch("credit_risk_lib.config.config_factory.ConfigFactory.get_conf", return_value= mock_config):
        with patch("google.cloud.pubsub_v1.PublisherClient") as mock_pubsub_client:
            mock_pubsub_client_instance = mock_pubsub_client.return_value
            mock_pubsub_client_instance.topic_path.return_value = "projects/test_project/topics/test_topic"

            publisher = Publisher(r"src/order_publisher/publisher_conf.json")

            mock_pubsub_client_instance.topic_path.assert_called_with("test_project", "test_topic")
            assert publisher._topic_path == "projects/test_project/topics/test_topic"


def test_configuration_file_not_found():
    with patch("credit_risk_lib.config.config_factory.ConfigFactory.get_conf", side_effect=ValueError("Configuration file not found")):
        with pytest.raises(ValueError):
            Publisher("path/to/nonexistent/config/file")
