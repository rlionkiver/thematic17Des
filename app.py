
from flask import Flask, request, jsonify
import xml.etree.ElementTree as ET
from tokenizer_utils import count_tokens
from llm_client import call_llm
from prompts import XML_PROMPT, JSON_PROMPT, RAW_PROMPT, XML_Snailly

app = Flask(__name__)

@app.route("/analyze-json", methods=["POST"])
def analyze():
    data = request.get_json()
    # Bangun prompt dari field persona, task, questions jika 'prompt' tidak ada
    if "prompt" in data:
        prompt = data["prompt"]
    else:
        persona = data.get("persona", "")
        task = data.get("task", "")
        questions = data.get("questions", "")
        if not (persona or task or questions):
            return jsonify({"error": "Input harus mengandung 'prompt' atau kombinasi 'persona', 'task', dan 'questions'."}), 400
        prompt = f"Persona: {persona}\nTask: {task}\nQuestions: {questions}"

    model = data.get("model", "llama-3.1-8b-instant")

    output = call_llm(prompt, model=model)
    prompt_tokens = count_tokens(prompt)
    output_tokens = count_tokens(output)

    return jsonify({
        "prompt_tokens": prompt_tokens,
        "output_tokens": output_tokens,
        "total_tokens": prompt_tokens + output_tokens,
        "output_preview": output
    })

@app.route("/analyze-xml", methods=["POST"])
def analyze_xml():
    if request.content_type == "application/xml":
        xml_data = request.data.decode("utf-8")
        print("XML DATA:", repr(xml_data)) 
        try:
            root = ET.fromstring(f"<root>{xml_data}</root>")
            prompt = ET.tostring(root, encoding="unicode")
        except ET.ParseError as e:
            return jsonify({"error": f"XML ParseError: {str(e)}"}), 400
        
        output = call_llm(prompt)
        prompt_tokens = count_tokens(prompt)
        output_tokens = count_tokens(output)
        return jsonify({
            "prompt": prompt,
            "prompt_tokens": prompt_tokens,
            "output_tokens": output_tokens,
            "total_tokens": prompt_tokens + output_tokens,
            "output_preview": output
        })
    else:
        return jsonify({"error": "Content-Type must be application/xml"}), 415

@app.route("/membandingkan", methods=["POST"])
def membandingkan():
    data = request.get_json()
    model = data.get("model", "llama-3.1-8b-instant")

    prompts = {
        "XML": XML_PROMPT,
        "JSON": JSON_PROMPT,
        "RAW": RAW_PROMPT
    }
    results = {}
    for fmt, prompt in prompts.items():
        output = call_llm(prompt, model=model)
        prompt_tokens = count_tokens(prompt)
        output_tokens = count_tokens(output)
        results[fmt] = {
            "prompt_tokens": prompt_tokens,
            "output_tokens": output_tokens,
            "total_tokens": prompt_tokens + output_tokens,
            "output_preview": output
        }
    return jsonify(results)

#ini mencoba untuk analisis gambar dengan formasi hierarki XML pada produk snailly
@app.route("/snailly", methods =["POST"])
def snailly_analysis():
    output = call_llm(XML_Snailly, model="meta-llama/Llama-4-Scout-17B-16E-Instruct")
    prompt_tokens = count_tokens(XML_Snailly)
    output_tokens = count_tokens(output)
    return jsonify({
        "prompt_tokens": prompt_tokens,
        "output_tokens": output_tokens,
        "total_tokens": prompt_tokens + output_tokens,
        "output_preview": output
    })

if __name__ == "__main__":
    app.run(debug=True, port = 5000)
