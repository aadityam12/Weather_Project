from django.shortcuts import render
import requests

# Create your views here.
def home(request):
	if request.GET.get("city") and request.GET.get("btn"):
		city = request.GET.get("city")
		try:
			a1 = "http://api.openweathermap.org/data/2.5/weather?units=metric" 
			a2 = "&q=" + city
			a3 = "&appid=" + "c6e315d09197cec231495138183954bd"
			wa = a1 + a2 + a3
			res = requests.get(wa)
			data = res.json()
			temp = data['main']['temp']
			desc = data['weather'][0]['description']
			msg = " City = " + city + "\n Temp = " + str(temp) + "\n Desc = " + desc
			icon = "http://api.openweathermap.org/img/w/" + data['weather'][0]['icon']
			return render(request,"home.html",{"msg":msg})
		except Exception as e:
			return render(request,"home.html",{"msg":str(e) + str("Invalid City Name")})
	else:
		return render(request,"home.html")

			
