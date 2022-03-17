from pocketsphinx import LiveSpeech
import json
import os
import re

class Interpreter():
    
    def __init__(self, **kwargs):    
        params = {"voice_bindings_path": "voice_bindings.json"}
        params.update(kwargs)

        with open(params["voice_bindings_path"], "r") as f:
            s = f.read()
        self.voice_bindings = json.loads(s)


    def start(self):
        for phrase in LiveSpeech():
            print(phrase)
            
            phrase = str(phrase)
            tokens = re.split("\s+", phrase)

            for token in tokens:
                try:
                    command = self.voice_bindings[token]
                    print(command)
                    
                    # os.system(command)
                    for i in range(10):
                        os.system(command)

                except:
                    print("unrecognized voice-binding!")


