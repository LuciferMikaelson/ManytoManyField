from rest_framework import viewsets
from rest_framework.response import Response
from school.models import Students, Modules
from .serializer import StudentsSerializer, ModulesSerializer


class StudentsViewSet(viewsets.ModelViewSet):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer


    # def create(self, validated_data):
    #     modules_data = validated_data.pop('modules')
    #     student = Students.objects.create(**validated_data)
        
    #     # import pdb; pdb.set_trace()
    #     for module_data in modules_data:
    #         Modules.objects.create(student = student, module = module_data)
    #     return student

    def create(self, request, *args, **kwargs):
        new_student = StudentsSerializer(data=request.data)
        new_student.is_valid(raise_exception=True)
        new_student.save()

        # import pdb; pdb.set_trace()
        # for module in request.data["modules"]:
        #     module_obj = Modules.objects.get(id=module["id"])
        #     new_student.modules.add(module_obj)

        return Response(new_student.data)

    # def create(self, request, *args, **kwargs):
    #     data = request.data

    #     new_student = Students.objects.create(name=data["name"], age=data['age'], grade=data["grade"])

    #     new_student.save()

    #     for module in data["modules"]:
    #         module_obj = Modules.objects.get(id=module["id"])
    #         new_student.modules.add(module_obj)

    #     serializer = StudentsSerializer(new_student)

    #     return Response(serializer.data)


class ModulesViewSet(viewsets.ModelViewSet):
    queryset = Modules.objects.all()
    serializer_class = ModulesSerializer