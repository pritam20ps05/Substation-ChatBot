#function for chatbot in python with the help of openai's chat gpt api
#developed by Ayush Burman
import openai
class GPTapi:

    def __init__(self, api_key) -> None: #constructor to pass api key parameter for security purpose
        self.api_key=api_key
        openai.api_key=api_key
        self.temperature=0.8 #to train the model to be random&creative(more value of temp..) or deterministic&focused(less value of temp..)
        self.max_tokens=None #to set the maximum limits on words(1token=1.5words)
    
    def chatapi(self, data: dict) -> dict: #data should be in dict format in the form(data={"messages":[{"role":"abc","content":"xyz........."},...]})
        messages = [] 
        system_msg = "You are an Intelligent chatbot named powerbot, who answers queries about Maintainence Process within a Subtstaion in a very concise, summarised way and in different points or paragraphs. Try to keep all the responses roughly within around 80 tokens." # behaviour of the bot
        messages.append({"role": "system", "content": system_msg})

        messages+=data["messages"]
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=data["temp"],
            max_tokens=self.max_tokens)
        reply: str = response.choices[0].message.content
        rep={"content": reply}
        print(rep)
        return rep