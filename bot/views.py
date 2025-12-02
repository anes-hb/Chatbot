from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from transformers import pipeline

translator_en_fr = pipeline("translation_en_to_fr", model="Helsinki-NLP/opus-mt-en-fr")
translator_fr_en = pipeline("translation_fr_to_en", model="Helsinki-NLP/opus-mt-fr-en")

@api_view(["POST"])
def translate_text(request):
    text = request.data.get("text")
    target = request.data.get("target")  # "fr" or "en"

    if not text or not target:
        return Response({"error": "text & target are required"}, status=400)

    # EN → FR
    if target.lower() == "fr":
        translated = translator_en_fr(text)[0]['translation_text']

    # FR → EN
    elif target.lower() == "en":
        translated = translator_fr_en(text)[0]['translation_text']

    else:
        return Response({"error": "Unsupported target language"}, status=400)

    return Response({
        "original": text,
        "translated": translated
    })



# ✅ Summarizer: placeholder
@api_view(['POST'])
def summarize_text(request):
    text = request.data.get("text")

    if not text:
        return Response({"error": "text is required"}, status=400)

    # (We will add real AI summarization later)
    short = text[:50] + "..." if len(text) > 50 else text

    return Response({
        "summary": short
    })


#chat

@api_view(["POST"])
def chat(request):
    message = request.data.get("message", "").lower()

    if not message:
        return Response({"error": "message is required"}, status=400)

    # English
    if "hello" in message or "hi" in message:
        reply = "Hi! How can I help you?"
    elif "how are you" in message:
        reply = "I'm doing great! Thanks for asking."
    elif "bye" in message:
        reply = "Goodbye! Have a nice day!"

    # French
    elif "bonjour" in message:
        reply = "Bonjour ! Comment puis-je vous aider ?"
    elif "salut" in message:
        reply = "Salut ! Comment ça va ?"
    elif "ça va" in message or "ca va" in message:
        reply = "Je vais bien, merci !"
    elif "au revoir" in message:
        reply = "Au revoir ! Bonne journée !"

    # Arabic
    elif "السلام" in message or "سلام" in message:
        reply = "وعليكم السلام! كيف أستطيع مساعدتك؟"
    elif "مرحبا" in message or "اهلا" in message:
        reply = "أهلاً! كيف يمكنني مساعدتك؟"
    elif "كيف حالك" in message:
        reply = "أنا بخير! شكرًا لسؤالك."
    elif "مع السلامة" in message:
        reply = "مع السلامة! أتمنى لك يومًا سعيدًا!"

    else:
        reply = "Sorry, I didn't understand that."

    return Response({"response": reply})