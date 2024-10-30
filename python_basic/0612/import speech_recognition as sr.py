import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source :
    print("말씀해주세요.")
    audio = r.listen(source)

text = r.recognize_google(audio, language='ko-KR')