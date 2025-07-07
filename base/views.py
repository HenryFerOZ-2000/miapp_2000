from django.shortcuts import render
from .models import Operacion

def menu(request):
    return render(request, 'base/menu.html')

def calculadora(request):
    resultado = None
    historial = Operacion.objects.all().order_by('-fecha')[:5]

    if request.method == 'POST':
        num1 = float(request.POST.get('num1', 0))
        num2 = float(request.POST.get('num2', 0))
        operacion = request.POST.get('operacion')

        if operacion == 'sumar':
            resultado = num1 + num2
        elif operacion == 'restar':
            resultado = num1 - num2
        elif operacion == 'multiplicar':
            resultado = num1 * num2
        elif operacion == 'dividir':
            resultado = "No se puede dividir por cero" if num2 == 0 else num1 / num2

        # Guardar en la base de datos
        Operacion.objects.create(
            num1=num1,
            num2=num2,
            operacion=operacion,
            resultado=str(resultado)
        )

        # Actualizar historial
        historial = Operacion.objects.all().order_by('-fecha')[:5]

    return render(request, 'base/calculadora.html', {'resultado': resultado, 'historial': historial})

    return render(request, 'base/calculadora.html', {'resultado': resultado})

def texto(request):
    resultado = ''
    if request.method == 'POST':
        texto_ingresado = request.POST.get('texto', '')
        accion = request.POST.get('accion')
        if accion == 'mayusculas':
            resultado = texto_ingresado.upper()
        elif accion == 'minusculas':
            resultado = texto_ingresado.lower()
    return render(request, 'base/texto.html', {'resultado': resultado})

