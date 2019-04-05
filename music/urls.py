from django.urls import path
from . import views



app_name= 'music'
urlpatterns = [
    path('signup',views.signup, name='signup'),
    path('login',views.signin, name='signin'),
    path('logout',views.logout_user, name='logout'),
    path('',views.index, name='index'),
    path('(?p<album_id>[0-9]+)',views.detail,name='detail'),
    path('new-album',views.create_album,name='create-album'),
    path('<int:pk>/update-album',views.AlbumUpdateView.as_view(), name='album-update'),
    path('(?p<album_id>[0-9]+)/delete-album',views.album_delete, name='album-delete'),
    path('(?p<album_id>[0-9]+)/new-song',views.create_song, name='new-song'),
    path('<int:pk>/song-update',views.SongUpdateView.as_view(),name='song-update'),
    path('(?p<album_id>[0-9]+)/delete-song/(?<song_id>[0-9]+)/',views.delete_song, name='song-delete'),

]
