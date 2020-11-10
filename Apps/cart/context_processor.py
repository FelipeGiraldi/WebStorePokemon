def MontoTotalCarrito(request):
    total = 0
    if request.user.is_authenticated:
        for key, value in request.session['cart'].items():
            total = total + (float(value['precio']) * value['cantidad'])
    return {'MontoTotalCarrito': total}
