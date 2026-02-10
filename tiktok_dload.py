import asyncio
import os
from TikTokApi import TikTokApi

async def download_tiktok_video(url: str, output_path: str = "video.mp4"):
    async with TikTokApi() as api:
        await api.create_sessions(num_sessions=1, headless=False, browser="chromium")

        video = api.video(url=url)
        await video.info()  # must call info() first to get downloadAddr

        counter = 0
        while os.path.exists(output_path):
            counter += 1
            output_path = output_path.replace(".mp4", f"{counter}_.mp4")

        video_bytes = await video.bytes()
        with open(output_path, "wb") as f:
            f.write(video_bytes)

        print(f"Video saved to {output_path}")

def main():
    download_tiktok_video(url)

if __name__ == "__main__":
    main()

# Test it
#video_url = "https://vt.tiktok.com/ZSmeoBxgY/"
#asyncio.run(download_tiktok_video(video_url))