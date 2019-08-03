from django.shortcuts import render
from homeapp.models import Registration
from homeapp.models import Event

# Create your views here.
def home(request):

    queryset = Event.objects.values('status').get(pk=1)
    print(queryset['status'])
    context ={
        'reg_status':'True'
    }
    
    if request.method == 'POST':
        your_name = request.POST.get('your_name')
        father_name = request.POST.get('father_name')
        mother_name = request.POST.get('mother_name')
        nid_number = request.POST.get('nid_number')
        present_address = request.POST.get('present_address')
        parmanent_address = request.POST.get('parmanent_address')
        passing_year = request.POST.get('passing_year')
        dob = request.POST.get('dob')
        blood_group = request.POST.get('blood_group')
        occupation = request.POST.get('occupation')
        batchmate_name = request.POST.get('batchmate_name')
        batchmate_phone_number = request.POST.get('batchmate_phone_number')
        your_phone_number = request.POST.get('your_phone_number')
        your_email = request.POST.get('your_email')
        reg_model = Registration(
            your_name=your_name,
            father_name=father_name,
            mother_name=mother_name,
            nid_number=nid_number,
            present_address=present_address,
            parmanent_address=parmanent_address,
            passing_year=passing_year,
            dob=dob,
            blood_group=blood_group,
            occupation=occupation,
            batchmate_name=batchmate_name,
            batchmate_phone_number=batchmate_phone_number,
            your_phone_number=your_phone_number,
            your_email=your_email,
            #event = Event.objects.values('id').get(pk=1)['id']
        )
        reg_model.save()
        return render(request,'homeapp/index.html',context)

    return render(request,'homeapp/index.html',context)



def about(request):
    return render(request,'homeapp/about.html')



def contact(request):
    return render(request,'homeapp/contact.html')  

def photo_gallery(request):
    return render(request,'homeapp/gallery.html')

def video_gallery(request):
    return render(request,'homeapp/video.html')

def social_activities(request):
    return render(request,'homeapp/social.html')    

def type(request):
    return render(request,'homeapp/type.html')       

def criteria(request):
    return render(request,'homeapp/criteria.html')   

def history(request):
    return render(request,'homeapp/history.html')  

def membership(request):
    return render(request,'homeapp/membership.html') 

def eventpage(request):
    queryset = Event.objects.values('status').get(pk=2)
    print(queryset['status'])
    context ={
        'reg_status':queryset['status'],
        'event_title':Event.objects.values('title').get(pk=2)['title'],
    }
    
    if request.method == 'POST':
        your_name = request.POST.get('your_name')
        father_name = request.POST.get('father_name')
        mother_name = request.POST.get('mother_name')
        nid_number = request.POST.get('nid_number')
        present_address = request.POST.get('present_address')
        parmanent_address = request.POST.get('parmanent_address')
        passing_year = request.POST.get('passing_year')
        dob = request.POST.get('dob')
        blood_group = request.POST.get('blood_group')
        occupation = request.POST.get('occupation')
        batchmate_name = request.POST.get('batchmate_name')
        batchmate_phone_number = request.POST.get('batchmate_phone_number')
        your_phone_number = request.POST.get('your_phone_number')
        your_email = request.POST.get('your_email')
        reg_model = Registration(
            your_name=your_name,
            father_name=father_name,
            mother_name=mother_name,
            nid_number=nid_number,
            present_address=present_address,
            parmanent_address=parmanent_address,
            passing_year=passing_year,
            dob=dob,
            blood_group=blood_group,
            occupation=occupation,
            batchmate_name=batchmate_name,
            batchmate_phone_number=batchmate_phone_number,
            your_phone_number=your_phone_number,
            your_email=your_email,
            #event = Event.objects.values('id').get(pk=2)['id']
        )
        reg_model.save()
        return render(request,'homeapp/eventpage.html',context)
    return render(request,'homeapp/eventpage.html', context) 
    
def committe(request):
    return render(request, 'homeapp/committee.html')

def scholarship(request):
    return render(request, 'homeapp/scholarship.html')
