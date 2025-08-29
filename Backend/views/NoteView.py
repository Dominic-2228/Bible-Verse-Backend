from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from django.http import HttpResponseServerError
from rest_framework import status
from Backend.models import Note
from Backend.serializers import NoteSerializer
from rest_framework import viewsets, status, permissions
from django.shortcuts import get_object_or_404

class NoteView(ViewSet):
  def list(self, request):
    try:
      note = Note.objects.all()
      serializer = NoteSerializer(note, many=True)
      return Response(serializer.data, status=status.HTTP_200_OK)

    except Exception as ex:
      return HttpResponseServerError(ex)
    
  def retrieve(self, request, pk=None):
        """GET /notes/{id} - Retrieve a single note"""
        try:
            note = get_object_or_404(Note, pk=pk)
            serializer = NoteSerializer(note)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as ex:
            return HttpResponseServerError(ex)

  def create(self, request):
        """POST /notes - Create a new note"""
        try:
            serializer = NoteSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            return HttpResponseServerError(ex)

  def update(self, request, pk=None):
        """PUT /notes/{id} - Update a note"""
        try:
            note = get_object_or_404(Note, pk=pk)
            serializer = NoteSerializer(note, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            return HttpResponseServerError(ex)

  def destroy(self, request, pk=None):
        """DELETE /notes/{id} - Delete a note"""
        try:
            note = get_object_or_404(Note, pk=pk)
            note.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as ex:
            return HttpResponseServerError(ex)