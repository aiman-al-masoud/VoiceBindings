# Voice-Bindings

Do stuff with your voice! 


## Installation:

run the bash script `install.sh` on your linux-box:

```
./install.sh
```

## Try it out:

run the `__main__.py` file, then open up `test_game.html`  on your favourite browser, and start issuing voice commands to the helicopter sprite:

```
python3 __main__.py
firefox test_game.html
```

### Then say one or more of these in any order:

* Down
* Up/yes
* Right
* Left

## Add your own 'voice-bindings':

Just edit the `voice_bindings.json` file, adding in your own voice-binding as a key, and the command you want it to trigger on your system (in bash) as a value.



## External Links:

### This utility is powered by <a href="https://pypi.org/project/pocketsphinx/">Pocketsphinx</a> offline speech recognition software.

### Game from here:
<a href="https://github.com/aiman-al-masoud/ReactGame">https://github.com/aiman-al-masoud/ReactGame</a>

