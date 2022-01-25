from logging import Logger
import logging
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .services import get_lotteries


from .serializers import LotterySerializer
from .models import  Lottery

# Create your views here.
class LotteryView(viewsets.ModelViewSet):
    serializer_class = LotterySerializer
    queryset = Lottery.objects.all()
    
    def lottery_view(self):
        return self.queryset

    @api_view(['GET', 'POST'])
    def lottery_list(self, request):
        if request.method == 'GET':
            lottery = Lottery.objects.all()
            serializer = LotterySerializer(lottery,context={'request': request} ,many=True)
            return Response({'data': serializer.data })
        
        if request.method == 'POST':
            serializer = LotterySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def lottery_api(self, requests):
        lottery_results = get_lotteries()
        serializer = LotterySerializer(data=lottery_results)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        
