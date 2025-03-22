from django.http import HttpResponse
from django.contrib.auth.decorators import user_passes_test, login_required

# Función para verificar si el usuario es administrador
def es_admin(user):
    return user.groups.filter(name="Administrador").exists()

# Función para verificar si el usuario es editor
def es_editor(user):
    return user.groups.filter(name="Editor").exists()

# Vista para administradores
@user_passes_test(es_admin)
def dashboard_admin(request):
    return HttpResponse("Bienvenido al panel de administrador")

# Vista para editores
@user_passes_test(es_editor)
def editar_articulo(request):
    return HttpResponse("Acceso permitido solo a editores")

# Vista para usuarios registrados
@login_required
def ver_articulo(request):
    return HttpResponse("Acceso permitido a usuarios registrados")

# Vista de inicio para todos
def inicio(request):
    return HttpResponse("Página de inicio - Accesible para todos")