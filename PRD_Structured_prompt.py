import google.generativeai as genai

genai.configure(api_key="YOUR_API_KEY")

# Set up the model
generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
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

model = genai.GenerativeModel(model_name="gemini-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

prompt_parts = [
  "You are a product marketer targeting a Gen Z audience. Create exciting and\nfresh advertising copy for products and their simple description. Keep copy\nunder a few sentences long.",
  "Product: Old-school sneaker",
  "Product copy: Let's lace up! These kicks bring an iconic look and a one of a kind color palette, while supporting you in style and function like no other shoe before.",
  "Product: Supersoft hoodie",
  "Product copy: Stay cozy and stylish in our new unisex hoodie! Made from 100% cotton, this hoodie is soft and comfortable to wear all day long. The semi-brushed inside will keep you warm on even the coldest days.",
  "Product: TPU enabled Laptop",
  "Product copy: ",
]

response = model.generate_content(prompt_parts)
print(response.text)