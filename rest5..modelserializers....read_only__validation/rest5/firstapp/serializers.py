# from rest_framework import serializers
# from .models import Student




# class StudentSerializer(serializers.ModelSerializer):
#     # name = serializers.CharField(read_only=True)   can not update this fields
#     class Meta:
#         model = Student
#         fields = ['name','roll', 'city']
#         read_only_fields = ['name', 'roll'] # can not update this fields
#         # extra_kwargs = {'name':{'read_only':True}}  can not update this fields
# validation ar age ai code 


from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(validators = [start_with_r]) same work like above
    class Meta:
       model = Student
       fields = ['name','roll','city']
    
    

    def validate_roll(self, value):
        if value>=200:
            raise serializers.ValidationError('Seat Full')
        return value
    
  


