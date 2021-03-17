from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"<b>Currently Only supports Youtube Single(No playlist)🥺♥ /n/n Just Send Youtube Url /n/n Deployed by @Ez_Tee </b>"
    await message.reply_text(helptxt)
