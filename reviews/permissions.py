from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOwnerOfPropertyForReviewDelete(BasePermission):  # 1. Only the owner of the property (landlord) can delete a review.
                                                         #2. Everyone can read.
                                                         # 3. Only authenticated users can add
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True                                #everyone reads
        if request.method == 'POST':
            return request.user and request.user.is_authenticated  # only authenticated
        return True

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.property.owner == request.user