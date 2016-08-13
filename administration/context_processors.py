from .models import Company, StartPage

def company_processor(request):
    try:
        company = Company.load()
    except Company.DoesNotExist:
        company = None
    return {'company': company}

def pictures_processor(request):
    try:
        start_page = StartPage.load()
    except StartPage.DoesNotExist:
        start_page = None
    return {'start_page': start_page}