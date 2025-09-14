from rest_framework import generics, permissions
from .models import Provider
from .serializers import ProviderSerializer, ProviderUpdateSerializer

# Admin can edit active status
class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff

# Retrieve & Update provider
class ProviderRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Provider.objects.all()
    permission_classes = [permissions.AllowAny]  # keep this if public, else use IsAuthenticated

    # Use different serializer for read vs update
    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH']:
            return ProviderUpdateSerializer
        return ProviderSerializer

    def get_permissions(self):
        # Only admin can change "active"
        if self.request.method in ['PATCH', 'PUT'] and 'active' in self.request.data:
            return [IsAdmin()]
        return super().get_permissions()
    
# List all providers
class ProviderListAPIView(generics.ListAPIView):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer
    # permission_classes = [permissions.IsAuthenticated]
    permission_classes = [permissions.AllowAny]

# Create a provider
class ProviderCreateAPIView(generics.CreateAPIView):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer
    # permission_classes = [permissions.IsAuthenticated]
    permission_classes = [permissions.AllowAny]

# Retrieve a provider
class ProviderDetailAPIView(generics.RetrieveAPIView):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer
    # permission_classes = [permissions.IsAuthenticated]
    permission_classes = [permissions.AllowAny]

# Update a provider (including active, restricted to admin)
class ProviderUpdateAPIView(generics.UpdateAPIView):
    queryset = Provider.objects.all()
    serializer_class = ProviderUpdateSerializer 
    # permission_classes = [permissions.IsAuthenticated]
    permission_classes = [permissions.AllowAny]

    def get_permissions(self):
        if 'active' in self.request.data:
            return [IsAdmin()]
        return super().get_permissions()