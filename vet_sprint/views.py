
from django.shortcuts import render, redirect, get_object_or_404
from .models import Propietario, Mascota, Cita, Medicamento, Cirugia, BitacoraConsulta
from django.forms import ModelForm
from django import forms 
import csv
from django.http import HttpResponse



class PropietarioForm(ModelForm):
    class Meta:
        model = Propietario
        fields = ['nombre', 'telefono', 'direccion']

class MascotaForm(ModelForm):
    class Meta:
        model = Mascota
        fields = ['nombre', 'especie', 'raza', 'edad', 'propietario']

class CitaForm(ModelForm):
    class Meta:
        model = Cita
        fields = ['fecha', 'motivo', 'diagnostico', 'mascota']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}), 
        }
class MedicamentoForm(ModelForm):
    class Meta:
        model = Medicamento
        fields = ['nombre', 'descripcion', 'cantidad', 'fecha_vencimiento']
        widgets = {
            'fecha_vencimiento': forms.DateInput(attrs={'type': 'date'}), 
        }
class CirugiaForm(ModelForm):
    class Meta:
        model = Cirugia
        fields = ['fecha', 'descripcion', 'mascota', 'veterinario']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}), 
        }

class BitacoraConsultaForm(ModelForm):
    class Meta:
        model = BitacoraConsulta
        # No incluimos 'fecha_consulta' porque se genera automáticamente (auto_now_add=True)
        # No incluimos 'mascota' en el formulario directo, ya que lo pasaremos en la URL
        fields = ['observaciones', 'diagnostico', 'tratamiento', 'veterinario']
def home(request):
    """
    Página de bienvenida
    """
    return render(request, 'vet_sprint/home.html', {'nombre_clinica': 'Clínica Veterinaria Amigos Peludos'})

def services(request):
    """
    Página de servicios
    """
    context = {
        'titulo': 'Nuestros Servicios Veterinarios',
        'servicios_list': [
            'Consultas generales y vacunación',
            'Registros de usuarios y mascotas',
            'Manejo de información de personas y mascotas',
            'Eliminación de usuarios',
            'Gestión de citas', # Servicio adicional
            'Gestión de medicamentos y cirugías',
            'Exportación de datos de mascotas y propietarios'
        ],
        'descripcion_adicional': 'Ofrecemos el mejor cuidado para tus mascotas.'
    }
    return render(request, 'vet_sprint/service.html', context)

def dynamic_content_placeholder(request):
    """
    Página con placeholders - Ahora redirige a la lista de propietarios.
    """
    return redirect('propietarios_list')

def ver_exportaciones(request):
    """ 
    Página para ver las exportaciones disponibles.
    """
    mascotas = Mascota.objects.all()
    propietarios = Propietario.objects.all()
    return render(request, 'vet_sprint/exportaciones.html', {'mascotas': mascotas, 'propietarios': propietarios})
#gestión de Propietarios
def propietarios_list(request):
    """
    Muestra una lista de todos los propietarios.
    """
    propietarios = Propietario.objects.all()
    return render(request, 'vet_sprint/propietarios_list.html', {'propietarios': propietarios})

def propietario_create(request):
    """
    Permite crear un nuevo propietario.
    """
    if request.method == 'POST':
        form = PropietarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('propietarios_list')
    else:
        form = PropietarioForm()
    return render(request, 'vet_sprint/propietario_form.html', {'form': form, 'accion': 'Crear'})

def propietario_update(request, pk):
    """
    Permite actualizar un propietario existente.
    """
    propietario = get_object_or_404(Propietario, pk=pk)
    if request.method == 'POST':
        form = PropietarioForm(request.POST, instance=propietario)
        if form.is_valid():
            form.save()
            return redirect('propietarios_list')
    else:
        form = PropietarioForm(instance=propietario)
    return render(request, 'vet_sprint/propietario_form.html', {'form': form, 'accion': 'Actualizar'})

def propietario_delete(request, pk):
    """
    Permite eliminar un propietario.
    """
    propietario = get_object_or_404(Propietario, pk=pk)
    if request.method == 'POST':
        propietario.delete()
        return redirect('propietarios_list')
    return render(request, 'vet_sprint/propietario_confirm_delete.html', {'propietario': propietario})

def exportar_propietarios_csv(request):
    # Crear la respuesta con tipo MIME para CSV
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="clientes.csv"'

    writer = csv.writer(response)
    # Escribir la cabecera
    writer.writerow(['ID', 'Nombre', 'Teléfono', 'Dirección'])

    # Escribir los datos
    for propietario in Propietario.objects.all():
        writer.writerow([propietario.id, propietario.nombre, propietario.telefono, propietario.direccion])

    return response

# gestión de Mascotas
def mascotas_list(request):
    """
    Muestra una lista de todas las mascotas.
    """
    mascotas = Mascota.objects.all()
    return render(request, 'vet_sprint/mascotas_list.html', {'mascotas': mascotas})

def mascota_create(request):
    """
    Permite crear una nueva mascota.
    """
    if request.method == 'POST':
        form = MascotaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mascotas_list')
    else:
        form = MascotaForm()
    return render(request, 'vet_sprint/mascota_form.html', {'form': form, 'accion': 'Crear'})

def mascota_update(request, pk):
    """
    Permite actualizar una mascota existente.
    """
    mascota = get_object_or_404(Mascota, pk=pk)
    if request.method == 'POST':
        form = MascotaForm(request.POST, instance=mascota)
        if form.is_valid():
            form.save()
            return redirect('mascotas_list')
    else:
        form = MascotaForm(instance=mascota)
    return render(request, 'vet_sprint/mascota_form.html', {'form': form, 'accion': 'Actualizar'})

def mascota_delete(request, pk):
    """
    Permite eliminar una mascota.
    """
    mascota = get_object_or_404(Mascota, pk=pk)
    if request.method == 'POST':
        mascota.delete()
        return redirect('mascotas_list')
    return render(request, 'vet_sprint/mascota_confirm_delete.html', {'mascota': mascota})

def exportar_mascotas_csv(request):
    """
    Exporta la lista de mascotas a un archivo CSV.
    """
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="mascotas.csv"'

    writer = csv.writer(response)
    # Escribir la cabecera
    writer.writerow(['ID', 'Nombre', 'Especie', 'Raza', 'Edad', 'Propietario'])

    # Escribir los datos
    for mascota in Mascota.objects.all():
        writer.writerow([mascota.id, mascota.nombre, mascota.especie, mascota.raza, mascota.edad, mascota.propietario.nombre])

    return response

#Gestión de Cita
def citas_list(request):
    """
    Muestra una lista de todas las citas.
    """
    citas = Cita.objects.all()
    return render(request, 'vet_sprint/citas_list.html', {'citas': citas})

def cita_create(request):
    """
    Permite agendar una nueva cita.
    """
    if request.method == 'POST':
        form = CitaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('citas_list')
    else:
        form = CitaForm()
    return render(request, 'vet_sprint/cita_form.html', {'form': form, 'accion': 'Crear'})

def cita_update(request, pk):
    """
    Permite actualizar una cita existente.
    """
    cita = get_object_or_404(Cita, pk=pk)
    if request.method == 'POST':
        form = CitaForm(request.POST, instance=cita)
        if form.is_valid():
            form.save()
            return redirect('citas_list')
    else:
        form = CitaForm(instance=cita)
    return render(request, 'vet_sprint/cita_form.html', {'form': form, 'accion': 'Actualizar'})

def cita_delete(request, pk):
    """
    Permite eliminar una cita.
    """
    cita = get_object_or_404(Cita, pk=pk)
    if request.method == 'POST':
        cita.delete()
        return redirect('citas_list')
    return render(request, 'vet_sprint/cita_confirm_delete.html', {'cita': cita})

#Gestion de Medicamentos

def medicamentos_list(request):
    """
    Muestra una lista de todos los medicamentos.
    """
    medicamentos = Medicamento.objects.all()
    return render(request, 'vet_sprint/medicamentos_list.html', {'medicamentos': medicamentos})

def medicamento_create(request):
    """ 
    Permite crear un nuevo medicamento.
    """
    if request.method == 'POST':
        form = MedicamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('medicamentos_list')
    else:
        form = MedicamentoForm()
    return render(request, 'vet_sprint/medicamento_form.html', {'form': form, 'accion': 'Crear'})

def medicamento_update(request, pk):
    """
    Permite actualizar un medicamento existente.
    """
    medicamento = get_object_or_404(Medicamento, pk=pk)
    if request.method == 'POST':
        form = MedicamentoForm(request.POST, instance=medicamento)
        if form.is_valid():
            form.save()
            return redirect('medicamentos_list')
    else:
        form = MedicamentoForm(instance=medicamento)
    return render(request, 'vet_sprint/medicamento_form.html', {'form': form, 'accion': 'Actualizar'})

def medicamento_delete(request, pk):
    """
    Permite eliminar un medicamento.
    """
    medicamento = get_object_or_404(Medicamento, pk=pk)
    if request.method == 'POST':
        medicamento.delete()
        return redirect('medicamentos_list')
    return render(request, 'vet_sprint/medicamento_confirm_delete.html', {'medicamento': medicamento})

#Gestion de Cirugias
def cirugias_list(request):
    """
    Muestra una lista de todas las cirugías.
    """
    cirugias = Cirugia.objects.all()
    return render(request, 'vet_sprint/cirugias_list.html', {'cirugias': cirugias})

def cirugia_create(request):
    """
    Permite crear una nueva cirugía.
    """
    if request.method == 'POST':
        form = CirugiaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cirugias_list')
    else:
        form = CirugiaForm()
    return render(request, 'vet_sprint/cirugia_form.html', {'form': form, 'accion': 'Crear'})

def cirugia_update(request, pk):
    """
    Permite actualizar una cirugía existente.
    """
    cirugia = get_object_or_404(Cirugia, pk=pk)
    if request.method == 'POST':
        form = CirugiaForm(request.POST, instance=cirugia)
        if form.is_valid():
            form.save()
            return redirect('cirugias_list')
    else:
        form = CirugiaForm(instance=cirugia)
    return render(request, 'vet_sprint/cirugia_form.html', {'form': form, 'accion': 'Actualizar'})

def cirugia_delete(request, pk):
    """
    Permite eliminar una cirugía.
    """
    cirugia = get_object_or_404(Cirugia, pk=pk)
    if request.method == 'POST':
        cirugia.delete()
        return redirect('cirugias_list')
    return render(request, 'vet_sprint/cirugia_confirm_delete.html', {'cirugia': cirugia})
 


# Bitácoras

def bitacoras_list(request, mascota_pk):
    """
    Muestra una lista de todas las bitácoras para una mascota específica.
    """
    mascota = get_object_or_404(Mascota, pk=mascota_pk)
    bitacoras = mascota.bitacoras.all() # Accede a las bitácoras a través de la relación inversa
    return render(request, 'vet_sprint/bitacoras_list.html', {'mascota': mascota, 'bitacoras': bitacoras})

def bitacora_create(request, mascota_pk):
    """
    Permite registrar una nueva bitácora de consulta para una mascota específica.
    """
    mascota = get_object_or_404(Mascota, pk=mascota_pk)
    if request.method == 'POST':
        form = BitacoraConsultaForm(request.POST)
        if form.is_valid():
            bitacora = form.save(commit=False) # No guarda aún para asignar la mascota
            bitacora.mascota = mascota # Asigna la mascota a la bitácora
            bitacora.save()
            return redirect('bitacoras_list', mascota_pk=mascota.pk) # Redirige a la lista de bitácoras de esa mascota
    else:
        form = BitacoraConsultaForm()
    return render(request, 'vet_sprint/bitacora_form.html', {'form': form, 'mascota': mascota, 'accion': 'Registrar'})

def bitacora_detail(request, mascota_pk, pk):
    """
    Muestra los detalles de una bitácora de consulta específica.
    """
    mascota = get_object_or_404(Mascota, pk=mascota_pk)
    bitacora = get_object_or_404(BitacoraConsulta, pk=pk, mascota=mascota) # Asegura que la bitácora pertenezca a la mascota
    return render(request, 'vet_sprint/bitacora_detail.html', {'bitacora': bitacora, 'mascota': mascota})

def bitacora_update(request, mascota_pk, pk):
    """
    Permite actualizar una bitácora de consulta existente.
    """
    mascota = get_object_or_404(Mascota, pk=mascota_pk)
    bitacora = get_object_or_404(BitacoraConsulta, pk=pk, mascota=mascota)
    if request.method == 'POST':
        form = BitacoraConsultaForm(request.POST, instance=bitacora)
        if form.is_valid():
            form.save()
            return redirect('bitacoras_list', mascota_pk=mascota.pk)
    else:
        form = BitacoraConsultaForm(instance=bitacora)
    return render(request, 'vet_sprint/bitacora_form.html', {'form': form, 'mascota': mascota, 'accion': 'Actualizar'})

def bitacora_delete(request, mascota_pk, pk):
    """
    Permite eliminar una bitácora de consulta.
    """
    mascota = get_object_or_404(Mascota, pk=mascota_pk)
    bitacora = get_object_or_404(BitacoraConsulta, pk=pk, mascota=mascota)
    if request.method == 'POST':
        bitacora.delete()
        return redirect('bitacoras_list', mascota_pk=mascota.pk)
    return render(request, 'vet_sprint/bitacora_confirm_delete.html', {'bitacora': bitacora, 'mascota': mascota})

def historia_clinica(request, mascota_pk):
    """
    Genera y muestra la historia clínica completa de una mascota.
    """
    mascota = get_object_or_404(Mascota, pk=mascota_pk)
    bitacoras = mascota.bitacoras.all()
    citas = mascota.citas.all()
    cirugias = mascota.cirugias.all()

    context = {
        'mascota': mascota,
        'bitacoras': bitacoras,
        'citas': citas,
        'cirugias': cirugias,
    }
    return render(request, 'vet_sprint/historia_clinica.html', context)