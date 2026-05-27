def convert(text):
    text=text.replace(":)", "🙂")
    text=text.replace(":(", "🙁")
    text=text.replace("</3", "💔")
    return text
def main():
    user_input=input("Enter a message using emoticons: ")
    converted_text= convert(user_input)
    print(converted_text)

main()
