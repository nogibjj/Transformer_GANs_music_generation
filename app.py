import streamlit as st
from keras.models import load_model

def generate_music(emotion):
    # Generate music based on the selected emotion
    if emotion == 'Happy':
        emotion = 1
        gan = load_model('combined3.h5')
    elif emotion == 'Sad':
        emotion = 2
        gan = load_model('combined2.h5')
    elif emotion == 'Angry':
        emotion = 3
        gan = load_model('combined1.h5')
    elif emotion == 'Relaxed':
        emotion = 0
        gan = load_model('combined0.h5')

    music = gan.generate_for_emotion(emotion)
    return music

# Streamlit app
st.title('Music Emotion Generator')
emotion = st.selectbox('Select emotion', ['Happy', 'Sad', 'Angry', 'Relaxed'])
if st.button('Generate'):
    music_file = generate_music(emotion)
    st.audio(music_file, format='audio/midi')
    