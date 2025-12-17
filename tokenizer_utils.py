
import tiktoken

enc = tiktoken.get_encoding("cl100k_base") #ini basenya emang buat ngitung token openai sih, tapi uda liat di web llama3.1 token counter..hasilnya sama

def count_tokens(text: str) -> int:
    return len(enc.encode(text))