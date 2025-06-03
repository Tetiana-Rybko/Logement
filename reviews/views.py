from rest_framework import generics
from .models import Review
from .serializers import ReviewSerializer
from .permissions import IsOwnerOfPropertyForReviewDelete



class ReviewListCreateView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsOwnerOfPropertyForReviewDelete]


    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsOwnerOfPropertyForReviewDelete]




