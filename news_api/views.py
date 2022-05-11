from django.shortcuts import render
import requests                                                 #added manually after installing requests module
API_KEY= '0ac0eba37dec4e38815409b47e09e2a2'

def home(request):
    country=request.GET.get('country')
    category=request.GET.get('category')

    if country:
        url= f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={API_KEY}'
        response= requests.get(url)                                                             #gets information from the url
        data=response.json()                                                                    #gets all data from the response
    
        articles = data['articles']

    else:
        url= f'https://newsapi.org/v2/top-headlines?category={category}&apiKey={API_KEY}'
        response= requests.get(url)                                                             
        data=response.json()                                                                   
    
        articles = data['articles']
                                                                 
    
        articles = data['articles']    
    context ={
       'articles': articles
    }


    return render(request,'index.html',context)