from datetime import datetime

def sample_responses(input_text):
    user_message = str(input_text).lower()


    if user_message in ("hello", "hi", "what's Up",):
        return "Hey! How's it going?"

    if user_message in ("who are you","who are you?"):
        return "I am TechieKhtz!"
    
     if user_message in ("github link"):
        return "https://github.com/Shashika503"

    if user_message in ("medium blog link"):
        return "https://medium.com/@TechieKahtz" 

    if user_message in ("Could plz tell the time now?" , "time"):
        now = datetime.now()
        date_time = now.strftime("%d%m%y, %H:%M:%S")

    return str(date_time)

    return "I don't understand you."


