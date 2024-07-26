from django.contrib.auth.models import User #User is our model here
from rest_framework import serializers

class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'inpyt_type': 'password'}, write_only=True)

    class Meta:

        model = User
        fields = ['username', 'email', 'password', 'password2']
        extra_kwargs = {
            'password':{'write_only':True}
        }


    def save(self):

        #to validate password

        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'error': 'Provided password are not same!'})
        
        #Validating Email
        if User.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError({'error': 'Email already exists!'})
        
        account =User(email=self.validated_data['email'], username = self.validated_data['username'])
        account.set_password(password)
        account.save()
        return account
