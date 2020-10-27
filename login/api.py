from rest_framework.viewsets import ModelViewSet
from login.serializers import UserModelSerializer,MessageModelSerializer
from Home.models import Profile,MessageModel
from socialmedia import settings
from rest_framework.authentication import SessionAuthentication
from rest_framework.pagination import PageNumberPagination



class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        return

class MessagePagination(PageNumberPagination):
    page_size = settings.MESSAGES_TO_LOAD

# ----------temprary
class MessageModelViewSet(ModelViewSet):
    queryset = MessageModel.objects.all()
    print(queryset)
    # serializer_class = MessageModelSerializer
    allowed_methods = ('GET', 'POST', 'HEAD', 'OPTIONS')
    authentication_classes = (CsrfExemptSessionAuthentication,)
    pagination_class = MessagePagination
    # userid = request.session["user"]
    # usr = Profile.objects.get(profile_id=userid)
    print("profile fname................")

    def list(self, request, *args, **kwargs):
        print(".......................")
        self.queryset = self.queryset.filter(Q(recipient=request.Profile) |
                                             Q(user=request.Profile))
        target = self.request.query_params.get('target', None)
        if target is not None:
            self.queryset = self.queryset.filter(
                Q(recipient=request.Profile, user__username=target) |
                Q(recipient__username=target, user=request.Profile))
        return super(MessageModelViewSet, self).list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        msg = get_object_or_404(
            self.queryset.filter(Q(recipient=request.user) |
                                 Q(user=request.user),
                                 Q(pk=kwargs['pk'])))
        serializer = self.get_serializer(msg)
        print(msg, serializer)
        
        return Response(serializer.data)

# ----------temprary


class UserModelViewSet(ModelViewSet):
    queryset = Profile.objects.all()
    print(queryset)
    serializer_class = UserModelSerializer
    allowed_methods = ('GET', 'HEAD', 'OPTIONS')
    pagination_class = None  # Get all user

    def list(self, request, *args, **kwargs):
        # Get all users except yourself
        userid = request.session["user"]
        self.queryset = self.queryset.exclude(profile_id=userid)
        return super(UserModelViewSet, self).list(request, *args, **kwargs)


