import os


# -------------------- camera --------------------
# CAMERA_URL = ['rtsp://190.7.215.86:7447/589dd55ae4b052391484b354_1']
# CAMERA_URL = ['../sample.mp4']
CAMERA_URL = ['../samples/1.mp4']
# CAMERA_URL = ['../car1.mp4', '../1.mp4']

# --------------------- DB ----------------------
DB_PATH = 'database'
DB_CSV = os.path.join(DB_PATH, 'register.csv')
DB_IMAGES_PATH = os.path.join(DB_PATH, 'images')

# --------------- Face detection ----------------
DETECTION_THRESHOLD = 0.99
RECOGNITION_THRESHOLD = 0.6
STORE_THRESHOLD = 0.25

# -------------------- Others -------------------
RESIZE_FACTOR = 1.0
DISPLAY_DETECT_FRAME_ONLY = True
FACE_COORDINATES = 'coordinates'
FACE_SCORES = 'scores'
FACE_NAMES = 'names'
SAVE_VIDEO = False
FOLDER_UNIDENTIFIED = 'save_unidentified'

# ----------------- Azure Action ------------------
SEND_EVENT = False
SEND_FACES = True
