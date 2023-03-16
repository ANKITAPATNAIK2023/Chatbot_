import random
R_EATING = "I dont like eating anything because I'm a bot obviously!"
R_ADVICE = "If I were you,I would go to  the internet and type exactly what you wrote there! "

def unknown():
    response= ['could you re-phrase that?',
               "...",
               "sounds about right",
               "what does that mean?"][random.randrange(4)]
    return response