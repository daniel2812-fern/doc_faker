from pyChatGPT import ChatGPT
# session_token = 'abc123'  # `__Secure-next-auth.session-token` cookie from https://chat.openai.com/chat
# api = ChatGPT(session_token)  # auth with session token
# api = ChatGPT(session_token, conversation_id='some-random-uuid')  # specify conversation id
# api = ChatGPT(session_token, proxy='https://proxy.example.com:8080')  # specify proxy
# api = ChatGPT(session_token, chrome_args=['--window-size=1920,768'])  # specify chrome args
# api = ChatGPT(session_token, moderation=False)  # disable moderation
# api = ChatGPT(session_token, verbose=True)  # verbose mode (print debug messages)

# auth with google login
api = ChatGPT(auth_type='google', email='danghoangnhan.1@gmail.com', password='huynhnhu10082017')



resp = api.send_message('Hello, world!')
print(resp['message'])

# api.reset_conversation()  # reset the conversation
# api.clear_conversations()  # clear all conversations
# api.refresh_chat_page()  # refresh the chat page