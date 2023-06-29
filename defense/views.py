from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from .models import *
from .encryption import *
from .a_encryption import *
from django.conf import settings
from django.core.files import File
import os, requests, ipfsapi,json
from requests.auth import HTTPBasicAuth
from django.contrib.auth import login, logout, authenticate
# Create your views here.
def user_login(request):
	if request.user.role == 'militarychief':
		return redirect('militarychief_dashboard')
	if request.user.role == "militarypersonal":
		return redirect('militarypersonal_dashboard')
	if request.user.role == 'controlcenter':
		return redirect('controlcenter_dashboard')


@login_required(login_url='login')
@csrf_exempt
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

@login_required(login_url='login')
@csrf_exempt
def militarychief_dashboard(request):
	blockchain = request.user.blockchain
	zero_proof = request.user.zero_proof
	p_request = Request.objects.filter(tusername=request.user.username,status='Pending')
	a_request = Request.objects.filter(tusername=request.user.username).exclude(status='Pending')
	if request.method == 'POST':
		if request.POST.get('accept'):
			username = request.user.username
			b_id = request.POST['b_id']
			Request.objects.filter(tusername=username,id=b_id).update(status='Accepted')
			messages.success(request, 'Request Accepted! Click on Accepted Request Section on check your requests.',extra_tags='accept')
		else:
			paper = request.FILES.get('paper',None)
			key = encrypt_file(paper)
			new_file = {'file': open('static/encrypted_files/'+str(paper)+'.encrypted',"rb")


			}
			url = 'https://ipfs.infura.io:5001/api/v0/add'
			headers = {'Accept': 'application/json'}
                        api_secrets =""
                        api_keys = ""
			auth = HTTPBasicAuth('api_secrets', 'api_keys')
			
			api= requests.post(url, headers=headers, auth=auth, files=new_file)
			p= api.json()
			hash_id = p['Hash']
			arr = a_encryption(hash_id,key,request.user.personal_id)
			file_ = open(os.path.join(settings.ENCRYPTION_ROOT,request.user.personal_id+'_private_key.pem'),'rb')
			p_file = File(file_)
			store = Request.objects.get(tusername=request.user.username)
			store.private_key.save(request.user.personal_id+'_private_key.pem',p_file,save=True)
			store.enc_field = arr
			store.status = 'Uploaded'
			store.save()
			messages.success(request, 'Paper uploaded successfully!', extra_tags='upload')
			print(p)
	return render(request,'militarychief.html',{'p_request':p_request,'a_request':a_request, 'blockchain': blockchain, 'zero_proof': zero_proof})

@login_required(login_url='login')
@csrf_exempt
def militarypersonal_dashboard(request):
	blockchain = request.user.blockchain
	zero_proof = request.user.zero_proof
	if request.method == "POST":
		file_code = request.POST['file_code']
		t_id = request.POST['t_id']
		Request.objects.filter(file_code=file_code).exclude(id=t_id).delete()
		queryset,created = Request.objects.update_or_create(id=t_id,defaults={'status':'Finalized'})
		messages.success(request, 'Paper has been finalized and sent to respective Control Center.')
		f_papers = Request.objects.filter(id=t_id).values('tusername','enc_field','private_key','file_code')
		for paper in f_papers:
			militarychief = CustomUser.objects.filter(username=paper['tusername']).values('department','base','country','mission')
			values = a_decryption([paper['enc_field'],paper['private_key']])
			hash_id = values[1].decode('utf-8')
			headers = {'Accept': 'application/json'}
                        api_secrets = ""
                        api_keys = ""
			auth = HTTPBasicAuth('api_secrets','api_keys' )
			r = requests.post('https://ipfs.infura.io:5001/api/v0/cat?arg='+hash_id, headers=headers, auth=auth)
			print(r)
			print(len(file_code))
			final_paper = decrypt_file(r,values[0],paper['file_code'])
			FinalPapers.objects.create(file_code=paper['file_code'], department=militarychief[0]['department'],base=militarychief[0]['base'],
				country=militarychief[0]['country'], mission=militarychief[0]['mission'])
			final = FinalPapers.objects.latest('id')
			final.paper.save(paper['file_code']+'.pdf',final_paper,save=True)
	requests_ = Request.objects.values('tusername','status')
	arr = []
	for r in requests_:
		name = CustomUser.objects.filter(username=r['tusername']).values('first_name','last_name')
		arr.append({'name':name[0]['first_name']+ " " + name[0]['last_name'],'status':r['status']})
	return render(request,'militarypersonnel.html',{'arr':arr, 'blockchain': blockchain, 'zero_proof': zero_proof})
@login_required(login_url='login')
@csrf_exempt
def controlcenter_dashboard(request):
	blockchain = request.user.blockchain
	zero_proof = request.user.zero_proof
	queryset = FinalPapers.objects.all()
	return render(request,'controlcenter.html',{'queryset':queryset, 'blockchain': blockchain, 'zero_proof': zero_proof})

def get_chief(request):
    department = request.POST.get('department', None)
    base = request.POST.get('base', None)
    country = request.POST.get('country', None)
    mission = request.POST.get('mission', None)
    queryset1 = Request.objects.values('tusername').distinct()
    file_code = FileCode.objects.filter(mission=mission).values()
    if file_code:
        file_code = file_code[0]['file_code']
        queryset2 = Request.objects.filter(file_code=file_code, status='Uploaded').values('id')
        queryset = CustomUser.objects.filter(department=department, base=base, country=country, mission=mission).exclude(username__in=queryset1).values()
        data = {'queryset': list(queryset), 'file_code': file_code, 'queryset2': list(queryset2)}
        return JsonResponse(data)
    else:
        data = {'queryset': [], 'file_code': '', 'queryset2': []}
        return JsonResponse(data)

def add_chief(request):
	file_code = request.POST.get('file_code',None)
	file1 = request.FILES.get('file1',None)
	file2 = request.FILES.get('file2',None)
	t_id = request.POST.get('g_id')
	"""deadline = request.POST.get('deadline',None)"""
	username = CustomUser.objects.filter(id=t_id).values('username')
	print(file_code,file1,t_id)
	Request.objects.create(tusername=username[0]['username'],file_code=file_code,file1=file1,file2=file2)
	new_chief = CustomUser.objects.filter(username=username[0]['username']).values()
	return JsonResponse({'new_chief':list(new_chief)})