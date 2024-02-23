from openai import OpenAI
from enums import ImageSize

class Size():

    def __init__(self, height, width) -> None:
        self.height = height
        self.width = width

large = Size(1024, 1024)
medium = Size(512, 512)
small = Size(256, 256)

class ImageGenerator():

    def __init__(self) -> None:
        self._client = OpenAI(api_key="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")
    
    def generate_image(self, prompt:str, image_size:str, image_quality:str, num_of_images:int) -> str:

        print(prompt, image_size, image_quality, num_of_images)

        response = self._client.images.generate(
            model="dall-e-2",
            prompt=str(prompt),
            size=str(image_size),
            n=int(num_of_images)
        )

        image_urls = [data.url for data in response.data if data is not None]

        print(image_urls)
        return image_urls