import boto3


class SSMService:
    """SSM API Implementation"""

    def __init__(self) -> None:
        super().__init__()
        self._endpoint_url = "http://localhost:4566"
        self._ssm_client = boto3.client('ssm', region_name='us-west-2', endpoint_url=self._endpoint_url)

    def put_ssm_parameter(self, parameter_name, parameter_value, parameter_type, overwrite=True):
        """Storing ssm parameters"""

        response = self._ssm_client.put_parameter(
            Name=parameter_name,
            Value=parameter_value,
            Type=parameter_type,
            Overwrite=overwrite
        )
        return response

    def get_ssm_parameter(self, parameter_name, decrypt=False):
        """ retrieving ssm parameters"""

        response = self._ssm_client.get_parameter(
            Name=parameter_name,
            WithDecryption=decrypt)
        return response
