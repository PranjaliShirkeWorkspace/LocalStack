import boto3


class SNSService:
    """SNS service API implementations"""

    def __init__(self) -> None:
        super().__init__()
        self._endpoint_url = "http://localhost:4566"
        self._sns_client = boto3.client('sns', region_name='us-west-2', endpoint_url=self._endpoint_url)

    def create_topic(self, topic_name):
        """Creates topic"""
        resp = self._sns_client.create_topic(Name=topic_name)
        return resp["TopicArn"]

    def list_topic(self):
        """Lists topics"""
        resp = self._sns_client.list_topics()
        return resp["Topics"]

    def delete_topics(self, topic_name):
        """ Deletes topic"""
        self._sns_client.delete_topic(TopicArn=topic_name)

    def add_subscription(self, topic_arn, protocol, subscription_endpoint):
        """ Add subscription to topic """
        resp = self._sns_client.subscribe(TopicArn=topic_arn, Protocol=protocol,
                                          Endpoint=subscription_endpoint)
        return resp["SubscriptionArn"]

    def list_subscription(self):
        """ lists subscriptions"""
        resp = self._sns_client.list_subscriptions()
        return resp["Subscriptions"]

