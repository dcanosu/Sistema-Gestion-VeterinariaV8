# vet_sprint/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # URL
    path('', views.home, name='home'),
    path('servicios/', views.services, name='services'),
    path('informacion/', views.dynamic_content_placeholder, name='dynamic_placeholder'), # Ajustado el nombre de la URL
    path('exportaciones/', views.ver_exportaciones, name='ver_exportaciones'),

    # URL Propietarios
    path('propietarios/', views.propietarios_list, name='propietarios_list'),
    path('propietarios/crear/', views.propietario_create, name='propietario_create'),
    path('propietarios/actualizar/<int:pk>/', views.propietario_update, name='propietario_update'),
    path('propietarios/eliminar/<int:pk>/', views.propietario_delete, name='propietario_delete'),
    path('exportar_propietarios/', views.exportar_propietarios_csv, name='exportar_propietarios_csv'),

    # URL Mascotas
    path('mascotas/', views.mascotas_list, name='mascotas_list'),
    path('mascotas/crear/', views.mascota_create, name='mascota_create'),
    path('mascotas/actualizar/<int:pk>/', views.mascota_update, name='mascota_update'),
    path('mascotas/eliminar/<int:pk>/', views.mascota_delete, name='mascota_delete'),
    path('exportar_mascotas/', views.exportar_mascotas_csv, name='exportar_mascotas_csv'),

    # URL Citas
    path('citas/', views.citas_list, name='citas_list'),
    path('citas/crear/', views.cita_create, name='cita_create'),
    path('citas/actualizar/<int:pk>/', views.cita_update, name='cita_update'),
    path('citas/eliminar/<int:pk>/', views.cita_delete, name='cita_delete'),

    # URL Medicamentos
    path('medicamentos/', views.medicamentos_list, name='medicamentos_list'),
    path('medicamentos/crear/', views.medicamento_create, name='medicamento_create'),
    path('medicamentos/actualizar/<int:pk>/', views.medicamento_update, name='medicamento_update'),
    path('medicamentos/eliminar/<int:pk>/', views.medicamento_delete, name='medicamento_delete'),

    # URL Cirugías
    path('cirugias/', views.cirugias_list, name='cirugias_list'),
    path('cirugias/crear/', views.cirugia_create, name='cirugia_create'),
    path('cirugias/actualizar/<int:pk>/', views.cirugia_update, name='cirugia_update'),
    path('cirugias/eliminar/<int:pk>/', views.cirugia_delete, name='cirugia_delete'),

 # URL Bitácoras
   
    path('mascotas/<int:mascota_pk>/bitacoras/', views.bitacoras_list, name='bitacoras_list'),
    path('mascotas/<int:mascota_pk>/bitacoras/crear/', views.bitacora_create, name='bitacora_create'),
    path('mascotas/<int:mascota_pk>/bitacoras/<int:pk>/', views.bitacora_detail, name='bitacora_detail'),
    path('mascotas/<int:mascota_pk>/bitacoras/actualizar/<int:pk>/', views.bitacora_update, name='bitacora_update'),
    path('mascotas/<int:mascota_pk>/bitacoras/eliminar/<int:pk>/', views.bitacora_delete, name='bitacora_delete'),
    
    # URL Historia Clínica
    path('mascotas/<int:mascota_pk>/historia_clinica/', views.historia_clinica, name='historia_clinica'),

]