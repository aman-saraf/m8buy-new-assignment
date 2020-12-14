import boto3

class SecretService:

    def getSecretValue(self, secretName):
        client = boto3.client('ssm')
        response = client.get_parameter(Name=secretName, WithDecryption=True)
        return response['Parameter']['Value']