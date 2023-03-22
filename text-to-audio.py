#!/usr/bin/env python
# coding=utf8
#
# Copyright (C) 2023, Diego Cambiaso
# GNU General Public License v3.0

'''
This script is for educational purposes and will let you convert text to audio.
'''

from gtts import gTTS
from playsound import playsound

file = 'interview.mp3'
speach = gTTS(text='This is the text that you want \
    to convert into audio file.',
    lang = 'en', slow = False)

speach.save(audio)
playsound(audio)
