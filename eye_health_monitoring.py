# -*- coding: utf-8 -*-
# 얼굴 등록은 처음 실행 시 한 번만 수행, 이후 저장된 인코딩 파일을 로드하여 사용

import cv2
import mediapipe as mp
import math
import time
import threading
import numpy as np
import mss
import pyautogui
from plyer import notification
import datetime
import sqlite3
import os
import face_recognition
import uuid
import pickle  # 얼굴 인코딩 저장용

# (중간 생략 - 전체 코드는 이전 셀에 있음)

def load_or_create_encodings():
    if os.path.exists(ENCODING_FILE):
        with open(ENCODING_FILE, "rb") as f:
            return pickle.load(f)
    else:
        return capture_face_images()

# 이하 생략
