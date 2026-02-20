import json
from livekit import api
import os

LIVEKIT_URL = os.environ.get("LIVEKIT_URL", "wss://clawd-du70h79g.livekit.cloud")
LIVEKIT_API_KEY = os.environ.get("LIVEKIT_API_KEY", "APIMb93GV3fqLwr")
LIVEKIT_API_SECRET = os.environ.get("LIVEKIT_API_SECRET", "5K9wvpoIf0t3K8M3JfcTWTbIYKpMlhb7xf0i99NpaNBA")

def handler(req):
    try:
        body = req.get_body()
        if body:
            data = json.loads(body)
        else:
            data = {}
    except:
        data = {}
    
    identity = data.get('identity', f'user-{id(req)}')
    room_name = data.get('room', 'voice-room')
    
    # Create token
    token = api.AccessToken(LIVEKIT_API_KEY, LIVEKIT_API_SECRET)
    token.identity = identity
    token.name = data.get('name', 'Telegram User')
    token.add_grant(api.VideoGrants(
        room_join=True,
        room=room_name,
        can_publish=True,
        can_subscribe=True,
    ))
    
    return {"statusCode": 200, "headers": {"Content-Type": "text/plain"}, "body": token.to_jwt()}

def main(request):
    return handler(request)
