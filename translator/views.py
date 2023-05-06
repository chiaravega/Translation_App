from django.shortcuts import render
from translate import Translator





def home(request):
    return render(request, "home.html")





def all(request):
    if request.method == "POST":
        text = request.POST["translate"]
        language = request.POST["language"]

        translator = Translator(to_lang=language)
        translation = translator.translate(text)

        return render(request, 'all.html', {"result":translation})
        
    return render(request, "all.html")





def chineses(request):
    if request.method == "POST":
        text = request.POST["translate"]
        language = request.POST["language"]

        translator = Translator(to_lang=language)
        translation = translator.translate(text)

        return render(request, 'chineses.html', {"result":translation})

    return render(request, "chineses.html")





def french(request):
    if request.method == "POST":
        text = request.POST["translate"]
        language = request.POST["language"]

        translator = Translator(to_lang=language)
        translation = translator.translate(text)

        return render(request, 'french.html', {"result":translation})

    return render(request, "french.html")





def german(request):
    if request.method == "POST":
        text = request.POST["translate"]
        language = request.POST["language"]

        translator = Translator(to_lang=language)
        translation = translator.translate(text)

        return render(request, 'german.html', {"result":translation})

    return render(request, "german.html")





def italian(request):
    if request.method == "POST":
        text = request.POST["translate"]
        language = request.POST["language"]

        translator = Translator(to_lang=language)
        translation = translator.translate(text)

        return render(request, 'italian.html', {"result":translation})

    return render(request, "italian.html")





def japanese(request):
    if request.method == "POST":
        text = request.POST["translate"]
        language = request.POST["language"]

        translator = Translator(to_lang=language)
        translation = translator.translate(text)

        return render(request, 'japanese.html', {"result":translation})

    return render(request, "japanese.html")





def korean(request):
    if request.method == "POST":
        text = request.POST["translate"]
        language = request.POST["language"]

        translator = Translator(to_lang=language)
        translation = translator.translate(text)

        return render(request, 'korean.html', {"result":translation})

    return render(request, "korean.html")





def spanish(request):
    if request.method == "POST":
        text = request.POST["translate"]
        language = request.POST["language"]

        translator = Translator(to_lang=language)
        translation = translator.translate(text)

        return render(request, 'spanish.html', {"result":translation})

    return render(request, "spanish.html")

