from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .models import NameDetails
from .serializers import NameDetailsSerializer


class NameDetailsList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        name_d_obj = NameDetails.objects.all()
        serializer_obj = NameDetailsSerializer(name_d_obj, many=True)
        return Response(serializer_obj.data)

    def post(self, request):
        serializer_obj = NameDetailsSerializer(data=request.data)
        if serializer_obj.is_valid():
            serializer_obj.save()
            return Response(serializer_obj.data, status=status.HTTP_201_CREATED)
        return Response(serializer_obj.errors, status=status.HTTP_400_BAD_REQUEST)


class NameDetailsDetails(APIView):

    def get_object(self, pk):
        try:
            return NameDetails.objects.get(id=pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        name_detail_obj = self.get_object(pk)
        serializer_obj = NameDetailsSerializer(name_detail_obj)
        return Response(serializer_obj.data)

    def put(self, request, pk):
        name_detail_obj = self.get_object(pk)
        serializer_obj = NameDetailsSerializer(name_detail_obj,
                                               data=request.data)
        if serializer_obj.is_valid():
            serializer_obj.save()
            return Response(serializer_obj.data)
        return Response(serializer_obj.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        name_detail_obj = self.get_object(pk)
        name_detail_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
