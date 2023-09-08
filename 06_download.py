import asyncio
import httpx

client = httpx.AsyncClient()

async def download(image_name, url):
    response = await client.get(url)
    print("Downloaded image", image_name)   

    file = open(image_name, "wb")     # Open file for writing
    file.write(response.read())       # Write image to file
    print("Image Saved ", image_name)

async def main():
    links = [
        "https://i.redd.it/v1xhudmir7mb1.jpg",
        "https://i.redd.it/vy7y1nleb9mb1.jpg",
        "https://i.redd.it/7153e160eamb1.jpg",
    ]

    await asyncio.gather(
        download("Cutedog.jpg", links[0]),
        download("2Cutedogs.jpg", links[1]),
        download("2Cutecats.jpg", links[2]),
    )

asyncio.run(main())
