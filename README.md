
## Packages

        pip install opencv-python
        pip install tensorflow==1.15.*
        pip install scipy
        pip install flask
        pip install flask-restful
        pip install azure-eventgrid
        pip install azure-storage-blob


## Running

- Add user to database

        python main.py  add  image_file  face_name
        
    For example
    
        python main.py  add  1.jpg  Maria
        
- Delete user from database

        python main.py  del/remove  face_name
        
    For example
    
        python main.py  del  Maria
        python main.py  remove  Maria
        
- Check the image and recognize the face, detect the mask

        python main.py  check  image_file
        
    For example
    
        python main.py  check  1.jpg
        
    The output format will be
    
        Checking user ...
            Face detected => Name: John, Score: 97.67, Gender: Male
            Face detected => Name: Maria, Score: 97.44, Gender: Female
            
- Check the video and recognize the face, detect the mask

        python main.py  check  video_file
        
    For example
    
        python main.py  check  1.mp4
        
- Check the Web cam

        python main.py  check  webcam
        
- Run flask server

        python flask_server.py
