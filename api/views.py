from rest_framework.views import APIView
from api.serializers import SendTextSerializer
from api.tasks import send_text as send_text_task
from django.http.response import HttpResponse
from rest_framework.status import HTTP_200_OK


class SendTextView(APIView):

    def post(self, request):
        serializer = SendTextSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        send_text_task.delay(phone_number=data['phone_number'], email=data['email'], text=data['text'])
        return HttpResponse("We will send your text as soon as possible", status=HTTP_200_OK)