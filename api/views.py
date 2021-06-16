from rest_framework.permissions import BasePermission, IsAuthenticatedOrReadOnly, SAFE_METHODS
from django.shortcuts import render
from django.http import Http404
from rest_framework.response import Response
from rest_framework.generics import (ListCreateAPIView, ListAPIView, RetrieveAPIView)
from rest_framework import status
from api.models import Mushroom
from api.serializers import FungusSerializer
from rest_framework import generics


class FungusCreateView(ListAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Mushroom.objects.all()
    serializer_class = FungusSerializer


class FungusDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Mushroom.objects.all()
    serializer_class = FungusSerializer

