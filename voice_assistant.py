import os
from dotenv import load_dotenv

load_dotenv()

AGENT_ID = os.getenv("AGENT_ID")
API_KEY = os.getenv("API_KEY")

from elevenlabs.client import ElevenLabs
from elevenlabs.conversational_ai.conversation import Conversation
from elevenlabs.conversational_ai.default_audio_interface import DefaultAudioInterface
from elevenlabs.types import ConversationConfig

user_name = "Brayan"
schedule = "Class from 10-11:30; 12-8: study o'clock"
prompt = f"You are a helpful assistant. Your interlocutor has the following schedule: {schedule}"
first_message = f"Hello, {user_name}, how can I help you today?"
