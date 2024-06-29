import logging
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .gemini import model

logger = logging.getLogger(__name__)


@api_view(["GET"])
def generate_story(request):
    try:
        question_asked = request.GET.get("prompt")
        if not question_asked:
            return Response(
                {"error": "Prompt parameter is required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        response = model.generate_content(question_asked)
        return Response({"message": response.text}, status=status.HTTP_200_OK)
    except Exception as e:
        logger.error(f"Error generating story: {e}")
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
