from datetime import datetime

from Entities.Call import Call
from Entities.Chat import Chat
from Entities.User import User
from Services.VoiceCallService import VoiceCallService
from Services.VideoCallService import VideoCallService

class CallService:
    def start_call(self, user: User, call: Call, chat: Chat, call_type):
        call.caller = user
        call.chat = chat
        call.call_type = call_type
        call.started_at = datetime.now()
        if call_type == "voice":
            VoiceCallService().start_voice_call()
        elif call_type == "video":
            VideoCallService().start_video_call()

    def end_call(self, call: Call):
        call.ended_at = datetime.now()

    def turn_on_speaker(self):
        pass

    def add_members(self, call: Call, user: User):
        call.receivers.append(user)
        pass