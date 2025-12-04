from Entities.Call import Call
from Services.VideoCallService import VideoCallService

class VoiceCallService:
    def start_voice_call(self):
        pass

    def switch_to_video_call(self, call: Call):
        call.call_type = "video"
        VideoCallService().start_video_call()
