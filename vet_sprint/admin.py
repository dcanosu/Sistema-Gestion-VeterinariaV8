from django.contrib import admin
from .models import Mascota
from .models import Propietario
from .models import Cita   
from .models import Medicamento
from .models import Cirugia

# Registra los modelos en el panel de administración de Django
admin.site.register(Propietario)
admin.site.register(Cita)
admin.site.register(Mascota)
admin.site.register(Medicamento)
admin.site.register(Cirugia)
