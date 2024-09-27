# class MyLoginView(LoginView):

#     template_name = 'login.html'  # Utilisez le nom de votre template de connexion existant
#     success_url = reverse_lazy('home')  # Remplacez 'home' par le nom de votre page d'accueil
 
#     # Define a view function for the login page
#     def get(self, request, *args, **kwargs):
#         print("hello Nasser and Igor, Yoroshiku Onegaishmasu")
     
#     # Check if the HTTP request method is POST (form submission)
#         if request.method == "POST":
#              print("post in action!")
             
#              email = request.POST.get('email')
         
#              password = request.POST.get('password')
#              print(password)
#         #   print(email)
#         #   print(password)
#         #   print(request)

#              if not User.objects.filter(email=email).exists():
#                  print("erroooorrrrrrrrrrrrrr!!!!!!!")
#                  messages.error(request, 'Invalid Username')
#                  return redirect('/login/')
            
#             # Display an error message if the username does not exist
         
           
          
#              user = authenticate(email=email, password=password)
#              if user is None:
#                  print("erroooorrrrrrrrrrrrrr!!!!!!!")
#                  messages.error(request, "Invalid Password")
#                  return redirect('/login/')
          
#              else:
#                 print("in the else")
#             # Log in the user and redirect to the home page upon successful login
#                 login(request, user)
#                 return redirect('/home/')
          
#         return render(request, 'login.html')