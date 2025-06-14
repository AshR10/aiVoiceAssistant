from livekit.agents import (
    Agent,
    AgentSession,
    JobContext,
    WorkerOptions,
    cli,
)
from livekit.plugins import groq, silero, elevenlabs

from dotenv import load_dotenv

load_dotenv(dotenv_path=".env")


async def entrypoint(ctx: JobContext):
    await ctx.connect()

    agent = Agent(
        instructions="""
            You are a friendly voice assistant built by LiveKit.
            Start every conversation by greeting the user.
            """,
        
    )
    session = AgentSession(
        vad=silero.VAD.load(),
        # any combination of STT, LLM, TTS, or realtime API can be used
        stt=groq.STT(),  
        llm=groq.LLM(model="llama-3.3-70b-versatile"),
        tts=elevenlabs.TTS(
        voice_id="EXAVITQu4vr4xnSDxMaL",  #voice id from elevanlabs/voices/default-voices
        model="eleven_monolingual_v1"            
    ),
    )

    await session.start(agent=agent, room=ctx.room)
    await session.generate_reply(instructions="Say good day, then ask the user how their day is going and how you can help.")

if __name__ == "__main__":
    cli.run_app(WorkerOptions(entrypoint_fnc=entrypoint))