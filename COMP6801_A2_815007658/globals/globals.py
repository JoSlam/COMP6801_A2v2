def get_context(request):
    context = {}
    context.update({ "user": request.user if request.user else None })
    return context

def update_context(context, key, value):
    context[key] = value