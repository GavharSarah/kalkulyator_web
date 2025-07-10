from django.shortcuts import render


from django.shortcuts import render, redirect


def calculator_view(request):
    result = None

    if request.method == "POST":
        num1 = float(request.POST.get("num1"))
        num2 = float(request.POST.get("num2"))
        operation = request.POST.get("operation")

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            result = num1 / num2 if num2 != 0 else "Division by zero!"

        history = request.session.get("history", [])
        history.append(f"{num1} {operation} {num2} = {result}")
        request.session["history"] = history

    return render(request, "index.html", {"result": result})

def history_view(request):
    history = request.session.get("history", [])
    return render(request, "history.html", {"history": history})
