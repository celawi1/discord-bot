#potrebno je kreirati server na discord.com
#komplet uputstvo na https://www.youtube.com/watch?v=W4U0UoT92YM&t=2222s
#token: MTQzMjgwODYzODczNjYzMzg4Nw.GUVPd6.K0YcnUyRkiPVa2LF8726k8F7tc6O5PVFI8WEoc
#general_url: https://discord.com/oauth2/authorize?client_id=1432808638736633887&permissions=8&integration_type=0&scope=bot
#pre pocetka smo morali da instaliramo dicord paket "pip install discord"

import discord

token = "MTQzMjgwODYzODczNjYzMzg4Nw.GUVPd6.K0YcnUyRkiPVa2LF8726k8F7tc6O5PVFI8WEoc"

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
'''
Ove dve funkcije (on_ready, on_message) su deo discord paketa i mi se na njih kacimo i dodajemo nas kod.
To su funkcije namenjene za slusanje evenata koji se trigeruju vezano za discord server
'''
@client.event
async def on_ready():
    print(f"Logged in as: {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return #ignorisi poruke od bota
    
    if message.content.lower() == "ping":   #dodao .lower() tako da bude non case sensitive
        await message.channel.send("Pong")

    if message.content.lower() == "sta ima novo":
        await message.channel.send("Aman bas nista.")  

#kikovanje usera sa servera
    if message.content.strip().lower() == "lol":
        await message.channel.send("Ne smes reci LOL na chatu!")
        await message.author.kick(reason="Izbacen si sa servera!")

#anketa
    if message.content.lower().startswith("!poll"):
        print("Usao")
        question = message.content[len("!poll "):].strip()
        if question:
            poll_message = await message.channel.send(f"Poll: {question}")
            await poll_message.add_reaction('\U0001F44D') #unicode za like U+1F44D (dodali \ na pocetku i 000 umesto plusa)
            await poll_message.add_reaction('\U0001F44E')
        else:
            await message.channel.send("Nisi postavio pitanje!")

#ovo je bonus kod iz ChatGPT---------------------
    responses = {
        "ping": "Pong",
        "kako si": "Dobro je, nije loše.",
        "cao": "Ćao i tebi!",
        "ko si ti": "Ja sam tvoj Discord bot 🤖"
    }

    msg = message.content.strip().lower()

    if msg in responses:
        await message.channel.send(responses[msg])
#--------------------------------------------------              
    
    print(message.content)
    #await message.channel.send("Caooooo")
#------------------------------------------------------YOUTUBE 59:00
client.run(token)

print("test")