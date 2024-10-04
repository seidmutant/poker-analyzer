import asyncio
import logging
from typing import Tuple

logging.basicConfig(level=logging.INFO)

from outspeed import realtime
from realtime.plugins.gemini_vision import GeminiVision
from realtime.plugins.key_frame_detector import KeyFrameDetector
from realtime.streams import VideoStream, Stream, TextStream
from realtime.plugins.youtube_stream import YouTubeStream
from realtime.plugins.file_writer import FileWriter

@realtime.App()
class PokerCardReader:
    async def setup(self):
        self.keyframe_node = KeyFrameDetector(
            key_frame_threshold=0.2, key_frame_max_time=15
        )
        self.llm_node = GeminiVision(
            system_prompt="You are a poker card reader. Your job is to identify and describe the cards visible on the table and in players' hands. Only mention the cards you can see clearly. If no cards are visible, say 'No cards visible'. Keep the response brief and factual.",
            auto_respond=8,
            temperature=0.2,
            chat_history=False,
        )
        self.youtube_stream = YouTubeStream()
        self.file_writer = FileWriter("poker_cards_output.txt")

    @realtime.streaming_endpoint()
    async def run(self, youtube_url: str) -> Tuple[Stream, ...]:
        video_input_stream: VideoStream = await self.youtube_stream.run(youtube_url)

        key_frame_stream: VideoStream = await self.keyframe_node.run(video_input_stream)

        card_text_stream: TextStream = await self.llm_node.run(key_frame_stream)

        # Write the text stream to a file
        await self.file_writer.run(card_text_stream)

        return card_text_stream,

    async def teardown(self):
        await self.keyframe_node.close()
        await self.llm_node.close()
        await self.youtube_stream.close()
        await self.file_writer.close()

if __name__ == "__main__":
    asyncio.run(PokerCardReader().run("https://www.youtube.com/watch?v=2xl7B-2Yfuo"))