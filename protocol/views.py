import requests
from django.contrib import messages
from django.contrib.sites.models import Site
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from web3 import Web3, HTTPProvider

from .forms import IPFSTransForm
from .models import IndexInfo, Transaction, IPFS
from .serializers import WalletSerializer, DataSerializer, IPFSDataSerializer


def home(request):
    index = IndexInfo.objects.all()[0]
    current_site = Site.objects.get_current()
    w3 = Web3(HTTPProvider())
    return render(request, 'protocol/content.html', context={'domain': current_site.domain,
                                                         'index': index, 'w3': w3})


def create_text_trans(request):
    index = IndexInfo.objects.all()[0]
    return render(request, 'protocol/create_text_trans.html', context={'index': index})


def ipfs_trans(request):
    index = IndexInfo.objects.all()[0]
    data_url = ''

    if request.method == "POST":
        form = IPFSTransForm(request.POST, request.FILES)

        if form.is_valid():
            # Проверка на наличие файла в запросе
            if 'file' in request.FILES and request.FILES['file']:
                inst = form.save(commit=False)
                inst.save()
                files = {
                    'file': bytes(inst.file.read())
                }
                response = requests.post('https://ipfs.infura.io:5001/api/v0/add', files=files,
                                         auth=('29QAqPI0HxrbfPWaTYotMnpdyho', 'a1d30f9c414e15aa990a140ac924f33b'))
                data_url = 'https://ipfs.io/ipfs/' + response.json().get('Hash')
                IPFS.objects.filter().update(hash_ipfs=response.json().get('Hash'))
            else:
                messages.error(request, 'Файл не был предоставлен.')

    form = IPFSTransForm()
    return render(request, 'protocol/ipfs_trans.html', context={'index': index, 'form': form, 'data_url': data_url})


def about(request):
    index = IndexInfo.objects.all()[0]
    return render(request, 'protocol/about.html', context={'index': index})


class UpdateHashTransaction(APIView):
    def post(self, request, *args, **kwargs):
        transaction = Transaction.objects.get(id=request.data.get('id'))
        transaction.res_hash = request.data.get('res_hash')
        transaction.data = request.data.get('data')
        transaction.save()
        return Response({'res_hash': transaction.res_hash, 'transaction': transaction, 'data': transaction.data})


class CreateUserWalletAddress(APIView):
    def post(self, request, *args, **kwargs):
        serializer = WalletSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class Data(APIView):
    def post(self, request, *args, **kwargs):
        serializer = DataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class IPFSData(APIView):
    def post(self, request, *args, **kwargs):
        serializer = IPFSDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
