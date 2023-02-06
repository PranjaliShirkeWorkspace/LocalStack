from MockedServices.S3 import S3Storage
from MockedServices.SSM import SSMService
from MockedServices.SNS import SNSService


if __name__ == "__main__":
    """S3 services"""
    s3 = S3Storage()
    s3.create_s3_bucket("sample-test2")
    s3.upload_to_aws('test-image.jpg', 'sample-test2', 'test-image2.jpg')
    print(s3.list_buckets())
    print(s3.list_data_in_bucket('sample-test2'))

    """SSM services"""
    ssm = SSMService()
    print(ssm.put_ssm_parameter("test2", "Hello", "String"))
    print(ssm.get_ssm_parameter("test2"))
    print(ssm.put_ssm_parameter("AccessKey", "123456789", "SecureString"))
    print(ssm.get_ssm_parameter("AccessKey"))
    print(ssm.get_ssm_parameter("AccessKey", True))

    """SNS services"""
    sns = SNSService()
    print(sns.create_topic("LocalStack"))
    print(sns.list_topic())
    print(sns.add_subscription("arn:aws:sns:us-west-2:000000000000:LocalStack", "email", "testuser@email.com"))
    print(sns.list_subscription())
