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
    """GET /notes/{id} - Retrieve a single note or related notes"""
    try:
        notes = Note.objects.all()
        single_note = Note.objects.filter(pk=pk).first()
        note_list = [n for n in notes if int(n.user_id) == int(pk)]

        if note_list:  # Found user-related notes
            return Response(
                [NoteSerializer(n).data for n in note_list],
                status=status.HTTP_200_OK
            )

        if single_note:  # Found a single note by pk
            return Response(NoteSerializer(single_note).data, status=status.HTTP_200_OK)

        # If nothing found, return empty with 200 (or 404 if you prefer)
        return Response([], status=status.HTTP_200_OK)

    except Exception as ex:
        # Log error to console for debugging
        import traceback
        print("ERROR in retrieve:", ex)
        traceback.print_exc()

        return HttpResponseServerError(str(ex))


  def create(self, request):
        """POST /notes - Create a new note"""
        try:
            serializer = NoteSerializer(data=request.data)
            if serializer.is_valid():
                note = serializer.save(user=request.user)
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