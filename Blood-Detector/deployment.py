import streamlit as st
import os 
import cv2
import numpy as np
from PIL import Image
import cv2 as cv
import tempfile
import io
from blood_detection import detection

style_html = '''
    <style>
        body {
            background-image: url('https://i.imgur.com/59I8Qgw.png');
            background-size: cover;
        }
        
    </style>
'''
st.markdown(style_html, unsafe_allow_html = True)

def file_selector(folder_path='./inference/input'):

    filenames = os.listdir(folder_path)
    selected_filename = st.selectbox('Elige el archivo', filenames)
    
    if selected_filename is not None:
        return os.path.join(folder_path, selected_filename)
    else:
        return None


def main():
    st.title("RasPi-BloodView") #creacion de titulo 
    st.write("Detección de células sanguíneas con Pytorch desplegando en Raspberry 4") #Subtitulo
    activites = ["Detección", "Acerca de"] #creacion de botones
    choices = st.sidebar.selectbox("Seleccione la opción", activites)
    
    if choices == "Detección":
        #st.subheader("")
        #file = st.file_uploader("Sube la imagen", type = ['png', 'jpeg', 'jpg', 'mp4'])
        path_file = file_selector()

        if path_file is not None:

            path_end_file = path_file.split("\\")[-1]  # path_end_file = test.jpg
            st.write('Archivo elegido `%s`' % path_end_file)
            endwith = path_end_file.split(".")[-1]

            if endwith == 'mp4':
                file = io.open("./inference/input/{}".format(path_end_file), "rb")
                video_bytes = file.read()
                st.video(video_bytes)
        
            elif endwith in ('png', 'jpeg', 'jpg'):
                image_upload = Image.open("./inference/input/{}".format(path_end_file))
                image_upload.thumbnail((640, 480), Image.ANTIALIAS)
                st.image(image_upload)
 
            if st.button("Realizar inferencia"):
                finished = detection(path_end_file)  # path_end_file = test.jpg or video.mp4
                
                st.write('Inferencia de `%s` terminada!' % path_end_file)

                
                endwith = path_end_file.split(".")[-1]

                if endwith == 'mp4':
                    file = io.open("./inference/output/{}".format(path_end_file), "rb")
                    video_bytes = file.read()
                    st.video(video_bytes)
                
                elif endwith in ('png', 'jpeg', 'jpg'):
                    image_upload = Image.open("./inference/output/{}".format(path_end_file))
                    image_upload.thumbnail((640, 480), Image.ANTIALIAS)
                    st.image(image_upload)
        else:
            st.write('Carpeta {} vacía'.format('./inference/input'))
            st.write('Por favor, agregre imágenes o videos')

    elif choices == "Acerca de":
        st.write("Alexander Morales Panitz")
        st.write("Cristhian Sánchez Sauñe")
        st.write("César Atusparia Alhua") 

if __name__ == '__main__':
    main()