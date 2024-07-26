from django.shortcuts import render
from coreApp.models import Department
from .serializers import Departmentserializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework import status,parsers
from rest_framework import permissions


#  A ViewSet for handling CRUD operations related to leaves.
class Departmentviewset(ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = Departmentserializer
    parser_classes = (parsers.FormParser,parsers.MultiPartParser,parsers.FileUploadParser)

    def get_serializer_class(self):
        """
        Returns the appropriate serializer class based on the action.
        """
        if self.action == 'list':
            return Departmentserializer
        elif self.action == 'create':
            return Departmentserializer
            
        return self.serializer_class
    
    def list(self, request):
        """
        Retrieve a list of all Department
        """
        try:
            Dept_objs = Department.objects.all()
            serializer = self.get_serializer(Dept_objs, many=True)

            return Response({
                'status': status.HTTP_200_OK,
                'data': serializer.data
            })

        except Exception as e:
            print(e)
            raise APIException({
                'message': APIException.default_detail,
                'status': APIException.status_code
            })
        
#add Department
    def create(self,request):
        try:
            serializer = self.get_serializer(data=request.data)
            if not serializer.is_valid():
                return Response({
                    'status':status.HTTP_400_BAD_REQUEST,
                    'data':serializer.errors,
                    'message':'Invalid data'
                }) 
            serializer.save()

            return Response({
                'status':status.HTTP_201_CREATED,
                'data':serializer.data,
                'message':'Department Added Successfully'
                }) 
        except Exception as e:
            raise APIException({
                'message':APIException.default_detail,
                'status':APIException.status_code
            }) 

    def retrieve(self, request, pk=None):
        """
        Retrieve details of a specific Department
        """
        try:
            id = pk
            if id is not None:
                Dept_objs = self.get_object()
                serializer = self.get_serializer(Dept_objs)

            return Response({
                'status': status.HTTP_200_OK,
                'data': serializer.data
            })

        except Exception as e:
            print(e)
            raise APIException({
                'message': APIException.default_detail,
                'status': APIException.status_code
            })

    def update(self, request, pk=None):
        """
        Update all fields of a specific Department
        """
        try:
            Dept_objs = self.get_object()
            serializer = self.get_serializer(Dept_objs, data=request.data, partial=False)

            if not serializer.is_valid():
                print(serializer.errors)
                return Response({
                    'status': status.HTTP_400_BAD_REQUEST,
                    'data': serializer.errors,
                    'message': 'Invalid data'
                })
            serializer.save()

            return Response({
                'status': status.HTTP_200_OK,
                'data': serializer.data,
                'message': 'Department updated successfully'
            })

        except Exception as e:
            print(e)
            raise APIException({
                'message': APIException.default_detail,
                'status': APIException.status_code
            })
        

    def partial_update(self, request, pk=None):
        """
        Partially update specific fields of Department.
        """
        try:
            Dept_objs = self.get_object()
            serializer = self.get_serializer(Dept_objs, data=request.data, partial=True)

            if not serializer.is_valid():
                print(serializer.errors)
                return Response({
                    'status': status.HTTP_400_BAD_REQUEST,
                    'data': serializer.errors,
                    'message': 'Invalid data'
                })
            serializer.save()

            return Response({
                'status': status.HTTP_200_OK,
                'data': serializer.data,
                'message': 'Department updated successfully'
            })

        except Exception as e:
            print(e)
            raise APIException({
                'message': APIException.default_detail,
                'status': APIException.status_code
            })

    def destroy(self, request, pk):
        """
        Delete a specific Department.
        """
        try:
            id = pk
            Dept_objs = self.get_object()
            Dept_objs.delete()
            return Response({
                'status': status.HTTP_200_OK,
                'message': 'Department deleted successfully'
            })

        except Exception as e:
            print(e)
            raise APIException({
                'message': APIException.default_detail,
                'status': APIException.status_code
            })
                
               




