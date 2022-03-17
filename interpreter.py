import json
import os
import re
# https://pypi.org/project/pocketsphinx/
from pocketsphinx import LiveSpeech


class Interpreter():

    """
    Listens to the user's voice and interprets their commands.
    """
    
    def __init__(self, **kwargs):    
        params = {"voice_bindings_path": "voice_bindings.json"}
        params.update(kwargs)

        with open(params["voice_bindings_path"], "r") as f:
            s = f.read()
        self.voice_bindings = json.loads(s)


    def start(self):

        """
        Enters listen-execute loop.
        """
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


