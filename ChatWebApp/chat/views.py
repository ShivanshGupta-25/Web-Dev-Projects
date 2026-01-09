from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from chat.models import ChatRoom, Message

# Create your views here. 
def index(request):
    return render(request, 'index.html')

def room(request, room):
    username = request.GET.get('username')
    room_details, created = ChatRoom.objects.get_or_create(name=room)

    return render(request, 'chat.html', {
        'room': room,
        'username': username,
        'room_details': room_details,
        })
    # return render(request, 'chat.html', {'room': room})

def checkview(request):
    room = request.POST.get('room_name')
    username = request.POST.get('username')

    if ChatRoom.objects.filter(name=room).exists():
        return redirect('/'+room+'/?username='+username)
    else:
        new_room = ChatRoom.objects.create(name=room)
        new_room.save()
        return redirect('/'+room+'/?username='+username)
    
def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']
    
    room = ChatRoom.objects.get(id=room_id)
    new_message = Message.objects.create(msg=message, user=username, room=room)
    new_message.save()
    return HttpResponse('Message Sent')

def  getMessages(request, room):
    # room = ChatRoom.objects.get(name=room)
    # messages = Message.objects.filter(room=room)
    # return JsonResponse({'messages': messages}, safe=False)
    
    try:
        room_obj = ChatRoom.objects.get(name=room)
    except ChatRoom.DoesNotExist:
        return JsonResponse({"error": "Room not found"}, status=404)

    messages = Message.objects.filter(room=room_obj).order_by('date')
    # Convert to list of dicts
    messages_data = [
        {
            "msg": msg.msg,
            "user": msg.user,
            "date": msg.date.strftime("%Y-%m-%d %H:%M:%S"),
        }
        for msg in messages
    ]

    return JsonResponse({"messages": messages_data}, safe=False)


    # room_details = ChatRoom.objects.get(name=room)
    # messages = Message.objects.filter(room=room_details.id)
    # return JsonResponse({'messages': list(messages.values())}, safe=False)
