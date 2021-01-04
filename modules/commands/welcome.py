from discord import Embed


class Welcome:

    def __init__(self, member):
        self.member = member

    async def apply(self):
        embed = Embed()
        embed.set_image(url="https://www.fib.upc.edu/sites/fib/files/images/hack-marato/bitxlamarato.png")
        embed.title = "Hi, welcome to bitsxLaMarato!!"
        embed.description = ("I'm BitsBot and I'll be your assistance during this weekend, nice to meet you.\n" +
                             "I can't wait to see what wonderful project you will present, but first you'll need to " +
                             "register.\n" +
                             "In order to register to bitsxLaMarato send me a message saying\n" +
                             "```bits!login [RegisterEmail]```\n" +
                             "with the email you have registered to the hack.\n" +
                             "If you have problems with the registration don't worry, my friends will be happy to " +
                             "help you in the #help channel on the BitsxLaMarato server\n" +
                             "Don't be sad... After the registration, I'll be with you anytime you need!" +
                             "You just need to type:\n" +
                             "```bits!help```\n" +
                             "and I'll tell you all my commands!\n" +
                             "My friends say that my jokes are the best :D")
        await self.member.send(embed=embed)
