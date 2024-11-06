from llama_index.core.workflow import Event

class UserProfileEvent(Event):
    user_profile: dict
