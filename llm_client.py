
from groq import Groq
import os

def call_llm(prompt: str, api_key: str = None, model: str = "llama-3.1-8b-instant", image: str = None) -> str:
    if api_key is None:
        api_key = "DIISIIIIIIIIIIIII" #masukkan API KEY kalian masing-masing disini ya wankawan
    if not api_key:
        raise ValueError("YANG BENER YA WANKAWAN MASUKIN APII NYAAA..KALAU KEUKEUH BILANG UDA BENER..NAPA BISA MASUK SINII")

    # Jika ada image, pakai model Llama-4-Scout
    if image is not None:
        model = "meta-llama/llama-4-scout-17b-16e-instruct"

    client = Groq(api_key=api_key)
    messages = [
        {
            "role": "user",
            "content": prompt
        }
    ]

    if image is not None:
        messages[0]["image"] = image

    completion = client.chat.completions.create(
        model=model,
        messages=messages
    )
    return completion.choices[0].message.content


