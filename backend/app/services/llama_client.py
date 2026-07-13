import os
import base64
from dotenv import load_dotenv
from huggingface_hub import InferenceClient


load_dotenv()


client = InferenceClient(
    token=os.getenv("HF_TOKEN")
)


MODEL = "meta-llama/Llama-4-Scout-17B-16E-Instruct"


def analyze_image(image_path, prompt):

    with open(image_path, "rb") as image_file:
        image_bytes = image_file.read()

    encoded_image = base64.b64encode(image_bytes).decode("utf-8")


    response = client.chat.completions.create(

        model=MODEL,

        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": prompt
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{encoded_image}"
                        }
                    }
                ]
            }
        ],

        max_tokens=1000
    )


    return response.choices[0].message.content