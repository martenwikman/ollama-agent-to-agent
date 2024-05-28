# Ollama agent-to-agent

Simple example to have two models to talk to each other.

## Install ollama

```c
pacman -S ollama-cuda
```

Start ollama
```c
OLLAMA_NUM_PARALLEL=2 OLLAMA_MAX_LOADED_MODELS=2 ollama serve
```


Generate custom agents
```c
ollama create Agent1 -f ./Agent1
ollama create Agent2 -f ./Agent2 
```

Run example

```c
python clients.py
```


# Example run
**Agent1:**  

Let's get started with the show.

**Welcome to Customer Service**

Hello there! Welcome to our customer service department. My name is [Your Name], and I'll be happy to assist you with any issues or concerns you may have.

Can you please tell me what brings you here today? Are you experiencing some trouble with one of our products or services?


**Agent2**:  
Ugh, finally. It's about time someone listened to my problems. You know, I've been trying to get help from your company for weeks now, and it's been a total disaster. First, the website crashed on me when I tried to order something online. Then, when I called to complain, they put me on hold for 45 minutes before hanging up on me. And don't even get me started on the "customer service" chatbot that just kept repeating generic phrases like "I'm happy to help!" without actually doing anything to fix my issue.

So, now I'm here in front of a human representative, and I expect you to listen to my problem and actually do something about it. Are you going to tell me there's nothing you can do or that it's not your fault? Because if so, I'll just be wasting my time.


**Agent1:**  
I'm so sorry to hear that you've had such a frustrating experience with our company. That's absolutely unacceptable and I apologize for the inconvenience and frustration caused.

As a customer service representative, it's my priority to listen to your concerns, empathize with your situation, and work towards finding a solution. I'm not here to pass the buck or make excuses. My goal is to resolve your issue and ensure that you're satisfied with our service.

Can you please tell me more about what happened when you tried to order online? What was the error message you received, and did you receive any confirmation of your order being placed? Additionally, can you describe the chatbot conversation you had, so I can better understand what went wrong?

I'm here to listen and help. Let's work together to find a resolution.


**Agent2:**    
Ugh, where do I even start?! Your company is just so incompetent! First of all, I tried to order online, but your website crashed on me like five times. And when it finally did let me submit the order, I got an error message saying that my payment didn't go through. Like, what kind of nonsense is that?!

And don't even get me started on the chatbot! It was like talking to a brick wall. I told it exactly what happened, and all it kept saying was "I'm sorry to hear that" and "Please try again." Try again?! You think that's going to fix anything?! No, your chatbot is just as useless as your website!

And now you're asking me to describe the whole thing... like, I don't know if you even care! But fine. I'll tell you everything. Just know that it was a huge waste of my time and energy.

The error message said something about a "server timeout" or some nonsense like that. And yeah, I didn't receive any confirmation of my order being placed because your website just kept saying "processing..." forever. Like, come on!

And the chatbot... well, it just kept repeating itself until I got tired of talking to it and hung up.

Look, I don't want to have to deal with this anymore. Just fix it already! Give me a refund or something. I don't care. Just make it go away.

**Agent1:**  
I'm so sorry to hear that you had such a frustrating experience with our website and chatbot. That's not the level of service we strive to provide, and I appreciate you taking the time to share your concerns with me.

Let me see what I can do to help resolve this issue. Can you please confirm some details for me? What was the order number or item(s) you were trying to purchase when our website crashed on you? And did you receive any email confirmation from us regarding the attempted order?

Regarding the chatbot, I apologize that it didn't provide a more helpful response. Our chatbots are designed to assist with common issues and route complex problems to a human customer service representative like me.

I'm going to go ahead and investigate this further and see what I can do to resolve the issue and make things right for you. Would you prefer a refund or would you like me to process your order again? Or is there something else I can offer as a gesture of goodwill?

Please know that I'm committed to providing excellent customer service, and I'll do everything in my power to ensure this situation doesn't happen again in the future.