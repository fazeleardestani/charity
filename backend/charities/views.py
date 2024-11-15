from rest_framework import status, generics
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated, SAFE_METHODS
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.permissions import IsCharityOwner, IsBenefactor
from charities.models import Task
from charities.serializers import (
    TaskSerializer, CharitySerializer, BenefactorSerializer
)


class BenefactorRegistration(APIView):
    def post(self, request):
        serializer = BenefactorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response( serializer.data, status=status.HTTP_201_CREATED)

class CharityRegistration(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        serializer = CharitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response( serializer.data, status=status.HTTP_201_CREATED)

class Tasks(generics.ListCreateAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.all_related_tasks_to_user(self.request.user)

    def post(self, request, *args, **kwargs):
        data = {
            **request.data,
            "charity_id": request.user.charity.id
        }
        serializer = self.serializer_class(data = data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            self.permission_classes = [IsAuthenticated, ]
        else:
            self.permission_classes = [IsCharityOwner, ]

        return [permission() for permission in self.permission_classes]

    def filter_queryset(self, queryset):
        filter_lookups = {}
        for name, value in Task.filtering_lookups:
            param = self.request.GET.get(value)
            if param:
                filter_lookups[name] = param
        exclude_lookups = {}
        for name, value in Task.excluding_lookups:
            param = self.request.GET.get(value)
            if param:
                exclude_lookups[name] = param

        return queryset.filter(**filter_lookups).exclude(**exclude_lookups)

class TaskRequest(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request, task_id):
        if not request.user.is_benefactor:
            return Response(status=status.HTTP_403_FORBIDDEN,
                            data={'detail': 'User is not a benefactor.'})

        task = get_object_or_404(Task, id=task_id)
        if task.state != Task.TaskStatus.PENDING:
            return Response(status=status.HTTP_404_NOT_FOUND,
                            data={'detail': 'This task is not pending.'})

        task.assign_to_benefactor(request.user.benefactor)
        task.save()

        return Response(status=status.HTTP_200_OK,
                        data={'detail': 'Request sent.'})

class TaskResponse(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request, task_id):

        if not request.user.is_charity:
            return Response(status=status.HTTP_403_FORBIDDEN,
                            data={'detail': 'User does not have permission to access this resource.'})

        task = get_object_or_404(Task, id=task_id)
        check_status = request.data.get("response")

        if check_status not in ['A' , 'R']:
            return Response(status=status.HTTP_400_BAD_REQUEST ,
                        data={'detail': 'Required field ("A" for accepted / "R" for rejected)'})

        if task.state != Task.TaskStatus.WAITING:
            return Response(status=status.HTTP_404_NOT_FOUND,
                            data={'detail': 'This task is not waiting.'})

        task.response_to_benefactor_request(check_status)

        return Response(status=status.HTTP_200_OK,
                            data={'detail': 'Response sent.'})


class DoneTask(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request, task_id):
        if not request.user.is_charity:
            return Response(status=status.HTTP_403_FORBIDDEN,
                            data={'detail': 'User does not have permission to access this resource.'})

        task = get_object_or_404(Task, id=task_id)
        if task.state != Task.TaskStatus.ASSIGNED:
            return Response(status=status.HTTP_404_NOT_FOUND,
                            data={'detail': 'Task is not assigned yet.'})
        task.state = Task.TaskStatus.DONE
        task.save()
        return Response(status=status.HTTP_200_OK,
                        data={'detail': 'Task has been done successfully.'})
    