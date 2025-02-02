from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import FAQ

class FAQListView(APIView):
    def get(self, request, *args, **kwargs):
        language = request.GET.get("lang", "en")  # Default to English
        faqs = FAQ.objects.all()
        data = [
            {
                "id": faq.id,
                "question": getattr(faq, f"question_{language}", faq.question_en),
                "answer": getattr(faq, f"answer_{language}", faq.answer_en),
            }
            for faq in faqs
        ]
        return Response(data)
