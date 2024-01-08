from pathlib import Path
import google.generativeai as genai

genai.configure(api_key="YOUR_API_KEY")

# Set up the model
generation_config = {
  "temperature": 0.6,
  "top_p": 0,
  "top_k": 32,
  "max_output_tokens": 4095,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

model = genai.GenerativeModel(model_name="gemini-pro-vision",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

# Validate that an image is present
if not (img := Path("image0.jpeg")).exists():
  raise FileNotFoundError(f"Could not find image: {img}")

image_parts = [
  {
    "mime_type": "image/jpeg",
    "data": Path("image0.jpeg").read_bytes()
  },
]

prompt_parts = [
  "look at the following picture and tell me who is the architect",
  image_parts[0],
  "Who are various people who lived in the building",
]

response = model.generate_content(prompt_parts)
print(response.text)