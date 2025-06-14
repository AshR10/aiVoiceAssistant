# aiVoiceAssistant

  This simple implementation of voice assistant can be done completely free using groq (stt,llm) and elevenlabs (tts) as of 14/06/2025. Changes may happen to the free tier of both groq and elevenlabs in future and you might have to replace them with another free service. 

# links

  If you dont have an account for any of these, sign up.

  livekit link : https://cloud.livekit.io/projects/p_43u0bzwb0as/settings/keys You have to create a project. API key,URL, and secret key can be found by creating a key from settings/keys

  livekit playground : https://agents-playground.livekit.io/ Choose cloud and the project you created.
  
  groq : https://console.groq.com/home Click create key to create an api key.
  
  elevenlabs : https://elevenlabs.io/app/home The api key can be found in audio tools/soundboard/api/api keys. For voice id go to voices/default voices click on 3 dots of any voice you find apt and copy the id.

  rename .sampleenv to .env and add keys 

# installations

  clone the repo

  git clone https://github.com/AshR10/aiVoiceAssistant.git
  cd aiVoiceAssistant

  create a virtual environment first to avoid conflicts

    python -m venv .venv
    .venv\Scripts\activate -> for windows
    source .venv/bin/activate -> for unix systems

  install/upgrade pip

    python -m pip install --upgrade pip

  install livekit-agents and dotenv

    pip install livekit-agents[groq,silero,elevenlabs]
    pip install python-dotenv

# execution

  run the main file via terminal

    python3 main.py start
  
  on your web browser go to livekit playground : https://agents-playground.livekit.io/
  choose cloud and the project you created.
  click connect, allow microphone.

