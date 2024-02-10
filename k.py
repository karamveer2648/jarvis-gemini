import speech_recognition as sr

recognizer = sr.Recognizer()
def mic1():
    with sr.Microphone(device_index=1) as source:
        print("Say Somethin: ")
        recognizer.adjust_for_ambient_noise(source)
        
        audio = recognizer.listen(source)  # Adjust timeout as needed
        
        print("recognizing...")
        text = recognizer.recognize_google(audio)
        print ("You said: ", text)
        return text
if __name__ == "__main__":
    
    mic1()
