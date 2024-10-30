import cv2
import mediapipe as mp
import numpy as np
import time, os

actions = ['come', 'away', 'spin', 'fuck']
seq_length = 30
secs_for_action = 30

mp_hands = mp.solutions.hands
mp_drawiong