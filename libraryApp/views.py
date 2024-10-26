from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Students,Books,Library
from .serializers import StudentsSerializer,BooksSerializer,LibrarySerializer
from rest_framework import status
from datetime import date,timedelta

#STUDENTS

@api_view(['GET'])
def list_all_students(request):
    students=Students.objects.all()
    serializer=StudentsSerializer(students,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def add_student(request):
    try:
        if Students.objects.filter(student_id=request.data['student_id']).exists():
            return Response(status=status.HTTP_409_CONFLICT)
        
        serializer=StudentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
def update_student(request,id):
    try:
        student=Students.objects.get(id=id)
        serializer=StudentsSerializer(instance=student,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_student(request,id):
    try:
        student=Students.objects.get(id=id)
        if student:
            student.delete()
            return Response(status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

def get_studentpk_by_studentId(sid):
    student=Students.objects.get(student_id=sid)
    return student.id


#BOOKS

@api_view(['GET'])
def list_all_books(request):
    books=Books.objects.all()
    serializer=BooksSerializer(books,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def add_book(request):
    try:
        if Books.objects.filter(book_id=request.data['book_id']).exists():
            return Response(status=status.HTTP_409_CONFLICT)

        serializer=BooksSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
def update_book(request,id):
    try:
        book=Books.objects.get(id=id)
        serializer=BooksSerializer(instance=book,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_book(request,id):
    try:
        book=Books.objects.get(id=id)
        if book:
            book.delete()
            return Response(status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

def get_bookpk_by_bookId(bid):
    book=Books.objects.get(book_id=bid)
    return book.id



#LIBRARY MEANS STUDENT AND BOOK MASTER COMBINED MASTER

@api_view(['GET'])
def list_all_library(request):
    library=Library.objects.all()
    serializer=LibrarySerializer(library,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def add_library(request): 
    try:
        sid=get_studentpk_by_studentId(request.data['student']) 
        bid=get_bookpk_by_bookId(request.data['book']) 

        if Library.objects.filter(book=bid).exists():
            return Response(status=status.HTTP_409_CONFLICT)
        
        request.data['student']=sid
        request.data['book']=bid
        request.data['issue_date']=date.today()
        request.data['renewal_date']=date.today()+timedelta(days=10)

        serializer=LibrarySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_library_by_bid(request):
    library=Library.objects.get(book=request.data['book'])
    return library.id

@api_view(['PATCH'])
def renewal_book(request,id): 
    try:
        library=Library.objects.get(id=id)
        
        fine=library.fine
        difference_date=(library.renewal_date-library.issue_date).days
        if difference_date<0:
            fine=library.fine+abs(difference_date)*10

        request.data['fine']=fine
        request.data['issue_date']=date.today()
        request.data['renewal_date']=date.today()+timedelta(days=10)

        serializer=LibrarySerializer(instance=library,data=request.data,partial=True)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['PUT'])
def update_library(request,id):
    library=Library.objects.get(id=id)

    serializer=LibrarySerializer(instance=library,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def return_book(request,id):
    try:
        library=Library.objects.get(id=id)
        
        if library:
            library.delete()
            return Response(status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)