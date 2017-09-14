set dB=%1
for /l %%x in (1, 1, 400) do sox audios_wav/%%x.wav -n remix 1 rate -v 6800 spectrogram -m -X 27 -r -z %dB% -o spectrograms/%dB%/%%x.png 