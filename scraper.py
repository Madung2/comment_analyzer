import googleapiclient.discovery
import googleapiclient.errors
import environ

# Set up environment variables
env = environ.Env()
# Reading .env file
environ.Env.read_env()

api_service_name = "youtube"
api_version = "v3"
SECRET_KEY = env.str('SECRET_KEY', '!!! SET YOUR SECRET_KEY !!!')
print('SECRET_KEY', SECRET_KEY)

youtube = googleapiclient.discovery.build(
    api_service_name, api_version, developerKey=SECRET_KEY
)

request = youtube.commentThreads().list(
    part="snippet",
    videoId="",
    maxResults=100
)

response=request.execute()

for item in response['items']:
    print(item['snippet']['topLevelComment']['snippet']['textDisplay'])
