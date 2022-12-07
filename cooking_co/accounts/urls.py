from django.urls import path, include

from cooking_co.accounts.views import SignUpView, SignInView, SignOutView, UserEditView, UserDeleteView, UserDetailsView

urlpatterns = [
    path('sign-up/', SignUpView.as_view(), name='sign up'),
    # path('sign-in/', sign_in, name='sign in'),
    path('sign-in/', SignInView.as_view(), name='sign in'),
    path('sign-out/', SignOutView.as_view(), name='sign out'),
    path('profile/', include([
        path('details/<int:pk>/', UserDetailsView.as_view(), name='user details'),
        path('edit/<int:pk>/', UserEditView.as_view(), name='user edit'),
        path('delete/<int:pk>/', UserDeleteView.as_view(), name='user delete'),
    ])),
]
