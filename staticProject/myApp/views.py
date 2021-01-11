from django.shortcuts import render

# Create your views here.
def view1(request):
    myname="vishnu"
    fathername="R.V.SURESHACHAR"
    instagram_id="vishnuaachar"
    fav_subject="python"
    d={'name':myname,'father':fathername,'instagram':instagram_id,'favsub':fav_subject}
    return render(request,'myApp/1.html',d)