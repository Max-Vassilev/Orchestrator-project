import boto3
from src.graphql.user_model import User
from dotenv import load_dotenv
import os

load_dotenv()

AWS_REGION = os.getenv('AWS_REGION')
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')

dynamodb = boto3.resource(
    'dynamodb',
    region_name=AWS_REGION,
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
)

users_table = dynamodb.Table('Users')

def get_all_users_from_dynamodb() -> list[User]:
    response = users_table.scan()
    return [User(Name=item['Name'], Email=item['Email']) for item in response['Items']]
