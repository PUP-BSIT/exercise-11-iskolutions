import emoji

def emotion_identifier():
    input_text = input("How are you feeling today? ").lower()

    responses = {
        "happy": ":beaming_face_with_smiling_eyes: I'm glad to hear that!",
        "sad": ":smiling_face_with_tear:  I'm sorry to hear that.",
        "angry": ":enraged_face: It's okay to feel angry sometimes.",
        "confused": ":thinking_face: It's normal to feel confused.",
        "shocked": ":flushed_face: That sounds surprising!",
        "bored": ":yawning_face: Maybe try something new!",
        "shy": ":face_with_peeking_eye:  It's okay to be shy.",
        "excited": ":partying_face: That's awesome!",
        "anxious": ":worried_face: It's okay to feel anxious.",
        "tired": ":sleepy_face: Make sure to rest.",
        "amazing": ":smiling_face_with_sunglasses: That's fantastic!"
    }

    message = ":neutral_face: I see."
    for word in responses:
        if word in input_text:
            message = responses[word]
            break

    print(emoji.emojize(message))

    print(emoji.emojize("Don't forget to take care of yourself! "
            + ":sparkling_heart:"))