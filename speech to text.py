
import speech_recognition as sr
r=sr.Recognizer()

with sr.Microphone()as src:
    print("speak")
    r.adjust_for_ambient_noise(src, duration=1)
    myaduio=r.listen(src)
    mytext=r.recognize_google(myaduio)
    mytext=mytext.lower()
    print(mytext)
    
    f=open("D:\\text.txt","a")
    f.writelines(mytext)
    f.close() 