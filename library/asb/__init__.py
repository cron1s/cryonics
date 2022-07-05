import nextcord
import asyncio
##
from nextcord import Intents, Activity, ActivityType
from nextcord.ext.commands import Bot as AI
##

OwnerID = [360857351307395075]  # Discord: cronis#0001

# In naher Zukunft werden Cogs implementiert, deswegen bereite ich alles kommentiert vor #cronis

class Ready(object):
    pass

class Bot(AI):
    def __init__(self):
        self.ready = False
        self.guild = None

        super().__init__(
            command_prefix="$",
            owner_ids=OwnerID,
            intents=Intents.all(),
            help_command=None,
            case_insensitive=True
        )

    def run(self, version):
        self.VR = version

        print("Setup started!")

        with open("./library/secret/tkn.0", "r", encoding="utf-8") as tf:
            self.TKN = tf.read()

        print(" AI is starting!")
        super().run(self.TKN, reconnect=True)

###

    async def on_ready(self):
        print(" on_ready starting!")
        if not self.ready:
            self.stdout = self.get_channel(993522590146629662)

            await self.stdout.send("AI ready to rumble")
            self.ready = True
            print("#####  Cryonics Online  #####")
        else:
            print("---Bot Failure---")
            print(" Reconnecting...")

        self.client_id = (await self.application_info()).id

        while True:
            await super().change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.listening, name=f"$"))
            await asyncio.sleep(20)
            await super().change_presence(
                activity=nextcord.Activity(type=nextcord.ActivityType.streaming, name="Got Revived"))
            await asyncio.sleep(20)


bot = Bot()