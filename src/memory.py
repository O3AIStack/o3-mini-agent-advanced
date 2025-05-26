from typing import Dict

class SessionMemory:
    def __init__(self):
        self.sessions: Dict[str, Dict[str, str]] = {}

    def add_to_session(self, session_id: str, key: str, value: str):
        if session_id not in self.sessions:
            self.sessions[session_id] = {}
        self.sessions[session_id][key] = value

    def get_from_session(self, session_id: str, key: str) -> str:
        return self.sessions.get(session_id, {}).get(key, "")

    def get_full_session(self, session_id: str) -> Dict[str, str]:
        return self.sessions.get(session_id, {})
