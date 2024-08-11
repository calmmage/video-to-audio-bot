from bot_lib import Handler, HandlerDisplayMode
from calmapp import App
from video_to_audio_bot.utils import convert_video_to_audio


class MyApp(App):
    """This is an amazing application that I developed in my free time! For now it just exists, and that is good!"""

    name: str = "My amazing app"
    # Sample
    start_message = "Hello! I am {name}. {description}"
    # Sample help message
    help_message = "Help! I need somebody! Help! Not just anybody! Help! You know I need someone! Help!"

    @property
    def description(self):
        return self.__doc__

    def invoke(self, input_str):
        return input_str

    def dummy_command(self):
        return "Hey! I am a dummy"

    def convert_video_to_audio(self, video):
        audio = convert_video_to_audio(video)
        return audio
        # return "Video converted to audio"


class MyHandler(Handler):
    name = "main"
    display_mode = HandlerDisplayMode.FULL
    commands = {
        "dummy_command_handler": "dummy_command",
    }

    has_chat_handler = True

    async def chat_handler(self, message, app: MyApp):
        input_str = await self.get_message_text(message)
        output_str = app.invoke(input_str)
        await self.reply_safe(output_str, message)

    async def dummy_command_handler(self, message, app: MyApp):
        output_str = app.dummy_command()
        await self.reply_safe(output_str, message)
